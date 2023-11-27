from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from Customer.models import Customer
from U_Admin.models import Product,Brand, Section
from U_Admin.models import *
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.views.decorators.cache import never_cache
from django.contrib import messages
# Create your views here.
def admin_dashboard_py(request):

    return render(request,'admin_temp/index.html')

def customer_views_py(request):
    cus_data = Customer.objects.all()
    return render(request, 'admin_temp/customer_view.html', {'cus_dict':cus_data})

def product_view_py(request):
    Prod_data = Product.objects.all()

   

    return render(request, 'admin_temp/product.html', {'product':Prod_data})


from django.core.files.base import ContentFile
from .models import Product  # Import your models

def product_update_py(request):
    brand_data = Brand.objects.all()
    section_data = Section.objects.all()

    if request.method == "POST":
        prod_name = request.POST.get('productname')
        brand_name = request.POST.get('brand_info')
        section_name = request.POST.get('section_info')
        discount = request.POST.get('discount')
        small = request.POST.get('small')
        large = request.POST.get('large')
        xl = request.POST.get('XL')
        xxl = request.POST.get('XXL')
        xxxl = request.POST.get('XXXL')
        qty = request.POST.get('qty')
        price = request.POST.get('price')
        image_i =request.FILES.getlist('producIMG')

        # Create a new product instance
        new_product = Product(
            pname=prod_name,
            brand_id=brand_name,
            section_id=section_name,
            discount=discount,
            small = small,
            large = large,
            xl = xl,
            xxl=xxl,
            xxxl = xxxl,
            Qty=qty,
            price=price,
            
        )
        new_product.save()

        # Process and associate uploaded images with the product
        for idx, img in enumerate(image_i):
            if idx == 0:
                new_product.prod_pic.save(img.name, img)
            elif idx == 1:
                new_product.prod_pic_two.save(img.name, img)
            elif idx == 2:
                new_product.prod_pic_three.save(img.name, img)


        return render(request, 'admin_temp/prod_update.html', {'brand_data': brand_data, 'section_data': section_data})

    return render(request, 'admin_temp/prod_update.html', {'brand_data': brand_data, 'section_data': section_data})


def section_brand_py(request):
    sections = Section.objects.all()
    brands = Brand.objects.all()

    return render(request, 'admin_temp/section_brand.html',{'sections':sections,'brands':brands})

def section_add_py(request):
    sections = Section.objects.all()
    if request.method =='POST':
        section_name = request.POST.get('section_name')
        discount_section = request.POST.get('discount_section')
        sectimg = request.FILES.get('sectionIMG')
        data = Section.objects.create(sectiontype=section_name,discount=discount_section,section_img=sectimg)
        data.save()
        return render(request,'admin_temp/Section_update.html',{'sections':sections})

    return render(request,'admin_temp/Section_update.html',{'sections':sections})

def brand_add_py(request):
    brands = Brand.objects.all()
    if request.method =='POST':
        brand_name = request.POST.get('brand_name')
        discount_brand = request.POST.get('discount_brand')
        brandimg = request.FILES.get('brandIMG')
        data = Brand.objects.create(brand=brand_name,discount=discount_brand,brand_img=brandimg)
        data.save()
        return render(request,'admin_temp/brand_update.html',{'brands':brands})

    return render(request,'admin_temp/brand_update.html',{'brands':brands})


@never_cache

def edit_product(request, product_id):
    prod_data = get_object_or_404(Product, pk=product_id)
    brand_data = Brand.objects.all()
    sect_data = Section.objects.all()

    if request.method == "POST":
        prod_data.pname = request.POST.get('productname')
        prod_data.brand_id = request.POST.get('brand_info')
        prod_data.section_id = request.POST.get('section_info')
        prod_data.discount = request.POST.get('discount')
        prod_data.small = request.POST.get('small')
        prod_data.large = request.POST.get('large')
        prod_data.xl = request.POST.get('XL')
        prod_data.xxl = request.POST.get('XXL')
        prod_data.xxxl = request.POST.get('XXXL')
        prod_data.Qty = request.POST.get('qty')
        prod_data.price = request.POST.get('price')
        prod_data.prod_pic = request.FILES.get('producIMG1')
        prod_data.prod_data_two = request.FILES.get('producIMG2')
        prod_data.prod_data_three = request.FILES.get('producIMG3')

        prod_data.save()
        return redirect(product_view_py)

    return render(request, 'admin_temp/edit_product.html', {'prod_data': prod_data, 'brand_data': brand_data, 'sect_data': sect_data})

def delete_product(request, product_id):
    prod_data = get_object_or_404(Product, pk=product_id)
    
    # if request.user.is_superuser or request.user.has_perm('auth.delete_user'):
    prod_data.delete()
    # else:
      
    #     return HttpResponseForbidden("You don't have permission to delete users.")
    
    return redirect(product_view_py) 

def section_edit_py(request,section_id):
    sect_data = get_object_or_404(Section,pk=section_id)
    if request.method == "POST":
        sect_data.sectiontype = request.POST.get('sect_name')
        sect_data.discount=request.POST.get('discount')
        if 'sect_img' in request.FILES:
            sect_data.section_img =request.FILES.get('sect_img')
        sect_data.save()
        return redirect(section_brand_py)
    return render(request,'admin_temp/edit_section.html', {'sect':sect_data})

def delete_section_py(request,section_id):
    sect_data = get_object_or_404(Section,pk=section_id)
    sect_data.delete()
    return redirect(section_brand_py)


def brand_edit_py(request,brand_id):
    brand_data = get_object_or_404(Brand,pk=brand_id)
    if request.method == "POST":
        brand_data.brand = request.POST.get('brand_name')
        brand_data.discount=request.POST.get('discount')
        if 'brand_img' in request.FILES:
            brand_data.section_img =request.FILES.get('brand_img')
        brand_data.save()
        return redirect(section_brand_py)
    return render(request,'admin_temp/brand_edit.html', {'brand':brand_data})

def customer_edit_py(request, customer_id):
    customer_data = get_object_or_404(Customer, pk=customer_id)

    if request.method == 'POST':
        # Get the form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        dob = request.POST.get('dob')
        username = request.POST.get('user_name')

        # Check if the username or email is changed
        if (
            username != customer_data.username
            and Customer.objects.filter(username=username).exists()
        ) or (
            email != customer_data.email and Customer.objects.filter(email=email).exists()
        ):
            messages.error(request, 'Username or email already exists.')
        else:
            # Update customer data
            customer_data.first_name = first_name
            customer_data.last_name = last_name
            customer_data.email = email
            customer_data.mobile = mobile
            customer_data.dob = dob
            customer_data.username = username

            # Save the customer data
            customer_data.save()

            return redirect(customer_views_py)

    return render(request, 'admin_temp/customer_edit.html', {'cust_data': customer_data})

def customer_del_py(request, customer_id):
    # Retrieve the customer instance or return a 404 response if not found
    customer = get_object_or_404(Customer, pk=customer_id)

    # Check if the request method is POST (to prevent accidental deletions)
    
    customer.delete()
        

    return redirect(customer_views_py)

def block_cust_py(request,customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    customer.is_blocked=True
    customer.save()
    return redirect(customer_views_py)
def unblock_cust_py(request,customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    customer.is_blocked=False
    customer.save()
    return redirect(customer_views_py)

def delete_brand_py(request,brand_id):
    brand_data = get_object_or_404(Brand,pk=brand_id)
    brand_data.delete()
    return redirect(section_brand_py)

def o_c_py(request):
    o_c_d = Offer_Coupon.objects.all()
    return render(request,'admin_temp/Offer&Coupon.html',{'oc_data':o_c_d})

def o_c_update(request,):
    o_c_d = Offer_Coupon.objects.all()
    if request.method =='POST':
        oc_name = request.POST.get('oc_name')
        discount = request.POST.get('discount')
        validaty = request.POST.get('validaty')
        oandd = Offer_Coupon(o_c_name=oc_name,discount=discount,validity=validaty)
        oandd.save()
    
    return render(request,'admin_temp/oc_update.html',{'oc_data':o_c_d,})

def oc_delete(request,offer_coupon_id):
    oc_data = get_object_or_404(Offer_Coupon,pk=offer_coupon_id)
    oc_data.delete()
    return redirect(o_c_py)

def oc_edit(request,offer_coupon_id):
    oc_data = get_object_or_404(Offer_Coupon,pk=offer_coupon_id)
    if request.method == 'POST':
        oc_data.o_c_name = request.POST.get('oc_name')
        oc_data.discount = request.POST.get('discount')
        oc_data.validity = request.POST.get('validaty')
        oc_data.save()
        return redirect(o_c_py)
        
    return render(request,'admin_temp/oc_edit.html',{'oandc':oc_data})

def block_oc(request,offer_coupon_id):
    oc_data = get_object_or_404(Offer_Coupon,pk=offer_coupon_id)
    oc_data.is_blocked = True
    oc_data.save()
    return redirect(o_c_py)

def unblock_oc(request,offer_coupon_id):
    oc_data = get_object_or_404(Offer_Coupon,pk=offer_coupon_id)
    oc_data.is_blocked = False
    oc_data.save()
    
    return redirect(o_c_py)
