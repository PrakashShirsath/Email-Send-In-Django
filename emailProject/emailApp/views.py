from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

def homePage(request):
    return render(request, 'emailApp/index.html')

def sendEmail(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        location = request.POST.get('location', '')
        message = request.POST.get('message', '')
        fromEmail = request.POST.get('fromEmail', '')
        recipientEmail = request.POST.get('recipientEmail', '')

        try:
            send_mail(
                f"New message from {name}",
                f"Name: {name}\nPhone: {phone}\nLocation: {location}\nMessage: {message}\nFrom: {fromEmail}",
                fromEmail,
                [recipientEmail],
                fail_silently=False,
            )
            return HttpResponse('Email Sent Successfully')
        except Exception as e:
            return HttpResponse('Email could not be sent')
    else:
        return render(request, 'emailApp/index.html')
