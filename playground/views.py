from django.shortcuts import render
from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
from templated_mail.mail import BaseEmailMessage
import requests


def say_hello(request):
    requests.get('https://httpbin.org/delay/2')
    
    return render(request, 'hello.html', {'name': 'Super Alfonso'})
