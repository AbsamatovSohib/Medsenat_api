from django.urls import path
from api import views

urlpatterns = [
    path('api/apply',views.ApplySponsor.as_view()),
    path('api/sponsorlist', views.ListSponsor.as_view()),

    path('api/studentlist', views.ListStudent.as_view())
]