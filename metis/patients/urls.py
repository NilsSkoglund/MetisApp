from django.urls import path
from . import views

app_name = 'patients'
urlpatterns = [
    path("", views.index, name="index"),
    path("delete_patient/<int:patient_id>/", views.delete_patient),
]