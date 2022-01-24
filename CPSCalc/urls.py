from . import views
from django.urls import path

urlpatterns = [
    path('drp/', views.DRCostView, name='drcost'),
    path('cpsc/', views.CPSCostView, name='cpscost'),
    path('summary/', views.CPSSummaryView.as_view(), name='summary'),
]