from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    # path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('edit/', views.edit, name='edit')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
