from django.contrib import admin
from django.urls import path
from Customer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.fresh_page,name='fresh_page'),
    path('user_login/', views.user_login_py,name='user_login'),
    path('user_registration',views.user_register_py,name='user_register'),
    path('user_home/',views.user_home_py,name='user_home'),
    path('user_logout',views.user_logout_py,name='user_logout')
    
]
# urls.py

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
