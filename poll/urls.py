from django.urls import path
from. import views


urlpatterns = [  
     path('', views.index),   
     path('blog/', views.blog, name='blog'), 
     path('search/', views.search, name='search'),
     path('create/', views.create, name='create'),   
     path('post/<id>/', views.post, name='post-detail'),     
     path('post/<id>/update/', views.update, name='post-update'),     
     path('post/<id>/delete/', views.delete, name='post-delete'),
]
    
