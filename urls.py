#from django.conf.urls.defaults import *
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^SIAConcurseiros/', include('SIAConcurseiros.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    (r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),

    (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'templates/js'}),

    (r'^$', 'AppQuestoes.views.index'),

    (r'^TAI/$', 'AppQuestoes.views.listaQuestoesDoNivelDoUser'),
    (r'^corrige_TAI', 'AppQuestoes.views.corrigeTAI'),

    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url': '/login/'}),
    (r'^register/$', 'AppQuestoes.views.register'),
)

from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )


