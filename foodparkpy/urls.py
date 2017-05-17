from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


from main import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'foodparkpy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('main.urls')),
    url(r'^foodparkpy/main/', include('main.urls')),
    url(r'^admin/', include(admin.site.urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
