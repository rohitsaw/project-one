from django.urls import path

from . import views

app_name = "noteapp"

urlpatterns = [
    path("", views.index, name='index'),
    # path('login/', views.login, name='login'),
    # path('new_user/', views.new_user, name="new_user"),
    # path('login_check/', views.login_check, name="login_check"),
    # path('signup/', views.signup, name="signup"),
    path('storenote/', views.storenote, name="storenote"),
    path('removenote/', views.remove, name="removenote"),
    # path('logout/', views.logout, name="logout")
]
