from django.shortcuts import render
from .models import Rate_angle

# Create your views here.
def rate_angle(request):
    ogga = Rate_angle.objects.all()
    return render(request, 'rate_angle/rate_angle.html',{'objects':ogga})
