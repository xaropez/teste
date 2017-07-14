from django.conf.urls import include, url
from va_hora import views

urlpatterns = [

    url(r'^$', views.va_hora, name='va_hora'),

]