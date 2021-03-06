from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin

from todo.views import api_root

urlpatterns = patterns('',
    ## django admin interface
    url(r'^admin/', include(admin.site.urls)),

    ## drf api
    url('^api/$', api_root),
    url('^api/tasks/', include('task.urls')), # task API
    url(r'^api/token-auth/', 'rest_framework_jwt.views.obtain_jwt_token',
        name='token-auth'),
    url(r'^api/token-refresh/', 'rest_framework_jwt.views.refresh_jwt_token',
        name='token-refresh'),
    url(r'^api/token-verify/', 'rest_framework_jwt.views.verify_jwt_token',
        name='token-verify'),
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns(
            # serve angularjs root template
            'django.contrib.staticfiles.views',
            url(r'^', 'serve', kwargs={'path': 'index.html'}),
    )
