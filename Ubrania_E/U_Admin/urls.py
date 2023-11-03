from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from U_Admin import views

urlpatterns = [
    path('admin_dashboard',views.admin_dashboard_py,name='admin_dash'),
    path('admin_dashboard/customer_view',views.customer_views_py,name='cus_view'),
    path('admin_dashboard/product_view',views.product_view_py,name='prod_view'),
    path('admin_dashboard/product_update',views.product_update_py,name='prod_update'),
   
    path('admin_dashboard/section_brand_update',views.section_brand_py,name='section_brand'),
    path('admin_dashboard/section_add',views.section_add_py,name='section_add'),
 
    path('admin_dashboard/brand_add',views.brand_add_py,name='brand_add'),
    path('edit_products/<int:product_id>/',views.edit_product, name='edit_prod')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)