from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt
# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for error in errors.values():
            messages.error(request, error)
        return redirect('/')
    hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    this_user = User.objects.create( 
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=hashed
    )
    request.session['user_id'] = this_user.id
    return redirect('/')

def login(request):
    users = User.objects.filter(email=request.POST['email'])
    if users:
        logging_in_user = users[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logging_in_user.password.encode()):
            request.session['user_id'] = logging_in_user.id
            return redirect('/')
    messages.error(request, "Email not found")
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')