from django.contrib import admin
from django.urls import path,re_path
from app1 import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    # re_path(r'^',include('app1.urls'))
    re_path(r'^$',views.home,name='home'),
    re_path(r'^details', views.details, name='details'),
    re_path(r'^report',views.report,name='report'),
]