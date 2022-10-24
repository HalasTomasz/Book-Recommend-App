from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes, name='routes'),

    path('books/',views.getBooks, name='books'),
    path('books/<str:pk>/',views.getBook, name='book'),

    path('users/data/<str:id>', views.getUser, name='user-data'),
    path('users/update/<str:id>', views.updateUser, name='user-update'),
    path('users/register/', views.registerUser, name='register')
]