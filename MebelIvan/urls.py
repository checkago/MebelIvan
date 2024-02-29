from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
from django.urls import path

from mebel_app.views import IndexView, ProjectView, ProjectDetailView, AboutView, ContactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('project/', ProjectView.as_view(), name='project'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('about/', AboutView.as_view(), name='about-us'),
    path('contact/', ContactView.as_view(), name='contact'),
]

if settings.MEDIA_ROOT:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
