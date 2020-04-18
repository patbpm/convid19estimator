from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .forms import ReportForm

from .serializers import RegionSerializer, ReportSerializer
from .models import Region, Report

# Create your views here.

def homepage(request):
    
    region = Region.objects.first()
    
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            
            report.save()
        
          
            report = Report.objects.create(
                
                periodType=form.get("periodType"),
                timeToElpase=form.get("timeToElpase"),
                reportedCases=form.get("reportedCases"),
                Population=form.get("population") ,
                totalHospitalBeds=form.get("totalHospitalBeds")
                
            )
            return redirect('homepage')  # TODO: redirect to the created topic page
    else:
        form = ReportForm()

    context = {
        'form': form
    } 
    
    return render(request, 'convidapp/templates/homepage.html', context)




class RegionReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
