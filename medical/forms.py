from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['district'].queryset = District.objects.none()

        if 'province' in self.data:
            try:
                province_id = int(self.data.get('province'))

                self.fields['district'].queryset = District.objects.filter(provice_id=province_id).order_by('district')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['district'].queryset = self.instance.province.district_set.order_by('district')


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['p_district'].queryset = District.objects.none()
        # self.fields['p_municipality'].queryset = District.objects.none()
        # self.fields['p_ward_no'].queryset = District.objects.none()
        # self.fields['t_district'].queryset = District.objects.none()
        # self.fields['t_municipality'].queryset = District.objects.none()
        # self.fields['t_ward_no'].queryset = District.objects.none()

        if 'municipality' in self.data:
            try:
                province_id = int(self.data.get('municipality'))

                self.fields['p_ward_no'].queryset = Ward.objects.filter(ward_no_id=province_id).order_by('ward_no')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['p_district'].queryset = self.instance.province.district_set.order_by('district')

