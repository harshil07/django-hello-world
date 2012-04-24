from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangosite.views.home', name='home'),
    # url(r'^djangosite/', include('djangosite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'scheduler.views.index'),
    url(r'^student/$', 'scheduler.views.student'),
    url(r'^student/(?P<student_id>\d+)/$', 'scheduler.views.student_detail'),
    url(r'^teacher/$', 'scheduler.views.teacher'),
    url(r'^teacher/(?P<teacher_id>\d+)/$', 'scheduler.views.teacher_detail'),
    url(r'^course/$', 'scheduler.views.course'),
    url(r'^course/(?P<course_id>\d+)/$', 'scheduler.views.course_detail'),
)
