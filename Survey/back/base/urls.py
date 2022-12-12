from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes, name='routes'),
    path('users/review/',views.NewReview, name='review'),
]