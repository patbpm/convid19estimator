from rest_framework import serializers

from .models import Region, Report

class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region
        fields = ('name', 'avAge',  'avDailyIncomeInUSD', 'avDailyIncomePopulation')

class ReportSerializer(serializers.HyperlinkedModelSerializer):
    
    region = RegionSerializer(required=True)

    class Meta:
        model = Report
        fields = ('region', 'periodType', 'timeToElpase','reportedCases','Population','totalHospitalBeds')