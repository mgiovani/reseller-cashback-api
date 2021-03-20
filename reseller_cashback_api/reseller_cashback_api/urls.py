from django.contrib import admin
from django.urls import path

from apps.reseller import views as reseller_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reseller/', reseller_views.ResellerView.as_view(), name='reseller'),
    path('login/', reseller_views.ResellerLoginView.as_view(), name='login'),
]
