from django.urls import path
from . import views

app_name = "cards"
urlpatterns = [
    path('', views.home, name="home"),
    path('details/<str:ref_code>/', views.card_details, name="card-details"),
    path('create-card/', views.create_card, name="create-card"),
    path('update-card/<str:ref_code>/', views.update_card, name="update-card"),
    path('users/', views.users, name="users"),
]
