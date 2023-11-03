from django.shortcuts import get_object_or_404, redirect, render
from Customer.models import Customer
from U_Admin.models import Product,Brand, Section
from U_Admin.models import *
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.views.decorators.cache import never_cache

# Create your views here.
def admin_dashboard_py(request):
    return render(request,'admin_temp/index.html')

def customer_views_py(request):
    cus_data = Customer.objects.all()
    return render(request, 'admin_temp/customer_view.html', {'cus_dict':cus_data})

def product_view_py(request):
    Prod_data = Product.objects.all()

   

    return render(request, 'admin_temp/product.html', {'product':Prod_data})


# def product_update_py(request):
#     brand_data = Brand.objects.all()
#     section_data = Section.objects.all()
#     if request.method == "POST":
    
#         prod_name = request.POST.get('productname')
#         brand_name = request.POST.get('brand_info')
#         section_name = request.POST.get('section_info')
#         discount = request.POST.get('discount')
#         size = request.POST.get('Size')
#         qty = request.POST.get('qty')
#         insert_data = Product.objects.create(pname=prod_name,brand_id=brand_name,section_id=section_name,discount=discount,size=size,Qty=qty)
#         insert_data.save
#         return render(request,'admin_temp/prod_update.html',{'brand_data':brand_data, 'section_data':section_data})

#     brand_data = Brand.objects.all()
#     section_data = Section.objects.all()
#     return render(request,'admin_temp/prod_update.html',{'brand_data':brand_data, 'section_data':section_data})



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
        image_1 =request.FILES.get('producIMG1')
        image_2 =request.FILES.get('producIMG2')
        image_3 =request.FILES.get('producIMG3')

        # Create a new product instance
    
        prod_data.pname=prod_name
        prod_data.brand_id=brand_name,
        prod_data.section_id=section_name,
        prod_data.discount=discount,
        prod_data.small = small,
        prod_data.large = large,
        prod_data.xl = xl,
        prod_data.xxl=xxl,
        prod_data.xxxl = xxxl,
        prod_data.Qty=qty,
        prod_data.price=price,
        prod_data.prod_pic=image_1,
        prod_data.prod_data_two=image_2,
        prod_data.prod_data_three=image_3
            
        
        prod_data.save()

            
        

    return render(request, 'admin_temp/edit_product.html',{'prod_data':prod_data,'brand_data':brand_data,'sect_data':sect_data})
    