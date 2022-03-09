from django.contrib import admin
from .models import Award

# Register your models here.

class AwardAdmin(admin.ModelAdmin):
    list_display=['description','photo']

admin.site.register(Award,AwardAdmin)

admin.site.site_header = '企业门户网站后台管理系统'
admin.site.site_title = '企业门户网站后台管理系统'