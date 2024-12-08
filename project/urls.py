"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app.views import AdminTemplateView,ProductListByCategory
from orders.views import all_orders_list

urlpatterns = [
    path('staff/orders/',all_orders_list, name="admin_all_orders"),
    path('staff/', AdminTemplateView.as_view(), name="admin-page"),
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('users/', include('users.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
   path('', ProductListByCategory.as_view(), name='main')
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
