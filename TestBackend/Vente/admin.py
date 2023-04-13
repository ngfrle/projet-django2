from django.contrib import admin

# Register your models here.
from .models import Restaurant,Restaurateur, Produit,Commentaire,Commande,Client


admin.site.register(Restaurant)
admin.site.register(Commentaire)
admin.site.register(Produit)
admin.site.register(Commande)
admin.site.register(Restaurateur)
admin.site.register(Client)



