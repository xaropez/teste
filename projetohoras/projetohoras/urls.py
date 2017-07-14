"""
Definition of urls for projetohoras.
"""

from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', projetohoras.views.home, name='home'),
    # url(r'^projetohoras/', include('projetohoras.projetohoras.urls')),

    url(r'^va_hora/', include('va_hora.urls')), #use o va_hora app e use o va_hora.url

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]
