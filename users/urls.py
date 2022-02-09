from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path('', views.CommonUserListView.as_view(), name='users_list'),
    path('current/', views.CommonUserDetailView.as_view(), name='current_user_common'),
    # path('<int:pk>/', views, name='patch_user'),
    # path('private/users/', views, name='private_users'),
    # path('private/users/<int:pk>/', views, name='private_current_user'),
]
