from django.core.mail import BadHeaderError, EmailMessage
import json

from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import ContactForm


# Create your views here.
def index(request):
    return render(request, "TestTemplate/home.html", {})


def center(request):
    return render(request, "TestTemplate/centerPage.html", {})


def header(request):
    return render(request, "TestTemplate/header.html", {})


def contact(request):
    return render(request, "TestTemplate/contact.html", {})


def main(request):
    return render(request, "TestTemplate/main.html", {})


def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']

            content = form.cleaned_data['content']

            try:
                email = EmailMessage(contact_name,
                                     "\n[Email: " + contact_email + "]\n[Nome: " + contact_name + "]\n\n" + content,
                                     contact_email,
                                     ['41326@etu.he2b.be'],  # change to your email
                                     reply_to=[contact_email],
                                     # Construire le message avec le mail de la personne car le message s'envoi à
                                     # nous même pour questions de connexion.
                                     )
                email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('../thank_you/')
    return render(request, 'TestTemplate/email.html', {'form': form})


def thank_you(request):
    return render(request, 'TestTemplate/thank_you.html')


def footer(request):
    return render(request, "TestTemplate/footer.html", {})


def project(request):
    data = {
               "photos": ["/static/images/apartment-balcony-building-271689.jpg",
                          "/static/images/apartments-architecture-balcony-273683.jpg"],
               "name": "Casa de Leiria",
               "summary": "Filet mignon brisket "
           }, {
               "photos": ["", "", ""],
               "name": "Casa Cork",
               "summary": "Filet mignon brisket pancetta fatback short ribs short loin prosciutto jowl turducken biltong kevin pork chop pork beef ribs bresaola. Tongue beef ribs pastrami boudin. Chicken bresaola kielbasa strip steak biltong. Corned beef pork loin cow pig short ribs boudin bacon pork belly chicken andouille. Filet mignon flank turkey tongue. Turkey ball tip kielbasa pastrami flank tri-tip t-bone kevin landjaeger capicola tail fatback pork loin beef jerky "
           }, {
               "photos": ["", "", ""],
               "name": "Moveis Caneiro",
               "summary": "Filet mignon brisket pancetta fatback short ribs short loin prosciutto jowl turducken "
                          "biltong kevin pork chop pork beef ribs bresaola. Tongue beef ribs pastrami boudin. Chicken "
                          "bresaola kielbasa strip steak biltong. Corned beef pork loin cow pig short ribs boudin "
                          "bacon pork belly chicken andouille. Filet mignon flank turkey tongue. Turkey ball tip "
                          "kielbasa pastrami flank tri-tip t-bone kevin landjaeger capicola tail fatback pork loin "
                          "beef jerky "
           }, {
               "photos": ["", "", ""],
               "name": "Hotel de Lisboa",
               "summary": "Filet mignon brisket pancetta fatback short ribs short loin prosciutto jowl turducken biltong "
                          "kevin pork chop pork beef ribs bresaola. Tongue beef ribs pastrami boudin. Chicken bresaola "
                          "kielbasa strip steak biltong. Corned beef pork loin cow pig short ribs boudin bacon pork "
                          "belly chicken andouille. Filet mignon flank turkey tongue. Turkey ball tip kielbasa pastrami "
                          "flank tri-tip t-bone kevin landjaeger capicola tail fatback pork loin beef jerky "
           }, {
               "photos": ["", "", ""],
               "name": "Museu da Cultura",
               "summary": "Filet mignon brisket pancetta fatback short ribs short loin prosciutto jowl turducken biltong kevin pork chop pork beef ribs bresaola. Tongue beef ribs pastrami boudin. Chicken bresaola kielbasa strip steak biltong. Corned beef pork loin cow pig short ribs boudin bacon pork belly chicken andouille. Filet mignon flank turkey tongue. Turkey ball tip kielbasa pastrami flank tri-tip t-bone kevin landjaeger capicola tail fatback pork loin beef jerky "
           }, {
               "photos": ["", "", ""],
               "name": "Global Visao",
               "summary": "Filet mignon brisket pancetta fatback short ribs short loin prosciutto jowl turducken biltong kevin pork chop pork beef ribs bresaola. Tongue beef ribs pastrami boudin. Chicken bresaola kielbasa strip steak biltong. Corned beef pork loin cow pig short ribs boudin bacon pork belly chicken andouille. Filet mignon flank turkey tongue. Turkey ball tip kielbasa pastrami flank tri-tip t-bone kevin landjaeger capicola tail fatback pork loin beef jerky "
           }

    return render(request, "TestTemplate/project.html", {'data': json.dumps(data)})


def two_window(request):
    return render(request, "TestTemplate/two_window.html", {})


def projects_photos(request):
    return render(request, "TestTemplate/projects_photos.html", {})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')
