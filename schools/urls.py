from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'schools.views.home', name='home'),
    # url(r'^schools/', include('schools.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/list$', 'philly.views.list_schools'),

    url(r'^$', 'philly.views.index'),
)
