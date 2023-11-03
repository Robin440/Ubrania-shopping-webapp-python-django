from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from Customer.models import Customer
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.contrib.auth import login
from Customer.models import Customer
from .models import Customer
from U_Admin.models import *
from Customer import views



def fresh_page(request):
    hi = 'jfgdsf'
    brand_data = Brand.objects.all()
    return render(request, 'index.html', {'brands': brand_data})



# def user_login_py(request):
#     if 'username' in request.session:
#         return redirect(user_home_py)  # Replace 'some_view' with the URL you want to redirect to for logged-in users.

#     if request.method == 'POST':
#         user_or_email = request.POST.get('name_or_email')
#         password = request.POST.get('password')

#         try:
#             user = Customer.objects.get(Q(username=user_or_email) | Q(email=user_or_email))
#         except Customer.DoesNotExist:
#             user = None

#         if user and user.check_password(password):
#             user = authenticate(request, username=user.username, password=password)
#             if user is not None:
#                 request.session['username'] = user.username
#                 login(request, user)
#                 return redirect(user_home_py) # Replace 'some_view' with the URL for the post-login view.
#         else:
#             messages.error(request, 'Password or Username is wrong')

#     return render(request,'user_login.html')



def user_home_py(request):

    if 'username' in request.session:

        brand_data = Brand.objects.all()
        prod_data = Product.objects.all()
        sec = Section.objects.all()

        first_name = request.session.get('username','Guest')
    
        return render(request,'user_home.html', {'brands': brand_data,'tst':first_name,'product':prod_data,'sect_data':sec})
    return redirect(user_login_py)


def user_logout_py(request):
    request.session.flush()
    logout(request)
    return render(request,'index.html')



def user_register_py(request):
    if request.method == 'POST':
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        dob = request.POST.get('dob')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        username = request.POST.get('user_name')

        if password == password2:
            # Check if the user with the given username or email already exists
            if Customer.objects.filter(username=username).exists() or Customer.objects.filter(email=email).exists():
                messages.error(request, 'Username or email already exists.')
            else:
                # Create a new user
                customer = Customer(username=username, first_name=f_name, last_name=l_name, email=email, mobile=mobile, dob=dob, password=password)
                customer.save()
                messages.success(request, 'Account created successfully. Please login to explore.')
                return redirect('user_login')

        else:
            messages.error(request, 'Password is not matching. Try again.')

    return render(request, 'user_register.html')



def user_login_py(request):
    if request.method == 'POST':
        username = request.POST.get('name_or_email')
        password = request.POST.get('password')
        user = Customer.objects.get(Q(username=username) | Q(email=username), password=password)
        if user is not None:
            request.session['username']=username
            messages.success(request, 'Login successful.')
            brand_data = Brand.objects.all()
            return redirect(user_home_py)
        else:
            messages.error(request,'Invalid Credentials')
          # Replace with your post-login page
        # messages.error(request, 'Password or username is wrong.')

    return render(request, 'user_login.html')
