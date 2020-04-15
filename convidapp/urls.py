from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'v1/on-covid-19', views.RegionReportViewSet)

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
]