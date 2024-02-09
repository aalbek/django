from django.urls import path
from .views import index_page
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index_page, name='index')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
