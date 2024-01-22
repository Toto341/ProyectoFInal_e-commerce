from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppEcommerce/', include('AppEcommerce.urls')),
    path('', include('AppEcommerce.urls'))
]
