from django.shortcuts import render

# Create your views here.
def experimental(request):
    return render(request, 'experimental/Experimental.html')