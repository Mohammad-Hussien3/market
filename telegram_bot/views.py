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

        if "message" in data:
            chat_id = data['message']['chat']['id']
            text = data['message']['text']

            args = data.get('message', {}).get('text', '').split()
            referrer_id = args[1] if len(args) > 1 else None

            profile, created = Profile.objects.get_or_create(telegram_id=chat_id)

            if referrer_id != None:
                text = args[0]
                referrer_id = int(referrer_id)
                if referrer_id != chat_id:
                    if profile.referred_by == None:
                        profile.referred_by = referrer_id
                        referred_profile = Profile.objects.get(telegram_id=referrer_id)
                        referred_profile.points += 10
                        referred_profile.save()

            if 'first_name' in data['message']['chat']:
                profile.first_name = data['message']['chat']['first_name']
            
            if 'last_name' in data['message']['chat']:
                profile.last_name = data['message']['chat']['last_name']

            if 'username' in data['message']['chat']:
                profile.username = data['message']['chat']['username']

            profile.save()

            if text == '/start':
                self.send_welcome_message(chat_id)
                self.send_menu(chat_id)

        elif 'callback_query' in data:
            callback_data = data['callback_query']['data']
            chat_id = data['callback_query']['message']['chat']['id']
            self.handle_callback(chat_id, callback_data)

        return JsonResponse({'status': 'ok'})
    
    def send_welcome_message(self, chat_id):
        message = 'مرحبًا بك في البوت! 😊\nاستخدم الأوامر التالية للتفاعل معي:'
        payload = {
            'chat_id': chat_id,
            'text': message
        }
        requests.post(TELEGRAM_API_URL, json=payload)

    def send_menu(self, chat_id):
        commands = [
            [{'text': '🛍️ زيارة المتجر للشراء', 'web_app' : {'url': WEB_APP_URL}}],
            [{'text': '📍 عرض نقاطي', 'callback_data': 'points'}],
            [{'text': '📢 احصل على رابط الإحالة', 'callback_data': 'referral'}],
            [{'text': '📌 عرض الطلبات المعلقة', 'callback_data': 'pending_orders'}],
            [{'text': '🛒 عرض طلباتي السابقة', 'callback_data': 'my_orders'}],
        ]

        payload = {
            'chat_id': chat_id,
            'text': 'اختر أحد الخيارات:',
            'reply_markup': {'inline_keyboard': commands}
        }
        requests.post(TELEGRAM_API_URL, json=payload)
    
    def handle_callback(self, chat_id, callback_data):
        if callback_data == 'points':
            self.send_points(chat_id)
        elif callback_data == 'referral':
            self.send_referral(chat_id)

    def send_points(self, chat_id):
        profile = Profile.objects.get(telegram_id=chat_id)
        message = f'📍 لديك {profile.points} نقاط.'

        payload = {
            'chat_id': chat_id,
            'text': message
        }
        requests.post(TELEGRAM_API_URL, json=payload)
    
    def send_referral(self, chat_id):
        profile = Profile.objects.get(telegram_id=chat_id)
        message = f'رابط احالتك هوة:{profile.referral_link}.'

        payload = {
            'chat_id': chat_id,
            'text': message
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
