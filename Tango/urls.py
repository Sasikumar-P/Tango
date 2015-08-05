from django.conf.urls import patterns, url,include
from rango import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project_17.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('rango.urls')), # ADD THIS NEW TUPLE!
)

