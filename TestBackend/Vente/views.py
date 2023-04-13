from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Restaurant,Commentaire, Produit
# , Commentaire
from .serializers import VenteSerializer ,CommentaireSerializer,ProduitSerializer
# , RegisterSerializer
# CommentaireSerializer

class ListRestaurantView(ListAPIView):
    queryset= Restaurant.objects.all()
    serializer_class= VenteSerializer 

class CreateRestaurantView(CreateAPIView):
    queryset= Restaurant.objects.all()
    serializer_class= VenteSerializer 

class UpdateRestaurantView(UpdateAPIView):
    queryset= Restaurant.objects.all()
    serializer_class= VenteSerializer 

class DeleteRestaurantView(DestroyAPIView):
    queryset= Restaurant.objects.all()
    serializer_class= VenteSerializer 


class ListCommentaireView(ListAPIView):
    queryset= Commentaire.objects.all()
    serializer_class= CommentaireSerializer

class CreateCommentaireView(CreateAPIView):
    queryset= Commentaire.objects.all()
    serializer_class= CommentaireSerializer

class ListProduitView(ListAPIView):
    queryset= Produit.objects.all()
    serializer_class= ProduitSerializer

class CreateProduitView(CreateAPIView):
    queryset= Produit.objects.all()
    serializer_class= ProduitSerializer

class UpdateProduitView(UpdateAPIView): 
    queryset= Produit.objects.all()
    serializer_class= ProduitSerializer

class DeleteProduitView(DestroyAPIView):
    queryset= Produit.objects.all()
    serializer_class= ProduitSerializer 






from rest_framework import status
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .models import Restaurateur
from .serializers import RestaurateurSerializer


class DeleteRestaurateurView(DestroyAPIView):
    queryset = Restaurateur.objects.all()
    serializer_class = RestaurateurSerializer
    permission_classes = [IsAdminUser]



















# views.py
from django.utils.http import urlsafe_base64_encode
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, get_user_model
from django.utils.encoding import force_str
from django.contrib.auth.tokens import default_token_generator
from .serializers import RestaurateurSerializer, LoginSerializer, PasswordResetSerializer

UserModel = get_user_model()

class RestaurateurCreateAPIView(CreateAPIView):
    serializer_class = RestaurateurSerializer
    permission_classes = (AllowAny,)

class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        if not user:
            return Response({'username': ['Invalid username.']}, status=status.HTTP_400_BAD_REQUEST)
        response_data = {
            'id': user.id,
            'phone_number': user.phone_number,
            'email': user.email,
            'username': user.username
        }
        return Response(response_data)


class PasswordResetAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = PasswordResetSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data['phone_number']
        email = serializer.validated_data['email']
        user_queryset = UserModel.objects.filter(phone_number=phone_number, email=email)
        if not user_queryset.exists():
            return Response({'detail': 'Invalid phone number or email.'}, status=status.HTTP_400_BAD_REQUEST)

        user = user_queryset.first()
        uid = urlsafe_base64_encode(force_bytes(user.pk)).decode('utf-8')
        token = default_token_generator.make_token(user)
        reset_url = f"{request.get_host()}/api/auth/password_reset_confirm/{uid}/{token}"
        message = f"Hello {user.username},\n\nPlease reset your password by clicking on the link: {reset_url}\n\nBest regards,\nThe KapyGenius Team"

        send_mail(
            subject="Reset your password",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False
        )

        return Response({'detail': f'Password reset link has been sent to {email}.'}, status=status.HTTP_204_NO_CONTENT)


class PasswordResetConfirmAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = PasswordResetSerializer

    def post(self, request, uidb64, token):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = UserModel.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            new_password = serializer.validated_data['password']
            user.set_password(new_password)
            user.save()
            return Response({'detail': 'Your password has been reset.'}, status=status.HTTP_204_NO_CONTENT)

        return Response({'detail': 'Invalid reset link.'}, status=status.HTTP_400_BAD_REQUEST)

# views.py

from rest_framework import mixins, generics
from .models import Restaurateur
from .serializers import RestaurateurSerializer

class RestaurateurList(mixins.ListModelMixin,
                       generics.GenericAPIView):
    """
    Récupère une liste de tous les restaurateurs enregistrés
    """
    queryset = Restaurateur.objects.all()
    serializer_class = RestaurateurSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



# views.py










from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Client
from .serializers import ClientSerializer

@api_view(['POST'])
def Clientregister(request):
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        client = Client()
        client.register(
            serializer.validated_data['username'],
            serializer.validated_data['email'],
            request.data['password'],
            serializer.validated_data['phone_number']
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def Clientlogin(request):
    try:
        client = Client.objects.get(username=request.data['username'])
        if client.login(request.data['username'], request.data['password']):
            serializer = ClientSerializer(client)
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    except Client.DoesNotExist:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def Clientreset_password(request):
    new_password = Client().reset_password(request.data['username'])
    if new_password:
        return Response({'new_password': new_password})
    else:
        return Response({'error': 'Invalid username'}, status=status.HTTP_400_BAD_REQUES)