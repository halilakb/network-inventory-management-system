from django.urls import path
from dashboard import views as dashboard_views
from inventory import views as inventory_views
from authentication import views as auth_views
from logs import views as logs_views

urlpatterns = [
    path('dashboard/', dashboard_views.dashboard_view, name='dashboard'),
    path('inventory/', inventory_views.inventory_view, name='inventory'),
    path('auth/', auth_views.auth_view, name='authentication'),
    path('logs/', logs_views.logs_view, name='logs'),
]