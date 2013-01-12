from django.contrib import admin
from models import *

class TrayItemInline(admin.TabularInline):
    model = TrayItem

class TrayAdmin(admin.ModelAdmin):
  list_display = ['name', 'restaurant', 'user']
  inlines = [
      TrayItemInline,
  ]
  #class Meta:
admin.site.register(Tray, TrayAdmin)


class RestaurantAdmin(admin.ModelAdmin):
  list_display = ['name', 'restaurant_code', ]
admin.site.register(Restaurant, RestaurantAdmin)


class TrayItemAdmin(admin.ModelAdmin):
  list_display = ['name',
                  #'tray__restaurant',
                  'item_code',
                  ]
admin.site.register(TrayItem, TrayItemAdmin)

class OptionAdmin(admin.ModelAdmin):
  list_display = [
                  'name',
                  'tray_item',
                  'option_code',
                  ]
admin.site.register(Option, OptionAdmin)
