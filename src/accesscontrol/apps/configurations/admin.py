from django.contrib import admin


# Register your models here.

from .models import General, Entity
from suit.admin import RelatedFieldAdmin, get_related_field
from django.utils.html import format_html

class GeneralAdmin(RelatedFieldAdmin):
    search_fields = ('site_name',)
    list_display = ('site_name', 'image_tag', 'with_image', 'height_image')
    list_select_related = True
    readonly_fields = ['image_tag']
    #inlines = (CityInline,)

    def image_tag(self, obj):
        image = format_html("<img src={url} height={h} width={w}>", url='/media/'+str(obj.site_image), w=obj.with_image, h=obj.height_image)
        return image
    image_tag.short_description = 'Logo'
    image_tag.allow_tags = True


class EntityAdmin(RelatedFieldAdmin):
    search_fields = ('entity_name',)
    list_display = ('entity_name', 'image_tag',)
    list_select_related = True
    readonly_fields = ['image_tag']
    #inlines = (CityInline,)

    def image_tag(self, obj):
        image = format_html("<img src={url} height={h} width={w}>", url='/media/'+str(obj.entity_image), w=100, h=80)
        return image
    image_tag.short_description = 'Logo'
    image_tag.allow_tags = True

admin.site.register(General , GeneralAdmin)
admin.site.register(Entity, EntityAdmin)

