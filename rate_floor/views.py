from django.shortcuts import render
from .models import Rate_floor

# Create your views here.
def rate_floor(request):
    ogga = Rate_floor.objects.all()
    return render(request, 'rate_floor/Rate_floor.html',{'objects':ogga})