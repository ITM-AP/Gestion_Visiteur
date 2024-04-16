from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Rdv
from .forms import RdvForm
from datetime import date
import json
# Create your views here.

def app_view(request):
    if request.method == 'GET':
        today = date.today()
        rdvs = Rdv.objects.all().order_by('time').order_by('date')
        form = RdvForm()
        return render(request, 'index.html', {'rdvs': rdvs})
    elif request.method == 'POST':
        form = RdvForm(request.POST)
        form.save()
        if form.is_valid():
            return redirect('app_view')

@csrf_exempt  
def delete_rdv(request):
    if request.method == 'POST':
        data = json.load(request)
        rdv_id = data.get('rdv_id')
        try:
            rdv = Rdv.objects.get(id=rdv_id)
            rdv.delete()
            return JsonResponse({'succes': True})
        except Rdv.DoesNotExist:
            return JsonResponse({'succes': False, 'error': 'Le rendez-vous n\'existe pas.'})

def afficheur_view(request):
    if request.method == 'GET':
        today = date.today()
        rdvs = Rdv.objects.all().filter(date=today).order_by('time')
        form = RdvForm()
        return render(request, 'afficheur.html', {'rdvs': rdvs})