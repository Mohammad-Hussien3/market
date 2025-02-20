import json
import requests
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from usermanagament.models import Profile
from item.models import Category
from rest_framework.pagination import PageNumberPagination
from item.serializers import CategorySerializer


BOT_TOKEN = "7706720810:AAHtk9RCd9nKr4a0nNWNPr2zhh4dOJE3SaQ"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
WEB_APP_URL = "https://market-cwgu.onrender.com/bot/homepage/"


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


class CategoryPagination(PageNumberPagination):
    page_size = 10


class HomePage(ListAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = CategoryPagination
