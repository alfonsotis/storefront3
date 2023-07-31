from django.shortcuts import render
from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage


def say_hello(request):

    try:
        message = EmailMessage('this is the subject of the admin mail',
                     'This is the message... very long or not',
                    'alfonso@alfonso.com',
                    ['info@alfonso.com', 'info@lupilu'])
        message.attach_file('playground/static/images/chess.jpeg')
        message.send()


    except BadHeaderError:
        pass

    return render(request, 'hello.html', {'name': 'Super Alfonso'})
