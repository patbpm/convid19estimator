from django.shortcuts import render
from rest_framework import viewsets

from .serializers import RegionSerializer, ReportSerializer
from .models import Region, Report

# Create your views here.

def homepage(request):
    
    context = {
        
    } 
    
    return render(request, 'convidapp/templates/homepage.html', context)




class RegionReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
