from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from upload.views import image_upload
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("upload/", image_upload, name="upload"),
    
    # re_path("", TemplateView.as_view(template_name="index.html"),  name=""),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)