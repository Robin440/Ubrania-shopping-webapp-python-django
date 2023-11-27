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
from django.views.decorators.cache import never_cache


def fresh_page(request):
    if 'username' in request.session:
        return redirect(user_home_py)
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



@never_cache
def user_home_py(request):
    
    if 'username' in request.session:
        username = request.session.get('username', 'Guest')
        
        # Retrieve the user instance from the database
        user = Customer.objects.get(username=username)

        # Check if the user is blocked
        if not user.is_blocked:
            brand_data = Brand.objects.all()
            prod_data = Product.objects.all()
            sec = Section.objects.all()

            return render(request, 'user_home.html', {'brands': brand_data, 'tst': username, 'product': prod_data, 'sect_data': sec})
        else:
            # Add a message indicating that the user is blocked
            messages.error(request, 'Your account is blocked.')

    # If the username is not in the session or the user is blocked, redirect to login
    return redirect(user_login_py)

@never_cache
def user_logout_py(request):
    request.session.flush()
    logout(request)
    return render(request,'index.html')


@never_cache
def user_register_py(request):
    if 'username' in request.session:
        return redirect(user_home_py)
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



from django.core.exceptions import ObjectDoesNotExist

# views.py

@never_cache
def user_login_py(request):
    if 'username' in request.session:
        return redirect(user_home_py)
    if request.method == 'POST':
        username = request.POST.get('name_or_email')
        password = request.POST.get('password')

        try:
            user = Customer.objects.get(Q(username=username) | Q(email=username), password=password)

            # Check if the user is blocked
            if user.is_blocked:
                messages.error(request, 'Your account is blocked. Contact support for assistance.')
                return render(request, 'user_login.html')

            # If not blocked, set session data and redirect
            request.session['username'] = username
            messages.success(request, '')
            brand_data = Brand.objects.all()
            return redirect(user_home_py)

        except ObjectDoesNotExist:
            messages.error(request, 'Invalid Credentials')
            return render(request, 'user_login.html')

    return render(request, 'user_login.html')
