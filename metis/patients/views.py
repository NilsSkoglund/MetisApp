from django.shortcuts import render, redirect
from .forms import NewPatientForm
from .models import Patient
from django.http import JsonResponse
import openai
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to the home page!")

def index(request):
    if request.method == 'POST':
        form = NewPatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patients:index')
    patients = Patient.objects.all()
    form = NewPatientForm()
    context = {"form": form, "patients": patients}
    return render(request, "patients/index.html", context)


def delete_patient(request, patient_id):
    try:
        patient = Patient.objects.get(id=patient_id)
        patient.delete()
        return JsonResponse({"status": "success"})
    except Patient.DoesNotExist:
        return JsonResponse({"status": "failure", "error": "Patient not found"})

