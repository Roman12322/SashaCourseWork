from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.signup),
    path('calcs', views.calcs),
    path('data', views.data),
    path('registration', views.Registration),
    path('calculate', views.Calculate),
    path('gettingDATA', views.getData)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)