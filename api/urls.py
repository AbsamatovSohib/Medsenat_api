from django.urls import path
from api import views

urlpatterns = [
    path('apply',views.ApplySponsor.as_view())
]