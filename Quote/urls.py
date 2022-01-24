from Quote import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('Quote/', views.QuoteInputView, name='quote'),
    path('ajax/load-location/', views.load_location, name='ajax_load_location'),

    path('list_quote/', views.AddQuoteListView.as_view(), name='list_quote'),
    path('<int:id>/detail/', views.AddQuoteDetailView.as_view(), name='detail'),
    path('<int:id>/update/', views.AddQuoteUpdateView.as_view(), name='update_quote'),
    path('<int:id>/delete/', views.AddQuoteDeleteView.as_view(), name='delete_quote'),

    path('404/', views.errorPage, name='404'),
    path('login/', views.login, name='login'),

    path('create/', views.MultiRegionCreate, name="create"),
]