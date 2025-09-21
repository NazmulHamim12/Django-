
from django.urls import path
from . import views
urlpatterns = [
   
    path('',views.home,name='home'),
    path('<int:m_id>',views.detail,name='detail'),
    path('about/',views.about,name='about'),
    path("login/",views.login, name="login"),
    path('login/<int:user_id>',views.profile,name='profile'),
    
    path("sing/",views.sing, name="sing"),
   
    
]