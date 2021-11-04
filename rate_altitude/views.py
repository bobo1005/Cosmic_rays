from django.shortcuts import render
from .models import Rate_altitude

# Create your views here.
def rate_altitude(request):
    ogga = Rate_altitude.objects.all()
    return render(request, 'rate_altitude/Rate_altitude.html',{'objects':ogga})