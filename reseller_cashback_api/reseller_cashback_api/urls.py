from django.contrib import admin
from django.urls import path

from apps.reseller import views as reseller_views
from apps.order import views as order_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reseller/', reseller_views.ResellerView.as_view(), name='reseller'),
    path('login/', reseller_views.ResellerLoginView.as_view(), name='login'),
    path('order/<str:pk>/', order_views.OrderDetailView.as_view(), name='order-detail'),  # noqa
    path('order/', order_views.OrderView.as_view(), name='order'),
]
