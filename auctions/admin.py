from django.contrib import admin
from .models import *

class ListingAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('title', 'category', 'user', 'date','price', 'active')
    actions = ['activate_listings', 'deactivate_listings']
    filter_horizontal = ("watchlist",)
    
    def activate_listings(self, request, queryset):
        queryset.update(active=True)
    
    def deactivate_listings(self, request, queryset):
        queryset.update(active=False)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'post', 'created_on')

class BidAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'price')

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Category)