from django.urls import path
from . import views

urlpatterns = [
    path('list-pdfs/', views.list_pdfs, name='list_pdfs'),
    path('summarize-pdf/', views.summarize_pdf, name='summarize_pdf'),
]
