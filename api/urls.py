from django.urls import path

from api import views

urlpatterns = [
    path("api/apply", views.ApplySponsor.as_view()),
    path("api/sponsorlist", views.ListSponsor.as_view()),
    path("api/createsponsor", views.SponsorCreate.as_view()),
    path("api/updatesponsor", views.SponsorUpdate.as_view()),
    path("api/liststudent", views.ListStudent.as_view()),
    path("api/createstudent", views.StudentCreate.as_view()),
    path("api/updatestudent", views.StudentUpdate.as_view()),
    path("api/detailstudent", views.StudentDetail.as_view()),
]
