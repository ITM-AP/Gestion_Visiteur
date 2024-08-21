from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Rdv
from .forms import RdvForm
from datetime import date
import json
# Create your views here.


def app_view(request):
    rdvs = Rdv.objects.all().order_by('date', 'time')
    return render(request, 'index.html', {'rdvs': rdvs})


def add_rdv(request):
    form = RdvForm()
    if request.method == 'POST':
        form = RdvForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_view')
    return redirect('app_view')


def delete_rdv(request):
    if request.method == 'POST':
        try:
            data = json.load(request)
            rdv_id = data.get('rdv_id')
            if rdv_id is not None:
                rdv = Rdv.objects.get(id=rdv_id)
                rdv.delete()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': 'Identifiant de rendez-vous manquant.'})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Erreur lors de la lecture des données JSON.'})
        except Rdv.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Le rendez-vous n\'existe pas.'})
    else:
        return JsonResponse({'success': False, 'error': 'La méthode HTTP doit être POST.'})


def afficheur_view(request):
    if request.method == 'GET':
        today = date.today()
        rdvs = Rdv.objects.all().filter(date=today).order_by('time')
        return render(request, 'afficheur.html', {'rdvs': rdvs})
