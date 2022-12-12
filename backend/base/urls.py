from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.getRoutes, name='routes'),

    path('books/',views.getBooks, name='books'),
    path('books/<str:pk>/',views.getBook, name='book'), 
    path('books/genre', views.getGenre, name='book_genre'),

    path('user/shortgenre', views.getShortGenre, name='user_short_genre'),
    path('user/update/genre/', views.updateUserGenre,  name='user_new_genre'),
   # path('user/genre/<str:id>', views.getUserGenre, name='user_genre'),

    path('user/history/<str:id>', views.getUserHistory, name='user-history'),
    path('user/set/history/', views.setUserHistory, name='set-user-history'),
    path('user/history/return/', views.returnBookUserHistory, name='return-user-history'),
    
    path('user/algo/<str:id>', views.getUserDataAlgo,  name='user_algo'),
    path('users/data/<str:id>', views.getUser, name='user-data'),
    path('users/update/<str:id>', views.updateUser, name='user-update'),
    path('users/register/', views.registerUser, name='register'),

    path('review/add/', views.addReview, name='review')
]