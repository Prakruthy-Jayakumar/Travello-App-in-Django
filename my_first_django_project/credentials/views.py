from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def registration(request):
    if request.method == 'POST':
        username =  request.POST['username']
        first_name =  request.POST['firstname']
        last_name =  request.POST['lastname']
        email =  request.POST['email']
        password =  request.POST['pass']
        confirm_password =  request.POST['re_pass']
        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username is already taken")
                return redirect('registration')
            elif User.objects.filter(email = email).exists():
                messages.info(request, "Email is already taken")
                return redirect('registration')
            else:
                user = User.objects.create_user(username = username,
                                   first_name = first_name,
                                   last_name = last_name,
                                   email = email,
                                   password = password)
                user.save();
                return redirect('login')
                # print("User created")
                # messages.info(request, "user created")

        else:
            messages.info(request, "password not matching")
            return redirect('registration')
        # print("password not matching")
        # return redirect('/')

    return render(request, 'registration.html')

def login(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['your_pass']
        fetch_details = auth.authenticate(username = user_name, password = password)
        if fetch_details is not None:
            auth.login(request,fetch_details)
            # print("yes here")
            # messages.info(request, "success")
            return redirect('/')
        else:
            # print("not here")
            messages.info(request,"invalid credentials")
            return redirect('login')


    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')