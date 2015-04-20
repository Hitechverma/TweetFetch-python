from django.conf.urls import patterns, include, url
from django.contrib import admin
from twitter.views import fetch #Importing VIEWs


urlpatterns = patterns('',
	# url(r'^admin/', include(admin.site.urls)),
    url(r'^fetch/', fetch),
)