from django.shortcuts import render,redirect

# Create your views here.
def signup(request):
    return render(request, 'signup.html')

def loginview(request):
    return render(request, 'login.html')

def logoutview(request):
    return redirect('/login/')