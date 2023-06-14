from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.views import PasswordResetView

@login_required
def home(request):
    return render(request, 'accueil.html')


@login_required
def fichier(request):
    return render(request, 'fichier.html')
    

@login_required   
def admin(request):
    return render(request, 'admin.html')


from django.shortcuts import render, redirect
from .form import EtudiantCreationForm, AdministrationCreationForm

def register1(request):
    if request.method == 'POST':
        form = EtudiantCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Rediriger vers l'interface appropriée
            return redirect('login')
    else:
        form = EtudiantCreationForm()
    return render(request, 'register.html', {'form': form})

def register2(request):
    if request.method == 'POST':
        form = AdministrationCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Rediriger vers l'interface appropriée
            return redirect('login')
    else:
        form = AdministrationCreationForm()
    return render(request, 'prof_register.html', {'form': form})

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .form import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                if hasattr(user, 'etudiant'):
                    return redirect('home')
                elif hasattr(user, 'administration'):
                    return redirect('add_file')
            else:
                form.add_error(None, 'Invalid email or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect
# from .form import LoginForm

# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('success')
#             else:
#                 form.add_error(None, 'Invalid email or password')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})



# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect
# from .form import LoginForm
# from .models import Etudiant, Administration

# def login_view(request):
#     form = LoginForm()
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']

#             # Authentifier l'utilisateur
#             user = authenticate(request, email=email, password=password)

#             if user is not None:
#                 login(request, user)
#                 # Connecter l'utilisateur et rediriger vers la page d'accueil
#                 if isinstance(user, Etudiant):
#                     return redirect('home')
#                 elif isinstance(user, Administration):
#                     return redirect('add_file')
#     return render(request, 'login.html', {'form': form})

# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect
# from .models import Etudiant, Administration


# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         # Authentifier l'utilisateur
#         user = authenticate(request, email=email, password=password)

#         if user is not None:
#             login(request, user)
#             print("Utilisateur connecté avec succès")
#             # Connecter l'utilisateur et rediriger vers la page d'accueil
#             if isinstance(user, Etudiant):
#                 # L'utilisateur est une instance de la classe Etudiant
#                 if user.is_etudiant:
#                     print("Utilisateur est un etudiant")  
#                     return redirect('home')
#             elif isinstance(user, Administration):
#                 if user.administration_status:
#                     print("Utilisateur est un etudiant")  
#                     return redirect('add_file')
    
#     return render(request, 'login.html')






# from Gesco.models import Etudiant,Administration
# from django.contrib.auth import authenticate, login
# from django.shortcuts import redirect, render
# from .models import CustomUser


# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             print("User logged in successfully")
#             # Rediriger vers l'interface appropriée
#             if isinstance(user, Etudiant):
#                 print("User is an instance of Etudiant")
#                 return redirect('home')
#             elif isinstance(user, Administration):
#                 print("User is an instance of Administration")
#                 return redirect('add_file')
#     return render(request, 'login.html')


from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

def password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        User = get_user_model()
        user = User.objects.filter(email=email).first()
        if user:
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            current_site = get_current_site(request)
            site_name = current_site.name
            domain = current_site.domain
            subject = f"Réinitialisation du mot de passe sur {site_name}"
            message = render_to_string('update_password.html', {
                'domain': domain,
                'site_name': site_name,
                'uid': uid,
                'token': token,
                'protocol': 'https',
            })
            send_mail(subject, message, None, [email])
            return redirect('password_reset_done')
    return render(request, 'update_password.html')

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login/')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Doc
from .form import DocForm

def add(request):
    if request.method == 'POST':
        form = DocForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('doc_list')
    else:
        form = DocForm()
    return render(request, 'add.html', {'form': form})









def doc_list(request):
    docs = Doc.objects.all()
    return render(request, 'doc_list.html', {'docs': docs})

def doc_detail(request, pk):
    doc = get_object_or_404(Doc, pk=pk)
    return render(request, 'doc_detail.html', {'doc': doc})



def update(request, pk):
    doc = get_object_or_404(Doc, pk=pk)
    form = DocForm(request.POST or None, request.FILES or None, instance=doc)
    if form.is_valid():
        form.save()
        return redirect('doc_detail', pk=doc.pk)
    return render(request, 'update.html', {'form': form})

def delete(request, pk):
    doc = get_object_or_404(Doc, pk=pk)
    if request.method == 'POST':
        doc.delete()
        return redirect('doc_list')
    return render(request, 'doc_confirm_delete.html', {'doc': doc})


from django.db.models import Q

def search_docs(nom="", auteur="", categorie=""):
    query = Q()
    if nom:
        query &= Q(nom__icontains=nom)
    if auteur:
        query &= Q(auteur__icontains=auteur)
    if categorie:
        query &= Q(categorie__nom__icontains=categorie)

    docs = Doc.objects.filter(query).order_by('-date_ajout')
    return docs

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.conf import settings
import os

from .models import Doc

def download_file(request, doc_id):
    doc = get_object_or_404(Doc, id=doc_id)
    file_path = os.path.join(settings.MEDIA_ROOT, doc.file.name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response        
    raise Http404