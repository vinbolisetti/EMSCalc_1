from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.QuoteInputView, name='addquote'),
    # path('add1/', views.HostingView),
    # path('<int:pk>/', views.hosting_update_view),
    path('ajax/load-location/', views.load_location, name='ajax_load_location'),
]