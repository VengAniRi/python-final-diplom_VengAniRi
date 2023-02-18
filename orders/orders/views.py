from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime


# Create your views here.

@api_view(['GET'])
def index(request):
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    data = {
        'Сообщение': 'Добро пожаловать на мой проект!',
        'Время сейчас на сервере': time,
        'URL API заказов ТУТ --->': 'http://127.0.0.1:8000/api/v1/',
        'Aдминка ТУТ --->': 'http://127.0.0.1:8000/admin/login/?next=/admin/',
        'Login в Админке': 'irissk.a@yandex.ru',
        'Пароль в Админке': 'admin'
    }
    return Response(data)
