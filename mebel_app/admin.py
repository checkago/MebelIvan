from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from mebel_app.models import Banner, About, Contact, Project, GalleryCategory, Gallery, Position, Employee, Social



class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position',)

# Register your models here.
admin.site.register(Banner)
admin.site.register(About)
admin.site.register(Position)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Contact)
admin.site.register(Project)
admin.site.register(GalleryCategory)
admin.site.register(Gallery)
admin.site.register(Social)

