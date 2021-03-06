from django.shortcuts import render
from .models import Patient

# Create your views here.
def patient_list(request):
	patients = Patient.objects.all().values('firstName', 'lastName', 'date_of_birth', 'primarycareprovider__firstName', 'primarycareprovider__lastName')
	return render(request, 'aggregate_health/patient_search_results.html', {'patients': patients, 'nbar': 'search_results'})

def dashboard(request):
	return render(request, 'aggregate_health/dashboard.html', {'nbar':'dash', 'tableloop': range(6)})

def alert_builder(request):
	return render(request, 'aggregate_health/alert_builder.html', {'nbar':'alert_builder'})