import json
import requests
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from usermanagament.models import Profile
from item.models import Category, Item
from item.serializers import LimitedCategorySerializer
from django.db.models import Prefetch, Count


BOT_TOKEN = "7706720810:AAHtk9RCd9nKr4a0nNWNPr2zhh4dOJE3SaQ"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
WEB_APP_URL = "https://nehad223.github.io/dsad/"


class Webhook(APIView):
    
    def post(self, request):
        
        data = json.loads(request.body)
        chat_id = data['message']['chat']['id']
        text = data['message']['text']

        profile, created = Profile.objects.get_or_create(telegram_id=chat_id)
        if 'first_name' in data['message']['chat']:
            profile.first_name = data['message']['chat']['first_name']
        
        if 'last_name' in data['message']['chat']:
            profile.last_name = data['message']['chat']['last_name']

        if 'username' in data['message']['chat']:
            profile.username = data['message']['chat']['username']

        profile.save()

        if text == '/start':
            self.send_store_button(chat_id)

        return JsonResponse({'status': 'ok'})
    
    def send_store_button(self, chat_id):
        message = f'مرحبًا بك في المتجر! 🛒 اضغط على الزر لفتح المتجر.'
        payload = {
            'chat_id': chat_id,
            'text': message,
            'reply_markup': {
                'inline_keyboard': [[
                    {'text': '🛍️ افتح المتجر', 'web_app': {'url': WEB_APP_URL}}
                ]]
            }
        }
        requests.post(TELEGRAM_API_URL, json=payload)


class HomePage(ListAPIView):
    serializer_class = LimitedCategorySerializer

    def get_queryset(self):
        queryset = Category.objects.annotate(num_items=Count('items')).filter(num_items__gt=0).order_by('name')

        queryset = queryset.prefetch_related(
            Prefetch('items', queryset=Item.objects.order_by('id')[:10], to_attr='limited_items')
        )

        return queryset
