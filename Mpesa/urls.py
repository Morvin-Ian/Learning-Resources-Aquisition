from django.contrib import admin
from django.urls import include,path
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_view.LoginView.as_view(template_name='UserApp/login.html') , name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='UserApp/login.html') , name='logout'),
    path('',include('UserApp.urls')),
    path('api/',include('DarajaApp.Api.urls')),
    path('resource/',include('ResourceApp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)

