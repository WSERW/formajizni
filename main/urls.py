from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lead/', views.lead_form_view, name='lead_form'),
]
