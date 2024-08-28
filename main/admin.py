from django.contrib import admin
from django.core.exceptions import ValidationError

from .models import ContactInfo, Lead, FAQ, Category, Work


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('phone1', 'phone2', 'email', 'address',
                    'working_hours', 'updated_at')
    ordering = ('-updated_at',)

    def save_model(self, request, obj, form, change):
        if not change and ContactInfo.objects.exists():
            raise ValidationError(
                "Можно создать только одну запись с контактной информацией.")
        super().save_model(request, obj, form, change)


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name',  'phone', 'created_at')
    search_fields = ('name', 'phone')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    search_fields = ('question',)
    ordering = ['question']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = ('name',)
    ordering = ['name']


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location',
                    'date_of_creation', 'image')
    list_filter = ('category',)
    search_fields = ('title', 'location', 'materials',
                     'advantages', 'for_decoration')
    ordering = ['title']
