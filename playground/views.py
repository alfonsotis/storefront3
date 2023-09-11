from django.shortcuts import render
from django.core.cache import cache
from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
from templated_mail.mail import BaseEmailMessage
import requests


def say_hello(request):
    key = 'httpbin_result'
    if cache.get(key) is None:
        response = requests.get('https://httpbin.org/delay/2')
        data = response.json()
        cache.set(key, data, 10*60)
    
    return render(request, 'hello.html', {'name': cache.get(key)})
