from django.shortcuts import render
from django.core.mail import send_mail, mail_admins, BadHeaderError


def say_hello(request):

    try:
        mail_admins('this is the subject of the admin mail',
                     'This is the message... very long or not', 
                     html_message='<h1> Hello from theother side </h1>' )
        # send_mail('subject', 'message',
        #           'info@alfonso.com', ['bob@alfonso.com'])
    except BadHeaderError:
        pass

    return render(request, 'hello.html', {'name': 'Super Alfonso'})
