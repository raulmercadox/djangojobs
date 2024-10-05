from django.urls import path
from .views import index, jobdetail

urlpatterns = [
    path('', index, name="home"),
    path('jobdetail/<int:pk>', jobdetail, name="detail")
]
