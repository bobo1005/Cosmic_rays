from django.shortcuts import render
from .models import Contacts

# Create your views here.
def contacts(request):
    ogga = Contacts.objects.all()
    return render(request, 'contacts/Contacts.html',{'objects':ogga})