from django.urls import path
from django.contrib.auth.views import PasswordChangeDoneView
from django.urls.conf import path, include
from . import views

app_name = "cards"
urlpatterns = [
    path('', views.home, name="home"),
    path('details/<str:ref_code>/', views.delete_card, name="card-delete"),
    path('card-link/<str:ref_code>/', views.card_link, name="card-link"),
    path('create-card/', views.create_card, name="create-card"),
    path('update-card/<str:ref_code>/', views.update_card, name="update-card"),
    path('password_change/done/', PasswordChangeDoneView.as_view())
]
