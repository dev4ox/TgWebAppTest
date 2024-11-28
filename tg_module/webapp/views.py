from django.shortcuts import render
from django.http import JsonResponse
import json


def index(request):
    return render(request, 'webapp/index.html')


def order_service(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        service = data.get('service')
        return JsonResponse({'status': 'success', 'message': 'Заказ принят!'})
    return JsonResponse({'status': 'error', 'message': 'Метод не поддерживается'}, status=400)
