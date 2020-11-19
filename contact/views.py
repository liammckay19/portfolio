from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail


def contacthome(request):
    if request.method == "POST":
        email = request.POST.get('email')
        msg = request.POST.get('message')
        subject = request.POST.get('subject')
        send_mail(
            subject,
            fail_silently=False,
            message=msg,
            from_email='liammckay2019@gmail.com', recipient_list=['liammckay2019@gmail.com', email])
        return contactsuccess(request)
    else:
        form = ContactForm()
        return render(request, template_name='contact/contacthome.html', context={'form': form})

def contactsuccess(request):
    return render(request, template_name='contact/contactsuccess.html')