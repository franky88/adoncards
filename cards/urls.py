from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

handler400 = 'cardadds.views.handler400'
handler403 = 'cardadds.views.handler403'
handler404 = 'cardadds.views.handler404'
handler500 = 'cardadds.views.handler500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cardadds.urls')),
    path('christmas-cards/', include('xmaspops.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
