from django.conf.urls import url
from django.urls import path
from django.urls import include

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^salas/$', views.SalaListView.as_view(), name='salas'),
	url(r'^sala/(?P<pk>\d+)$', views.SalaDetailView.as_view(), name='sala_detail'),
]
#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]