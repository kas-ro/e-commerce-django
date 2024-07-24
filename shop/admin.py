from django.contrib import admin
from django.utils.html import format_html

from shop.models.category import Category
from shop.models.image import ImageProduct
from shop.models.product import Product
from shop.models.slider import Slider
from shop.models.collection import Collection

class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'display_image')
    list_display_links = ('title', )

    def display_image(self, obj):
        return format_html(f'<img src="{ obj.image.url }" width="100"/>')
    
    display_image.short_description = 'image'
    

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'display_image')
    list_display_links = ('title', )

    def display_image(self, obj):
        return format_html(f'<img src="{ obj.image.url }" width="100"/>')
    
    display_image.short_description = 'image'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'display_image')
    list_display_links = ('name', )
    exclude = ('slug', )

    def display_image(self, obj):
        return format_html(f'<img src="{ obj.image.url }" width="100"/>')
    
    display_image.short_description = 'image'


class ImageInline(admin.TabularInline):
    model = ImageProduct
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = (
        'id', 'name', 'solde_price', 'regular_price', 'is_availlable',
        'is_best_seller', 'is_new_arrival', 'is_featured', 'is_specail_offer',
        'is_mega', 'display_image',
    )
    list_editable = (
        'is_availlable', 'is_best_seller', 'is_new_arrival', 
        'is_featured', 'is_specail_offer','is_mega',
    )
    list_display_links = ('name', )
    exclude = ('slug', )

    def display_image(self, obj):
        first_image = obj.images.first()
        if not first_image:
            return ''
        return format_html(f'<img src="{ first_image.image.url }" width="100"/>')
    
    display_image.short_description = 'image'
    
admin.site.register(Slider, SliderAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
