from django import forms
from .models import Patient


class NewPatientForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                               choices=[('', '-- select --')] + list(Patient.GENDER_CHOICES), required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    history = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    occupation = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    medication = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Patient
        fields = '__all__'