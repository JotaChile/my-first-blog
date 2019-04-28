from django.urls import path
from . import views
from . import views as core_views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<pk>/remove/', views.comment_remove, name='comment_remove'),
    path('signup/', core_views.signup, name='signup'),
    path('account_activation_sent/', core_views.account_activation_sent, name='account_activation_sent'),
    path('activate/<uidb64>[0-9A-Za-z_\-]+)/<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',core_views.activate, name='activate'),
]
