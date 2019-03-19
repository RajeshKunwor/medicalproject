from django import forms
from .models import *
import re
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DoctorScheduleForm(forms.ModelForm):
    class Meta:
        model = DoctorSchedule
        fields=["date","time","shift","max_patient"]


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        exclude=['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def clean_mobile_no(self):
        # super().clean()
        data = self.cleaned_data.get('mobile_no','')


        rule = re.compile(r'^98(\d{8})$|^97(\d{8})$')

        if not re.match(rule, data):
            raise forms.ValidationError("Invalid mobile number.")
        return self.cleaned_data.get('mobile_no','')


    # def clean_phone_no(self):
    #
    #     data = self.cleaned_data.get('phone_no','')
    #     # if data == '':
    #     #     raise forms.ValidationError("Phone number is empty.")
    #
    #     if len(data)!=9:
    #         raise forms.ValidationError("Invalid phone number.")
    #     return self.cleaned_data.get('phone_no','')


        # self.fields['p_district'].queryset = District.objects.none()
        # self.fields['p_municipality'].queryset = District.objects.none()
        # self.fields['p_ward_no'].queryset = District.objects.none()
        # self.fields['t_district'].queryset = District.objects.none()
        # self.fields['t_municipality'].queryset = District.objects.none()
        # self.fields['t_ward_no'].queryset = District.objects.none()
        #
        # if 'municipality' in self.data:
        #     try:
        #         province_id = int(self.data.get('municipality'))
        #
        #         self.fields['p_ward_no'].queryset = Ward.objects.filter(ward_no_id=province_id).order_by('ward_no')
        #     except (ValueError, TypeError):
        #         pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif self.instance.pk:
        #     self.fields['p_district'].queryset = self.instance.province.district_set.order_by('district')

