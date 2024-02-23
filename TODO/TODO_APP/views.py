from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import todo



# Create your views here.
@login_required
def home(request):
    if request.POST:
        task = request.POST['task']
        new_todo = todo(user=request.user, todo_name=task)
        new_todo.save()
        return redirect('home')

    todos = todo.objects.filter(user= request.user).order_by('-id')
    context = {'todos': todos}
    return render(request,'index.html' , context)

def user_logout(request):
    auth.logout(request)
    return redirect("login")


def user_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('doing')
        try:
            user = User.objects.get(username=username)
            print(user)
        except Exception as e:
            return render(request, 'authentication/login.html', {'error': 'User does not exist'})
            
    
        user = auth.authenticate(username = username, password = password)
        print("doing")
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request, 'authentication/login.html', {'error': 'Incorrect Password'})
    return render(request,'authentication/login.html')

def user_signup(request):
    if request.POST:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=email).exists():
            return render(request, 'authentication/signup.html', {'error': 'User already exists'})

        data = User.objects.create_user(username=email,first_name=firstname, last_name=lastname, email=email, password=password)
        data.save()
        return redirect('login')

    return render(request,'authentication/signup.html')


def delete(request, id):
    task = todo.objects.get(user=request.user, id = id)
    task.delete()
    return redirect('home')


def update(request, id):
    task = todo.objects.get(user=request.user, id = id)
    task.status = True
    task.save()
    return redirect('home')