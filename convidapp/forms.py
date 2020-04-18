from django import forms
from .models import Report

class ReportForm(forms.ModelForm):

    class Meta:
        model = Report
        fields = ('region', 'periodType','timeToElpase', 'reportedCases', 'Population', 'totalHospitalBeds')