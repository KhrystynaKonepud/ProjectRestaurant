"""
URL configuration for ProjectRestaurant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from Restaurant.views import home
from Restaurant.views.reservation_views import ReservationView, ReservationListView
from Restaurant.views.menu_view import menu_view
from Restaurant.views.dish_detail_view import dish_detail_view
from Restaurant.views.beverage_detail_view import beverage_detail_view


urlpatterns = [
path('admin/', admin.site.urls),
    path('', home.home_view, name='home'),
    path('reservation/', ReservationView.as_view(), name='reservation'),
    path('reservation/list/', ReservationListView.as_view(), name='reservation_list'),
    path('menu/', menu_view, name='menu'),
    path('menu/<slug:category_slug>/', menu_view, name='menu_by_category'),
    path('dish/<slug:slug>/', dish_detail_view, name='dish_detail'),
    path('beverage/<slug:slug>/', beverage_detail_view, name='beverage_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)