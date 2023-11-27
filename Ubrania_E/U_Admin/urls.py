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
    path('edit_products/<int:product_id>/',views.edit_product, name='edit_prod'),
    path('delete_user/<int:product_id>/', views.delete_product, name='delete_prod'),
    path('section_edit/<int:section_id>/',views.section_edit_py,name='sect_edit'),
    path('delete_section/<int:section_id>',views.delete_section_py,name='delete_sect'),
    path('brand_edit/<int:brand_id>',views.brand_edit_py,name='brand_edit'),
    path('brand_delete/<int:brand_id>',views.delete_brand_py,name='delete_brand'),
    path('customer_edit/<int:customer_id>',views.customer_edit_py,name='edit_cust'),
    path('customer_delete/<int:customer_id>',views.customer_del_py,name='del_cust'),
    path('customer_block/<int:customer_id>',views.block_cust_py,name='block_cust'),
    path('customer_unblock/<int:customer_id>',views.unblock_cust_py,name='unblock_cust'),
    path('admin_dashboard/offer_coupon',views.o_c_py,name='o&c_view'),
    path('admin_dashboard/offers_coupon_update',views.o_c_update,name='oc_update'),
    path('admin_dashboard/offers_coupon_delete/<int:offer_coupon_id>',views.oc_delete,name='oc_delete'),
    path('admin_dashboard/offers_coupon_edit/<int:offer_coupon_id>',views.oc_edit,name='oc_edit'),
    path('admin_dashboard/offers_coupon_block/<int:offer_coupon_id>',views.block_oc,name='block_oc'),
    path('admin_dashboard/offers_coupon_unblock/<int:offer_coupon_id>',views.unblock_oc,name='unblock_oc'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)