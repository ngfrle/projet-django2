
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **other_fields):
        if not email:
            raise ValueError("Email is required.")
        if not username:
            raise ValueError("Username is required.")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **other_fields):
        other_fields.setdefault('is_admin', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, password, **other_fields)

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='media', blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Etudiant(CustomUser):
    matricule = models.CharField(max_length=30, unique=True)
    is_etudiant = models.BooleanField(default=True)

class Administration(CustomUser):
    administration_status = models.BooleanField(default=True)




   




class Categorie(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
            return self.nom




class Doc(models.Model):
    nom = models.CharField(max_length=30, unique=True)
    auteur=models.CharField(max_length=30, unique=False, null=True)
    date_ajout = models.DateTimeField(auto_now=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    description = models.CharField(max_length=120)
    file = models.FileField(upload_to='media/', null=False)

    class Meta:
        ordering = ['date_ajout']
    def __str__(self):
            return self.nom






#






