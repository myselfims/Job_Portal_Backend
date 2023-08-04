from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('getjob',views.JobViewSet)


urlpatterns = [
    path('',views.home),
    path('api',include(router.urls))
]
