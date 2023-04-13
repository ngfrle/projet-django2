from django.urls import path
from . import views 
from knox import views as knox_views
# from django.urls import path
from .views import RestaurateurCreateAPIView, LoginAPIView, PasswordResetAPIView, PasswordResetConfirmAPIView,RestaurateurList,DeleteRestaurateurView
# ,Clientregister,Clientlogin,Clientreset_password
urlpatterns = [
    path('',views.ListRestaurantView.as_view(), name='resto'),
    path('add_resto/',views.CreateRestaurantView.as_view(), name='create_resto'),
    path('<pk>/update_resto/',views.UpdateRestaurantView.as_view(), name='resto_update'),
    path('<pk>/delete_resto/',views.DeleteRestaurantView.as_view(), name='resto_delete'),
    path('commentaire/',views.ListCommentaireView.as_view(), name='commentaire'),
    path('add_commentaire/',views.CreateCommentaireView.as_view(), name='create_commentaire'),
    path('produit/',views.ListProduitView.as_view(), name='produit'),
    path('add_produit/',views.CreateProduitView.as_view(), name='create_produit'),
    path('<pk>/update_produit/',views.UpdateProduitView.as_view(), name='produit_update'),
    path('<pk>/delete_produit/',views.DeleteProduitView.as_view(), name='produit_delete'),
    path('register/', RestaurateurCreateAPIView.as_view()),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('password_reset/', PasswordResetAPIView.as_view()),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmAPIView.as_view()),
    path('restaurateurs/', RestaurateurList.as_view(), name='restaurateur-list'),
    path('api/restaurateurs/<int:pk>/delete/', DeleteRestaurateurView.as_view(), name='delete_restaurateur'),
    path('registerclient/', views.Clientregister, name='registerclient'),
    path('loginclient/', views.Clientlogin, name='loginclient'),
    path('resetclient/', views.Clientreset_password, name='resetclient'),
    # path('confirmresetclient/', ClientPasswordResetConfirmView.as_view(), name='confirmresetclient'),


    

]
