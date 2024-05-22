from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe



class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'cuisine', 'price', 'get_image', )

    def get_image(self, menu):
        if menu.image:
            return mark_safe(f"<img src='{menu.image.url}' width='75px' style='border-radius:15px' />")

class CuisineAdmin(admin.ModelAdmin):
    list_display = ('name',)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name','get_image',)

    def get_image(self, menu):
        if menu.image:
            return mark_safe(f"<img src='{menu.image.url}' width='75px' style='border-radius:15px' />")

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','dish',)

    


admin.site.register(models.User)
admin.site.register(models.AboutUs)
admin.site.register(models.MenuCuisine, CuisineAdmin)
admin.site.register(models.MenuItem, MenuAdmin)
admin.site.register(models.TeamMember, TeamAdmin)
admin.site.register(models.Contact, CuisineAdmin)
admin.site.register(models.ClientReview, TeamAdmin)
admin.site.register(models.Service, TeamAdmin)
admin.site.register(models.Cart, OrderAdmin)
admin.site.register(models.Order)

