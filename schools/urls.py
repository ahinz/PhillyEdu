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
    url(r'^api/search$', 'philly.views.search_schools'),

    url(r'^$', 'philly.views.index'),
    url(r'^school/(?P<school_id>\d+)$', 'philly.views.school_info'),

    url(r'^schools$', 'philly.views.schools'),

    url(r'^js/search.js$','philly.views.search_js'),
)
