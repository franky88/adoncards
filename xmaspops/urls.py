from django.urls import path
from . import views

app_name = 'popups'
urlpatterns = [
    path('', views.home, name="home"),
    path('add-card/', views.create_card, name="add"),
    path('details/<str:ref_code>', views.card_details, name="details"),
    path('delete/<str:ref_code>', views.delete_card, name="delete"),
    path('card-preview/<str:ref_code>', views.card_preview, name="preview"),
]
