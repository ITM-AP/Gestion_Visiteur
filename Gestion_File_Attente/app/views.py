from django.shortcuts import render

# Create your views here.

def app_view(request):
    print(request.POST)
    return render(request, 'index.html')