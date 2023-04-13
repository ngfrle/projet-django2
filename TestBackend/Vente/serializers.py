# import serializers from the REST framework
from rest_framework import serializers
 

from django.contrib.auth.models import User

from rest_framework import serializers, validators
from .models import Restaurant,Commentaire, Produit,Restaurateur



class VenteSerializer(serializers.ModelSerializer):
 
    # create a meta class
    class Meta:
        model = Restaurant
        fields = ('Titre','siege', 'Image','telephone','Email','description','restaurateur')

class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model= Commentaire
        fields = ('name2','email2','phone2','suject2','description2')

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model= Produit
        fields =('titre','prix','Restaurant','image','date_ajout')




# serializers.py

from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class RestaurateurSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True, validators=[validate_password])

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password', 'phone_number')

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=15, write_only=True)

class PasswordResetSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, write_only=True, validators=[validate_password])


# serializers.py

from rest_framework import serializers
from .models import Restaurateur


class RestaurateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurateur
        fields = ["id", "username", "email","password", "phone_number"]


# serializers.py

from rest_framework import serializers
from .models import Client


# class ClientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Client
#         fields = ["id", "username", "email", "phone_number", "password"]
#         extra_kwargs = {"password": {"write_only": True}}


from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'username', 'email', 'phone_number')