from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'comment.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^my_app/', include('my_app.urls', namespace='my_app')),
    url(r'^admin/', include(admin.site.urls)),
]
