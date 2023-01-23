from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from base64 import urlsafe_b64decode, urlsafe_b64encode 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
# Create your views here.
def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']
        if password != confirm_password:
            messages.warning(request, "Password did't Match")
            return render(request,'signup.html')
        try:
            if User.objects.get(username=email):
                messages.error(request,"Email Already Exist")
                return render(request,'signup.html')
                
        except Exception as identifier:
            pass
        user = User.objects.create_user(email,email,password)    
        user.is_active=False
        user.save()
        email_subject = "Activate Your Account"
        message = render_to_string('activate.html',{
            'user':user,
            'domain':'127.0.0.1:8000',
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':generate_token.make_token(user),
        })
        email_message = EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[email])
        email_message.send()
        messages.success(request,'Activate Your Account by clicking the link in your gmail')
        return redirect('login')
    return render(request, 'signup.html')

def loginview(request):
    return render(request, 'login.html')

def logoutview(request):
    return redirect('/login/')