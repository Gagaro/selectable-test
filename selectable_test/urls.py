from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from selectable_test.views import MyView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
     url(r'^$', MyView.as_view(), name='home'),
    # url(r'^selectable_test/', include('selectable_test.foo.urls')),

    (r'^selectable/', include('selectable.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
