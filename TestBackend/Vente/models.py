from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager



# Create your models here.


class Restaurateur(AbstractUser):
    username = models.CharField(max_length=30, unique=True) 
    email = models.EmailField()
    password = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=20)

    def __str__(self):

        return self.username

       


from django.db import models

class Restaurant(models.Model):
    Titre = models.CharField(max_length=100)
    siege = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='restaurants/')
    telephone = models.CharField(max_length=20)
    Email = models.EmailField()
    description = models.CharField(max_length=100)
    restaurateur = models.ForeignKey(Restaurateur, on_delete=models.CASCADE)

    def __str__(self):
        return self.Titre


class Produit(models.Model): 
    titre = models.CharField(max_length=200)
    prix = models.FloatField()
    description = models.TextField()
    Restaurant = models.ForeignKey(Restaurant, related_name='restaurant',on_delete = models.CASCADE )
    image = models.ImageField(upload_to='media' , blank=True)
    date_ajout =models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-date_ajout']
        
    def __str__(self):
        return self.titre

class Commentaire(models.Model):
    name2 = models.CharField(max_length=30)
    email2 = models.EmailField(blank=True)
    phone2 = models.CharField(max_length=20)
    suject2 = models.CharField(max_length=50)
    description2 = models.TextField(default='votre probleme')

    def __str__(self):
        return f'Commentaire: (self.email2) (self.suject2)'

class Commande(models.Model):
    total =models.CharField(max_length=300)
    nom = models.CharField(max_length=300)
    email = models.EmailField()
    addresse= models.CharField(max_length=300)
    ville = models.CharField(max_length=300)
    pays = models.CharField(max_length=300)
    zipcode= models.CharField(max_length=300)
    date_commande = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_commande']
    
    def __str__(self):
        return self.nom 


from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.contrib.auth.hashers import make_password
import random
import string

class Client(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.username

    def register(self, username, email, password, phone_number):
        self.username = username
        self.email = email
        self.password = make_password(password)
        self.phone_number = phone_number
        self.save()

    def login(self, username, password):
        try:
            user = Client.objects.get(username=username)
            if user.check_password(password):
                return True
            else:
                return False
        except Client.DoesNotExist:
            return False

    def reset_password(self, username):
        try:
            user = Client.objects.get(username=username)
            new_password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            user.password = make_password(new_password)
            user.save()
            return new_password
        except Client.DoesNotExist:
            return None