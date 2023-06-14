from django.urls import path, include
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from django.urls import path
from .import views


from django.urls import path
# from .views import LogoutView

from django.urls import path
# from .views import PasswordResetView



urlpatterns = [



    path('list/', views.doc_list, name='doc_list'),
    path('doc/<int:pk>/', views.doc_detail, name='doc_detail'),
    path('addFile/', views.add, name='add_file'),
    path('doc/update/<int:pk>/', views.update, name='doc_update'),
    path('doc/delete/<int:pk>/', views.delete, name='doc_delete'),
   
    path('home/',views.home, name='home'),
    path('search/',views.search_docs, name='search'),
    path('fich/',views.fichier, name='fichier'),


    path('addFile/', RedirectView.as_view(url="/admin"),name="redirect-admin"),
    
    path('register/user_type_1/', views.register1, name='registerE'),
    path('register/user_type_2/', views.register2, name='registerA'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password_reset/', views.password_reset, name='password_reset'),


    # path('redirect-admin', RedirectView.as_view(url="addFile/"),name="redirect-admin"),







    # path('password_reset/', PasswordResetView.as_view(), name='password_reset'),


   
    # path('prof/login/', UserLoginView.as_view(template_name='login.html'), name='prof_login'),
    # path('etudiant/login/', UserLoginView.as_view(template_name='login.html'), name='etudiant_login'),








]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)