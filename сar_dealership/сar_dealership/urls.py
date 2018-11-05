from django.contrib import admin
from django.urls import include, path


from showroom.urls import router


urlpatterns = [
    path('api/', include(router.urls)),
    path('showroom/', include('showroom.urls')),
    path('admin/', admin.site.urls),
]
