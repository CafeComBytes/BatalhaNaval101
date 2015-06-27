from django.conf.urls import include, url
from django.contrib import admin
from BatalhaNaval.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tabuleiro/$', exibir_tabuleiro),
    url(r'^tabuleiro/atacar$', atacar),
]
