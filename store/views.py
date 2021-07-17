from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.urls import reverse
from .models._user import User1
from .models.chatroom import CHAT_MESSAGE
from .forms import CHATFORM
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.
# @login_required(login_url='/login/')
def home(request):
    return render(request,'home.html')

def register(request):
    # return render(request,'register.html')
    # return HttpResponse('Index Page')
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        # postData = request.POST
        name1 = request.POST.get('name1')
        phno = request.POST.get('phno')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # VALIDATING
        value = {
            'name1': name1,
            'phno': phno,
            'email': email
        }
        error_mess = None

        _user = User1(name1=name1,
                            phno=phno,
                            email=email,
                            password=password)
        if (not name1):
            error_mess = "Name is Required !!"
        elif (not phno):
            error_mess = "Phone No. is Required !!"
        elif len(phno) < 10:
            error_mess = "Phone No. Should be 10 digits !!"
        elif (not email):
            error_mess = "Email is Required !!"
        elif (not password):
            error_mess = "Password is Required !!"
        elif _user.isExists():
            error_mess = "Email Address Already Registered !!"

        # SAVING
        if (not error_mess):
            _user.password = make_password(_user.password)
            _user.register()
            # send_mail(
            #     'Subject here',
            #     'Here is the message.',
            #     settings.EMAIL_HOST_USER,
            #     ['50badshahraj@gmail.com'],
            #     fail_silently=False,
            # )
            # if customer.register():
            #     send_mail(
            #         {{name1}},
            #         {{phno}},
            #         settings.EMAIL_HOST_USER,
            #         ['50badshahraj@gmail.com'],
            #         fail_silently=False,
            #     )

            return redirect('home')
        else:
            data = {
                'error_mess': error_mess,
                'values': value
            }
            return render(request, 'register.html', data)


def login(request):
    # return render(request,'login.html')
    if request.method == 'GET':
        return render(request,'login.html',{})
    else:
        email=request.POST.get('email')
        password = request.POST.get('password')
        user = User1.get_customer_by_email(email)
        error_mess = None
        if user:
            flag = check_password(password,user.password)
            if flag:
                return redirect('profile')
            else:
                error_mess="Invalid Email Or Password !!"
        else:
            error_mess = "Invalid Email Or Password !!"
        return render(request,'login.html',{'error':error_mess})

def sign_out(request):
    logout(request)
    messages.success(request, "You've been signed out. Come back soon!")
    return HttpResponseRedirect(request,reverse('home'))


def profile(request):
    profile = request.user.profile
    return render(request, 'profile.html', {'profile': profile})

@login_required()
def chatroom(request):
    command = 0
    chatForm = CHATFORM(request.POST)
    chatMessages = CHAT_MESSAGE.objects.all()
    if chatForm.is_valid():
        message = chatForm.cleaned_data["message"]
        if message == "!help" or message == "!commands":
            command = 1
        else:
            command = 0
            CHAT_MESSAGE.objects.get_or_create(messageText=message )

    else:
        pass

    data = {
        "form" : chatForm,
        "msgs" : chatMessages,
        "command": command
    }

    return render(request,"chatroom.html",data)



@login_required
def view_profile(request):
    profile = request.user.profile
    return render(request, 'profile.html', {'profile':profile})