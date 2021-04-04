from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("closed_listings", views.closed_listings, name='closed_listings'),
    path("accounts/login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("create_listing/", views.create_listing, name="create_listing"),
    path("submit_listing/", views.submit_listing, name="submit_listing"),
    path("listings/<int:listing_id>/", views.listing_page, name="listing_page"),
    path("categories/", views.select_categories, name="select_categories"),
    path("categories/<str:category>/", views.category, name="category"),
    path("close_listing/", views.close_listing, name="close_listing"),
    path("listings/<int:listing_id>/place_bid/", views.place_bid, name='place_bid'),
    path("watchlist/", views.watchlist, name="watchlist"),
    path("add_to_watchlist/", views.add_to_watchlist, name="add_to_watchlist"),
    path("remove_from_watchlist/", views.remove_from_watchlist, name="remove_from_watchlist"),
    
] 

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
