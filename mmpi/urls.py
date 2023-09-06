from django.urls import path
from django.views.generic.base import TemplateView
from .views import *


app_name = 'mmpi'
urlpatterns = [
    path('', TemplateView.as_view(template_name='mmpi/main.html'), name='main'),
    path('male_test/', MaleTest.as_view(), name='male_test'),
    path('female_test/', FemaleTest.as_view(), name='female_test'),
    path('results/<pk>', Results.as_view(), name='results'),
    path('more', TemplateView.as_view(template_name='mmpi/more.html'), name='more')
]
