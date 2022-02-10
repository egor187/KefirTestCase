from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path('', views.CommonUserListView.as_view(), name='users_list'),
    path('current/', views.CommonUserDetailView.as_view(), name='current_user_common'),
    path('<int:pk>/', views.CommonUserUpdateView.as_view(), name='patch_user_common'),
    path('private/users/', views.AdminUserListView.as_view(), name='private_users_list'),
    # path('private/users/<int:pk>/', views, name='private_current_user'),
]
