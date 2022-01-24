from django.urls import path
from AddForm import views

urlpatterns = [
    path('pop/', views.CreateItem.as_view(), name='popup'),
    path('create/', views.CompanyCreate, name="create"),
    path('edit/', views.CompanyEdit, name="edit"),
]