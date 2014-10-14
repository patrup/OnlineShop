from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    # url(r'^$', 'OnlineShop.views.home', name='home'),

    url(r'^shop/', include('shop.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
