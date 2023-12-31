from django.shortcuts import render , get_object_or_404, redirect
from .models import Cours, Evenement, Sujet
from .forms import MessageForm
from django.core.mail import send_mail
########################################################## COURS#######################################

## Ce code permet d'afficher la page d'acceuil principale
def index(request):
  return render (request, "Acceuil1.html")

## Ce code permet d'afficher la page d'acceuil  des cours
def index_cours(request): 
  return render (request, "Acceuil2.html") 



## Ce code permet de lister tous les cours de premiere année
def index_cours_L1(request):
  liste_cours1 = Cours.objects.filter(Niveau_concerné__contains = "option1")
  context ={"liste_cours1": liste_cours1}
  return render (request, "Acceuil_L1.html", context) 


  ## Ce code permet de lister tous les cours de deuxieme année
def index_cours_L2(request):
  liste_cours2= Cours.objects.filter(Niveau_concerné__contains = "option2")
  context ={"liste_cours2": liste_cours2}
  return render (request, "Acceuil_L2.html", context) 



  ## Ce code permet de lister tous les cours de troisieme année
def index_cours_L3(request):
  liste_cours3= Cours.objects.filter(Niveau_concerné = "option3")
  context ={"liste_cours3": liste_cours3}
  return render (request, "Acceuil_L3.html", context) 



########################################################  EVENEMENT ############################################################


## Ce code permet de lister tous les évènements qui ont été publié.
def index_evenement(request):
  liste_evenement= Evenement.objects.all()
  context ={"liste_evenement": liste_evenement}
  return render (request, "Evenement.html", context) 


 
## Ce code permet de compter les personnes qui ont déja consulter le cours.
 
def nombre_consultation ( request, Cours_id) :
    cours =get_object_or_404(cours, pk=Cours_id)
    cours.Consultation +=1
    cours.save()
    return render(request,"Acceuil.html", {'cours': cours})





####################################################  SUJET ##################################################

def Sujet(request):
  return render (request, "Sujet.html")   

def index_sujet_sel(request):
  liste_sujet_sel = Sujet.objects.filter(Type_test= 'option1')
  context={"liste_sujet_sel": liste_sujet_sel}
  return render (request,"Sujet_selection.html",context)


def index_sujet_pres(request):
  liste_sujet_pres = Sujet.objects.filter(Type_test= 'option2')
  context={"liste_sujet_pres" : liste_sujet_pres}
  return render (request,"Sujet_preselection.html",context)



################################################### INFORMATION ########################################

def index_information(request):
  return render (request, "Information.html")  

def index_information_fil(request):
  return render (request, "Information_filiere.html")  

def index_information_site(request):
  return render (request, "Information_site.html")  

################################################### Formulaire message #######################"


  

def formulaire_message(request):
  if request.method == 'POST':
    form = MessageForm(request.POST)
    if form.is_valid():
         form.save()
         sujet = form.cleaned_data['sujet']
         message = form.cleaned_data['message']
         nom = form.cleaned_data['nom']
         prenom = form.cleaned_data['prenom']
         email = form.cleaned_data['email']
         destinataires = ['abdoulfaicalouedraogo120@gmail.com', 'judicaelkafando1704@gmail.com']
         send_mail(sujet, message, email,  destinataires, fail_silently=False)
    return redirect('confirmation_envoi')

  else :
    form = MessageForm()

  return render(request, 'message.html', {'form': form})


def formulaire_fond(request):
  fond_image=BackgroundImage.objects.first()
  context={"fond_image":fond_image}
  return render (request,'Acceuil1.html',context)
def AcceuilP(request):

  return render(request,"AcceuilP.html")