from . import views
from django.urls import path

urlpatterns = [
    path('tables/', views.QuoteInputView2, name='tables'),
    path('list_quote/', views.AddQuoteListView.as_view(), name='list_quote'),
    path('<int:id>/detail/', views.AddQuoteDetailView.as_view(), name='detail'),
    path('<int:id>/update/', views.AddQuoteUpdateView.as_view(), name='update_quote'),
    path('<int:id>/delete/', views.AddQuoteDeleteView.as_view(), name='delete_quote'),

    path('404/', views.errorPage, name='404'),
    path('login/', views.login, name='login'),

    path('tables1/', views.table1, name='tables1'),
    path('tables2/', views.table2, name='tables2'),
]
