from django.contrib import admin

# Register your models here.


from Gesco.models import Administration,Doc,Etudiant,Categorie
admin.site.register(Administration)
admin.site.register(Doc)
admin.site.register(Etudiant)
admin.site.register(Categorie)

