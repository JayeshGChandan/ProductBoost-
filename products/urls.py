from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('<int:product_id>', views.detail, name='detail'),
    path('<int:product_id>/upvote', views.upvote, name='upvote'),
    path('<int:product_id>/reply', views.reply, name='reply'),
    path('top/', views.top, name='top'),
]
