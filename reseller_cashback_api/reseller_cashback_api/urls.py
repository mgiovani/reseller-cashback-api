from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from apps.reseller import views as reseller_views
from apps.order import views as order_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reseller/', reseller_views.ResellerView.as_view(), name='reseller'),
    path('order/<str:pk>/', order_views.OrderDetailView.as_view(), name='order-detail'),  # noqa
    path('order/', order_views.OrderView.as_view(), name='order'),
    path('accumulated-cashback/', order_views.AccumulatedCashbackView.as_view(), name='accumulated-cashback'),  # noqa
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='login'),
    path('token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token-refresh'),  # noqa
]
