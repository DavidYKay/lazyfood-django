from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from piston.resource import Resource
from api.views import ArbitraryDataHandler, TrayDataHandler, TrayRandomHandler

user_resource = Resource(handler=ArbitraryDataHandler)

tray_random_resource = Resource(handler=TrayRandomHandler)
tray_resource = Resource(handler=TrayDataHandler)

urlpatterns = patterns(
  '',

  # HTML
  url(r'^$', 'lazyfood.views.home', name='home'),
  # url(r'^lazyfood/', include('lazyfood.foo.urls')),

  # ADMIN
  url(r'^admin/', include(admin.site.urls)),

  # API
  url(r'^other/(?P<username>[^/]+)/(?P<data>.+)/$', user_resource),

  url(r'^api/tray/$', tray_random_resource, { 'emitter_format': 'json' }),
  #url(r'^api/tray/(?P<username>[^/]+)/$', tray_resource, { 'emitter_format': 'json' }),
  #url(r'^api/tray/(?P<tray_num>\w{1})/$', tray_resource, { 'emitter_format': 'json' }),

)
