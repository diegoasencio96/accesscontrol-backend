from django.contrib import admin
from .models import DoorOpening
# Register your models here.

from suit.admin import RelatedFieldAdmin, get_related_field
from django.utils.safestring import mark_safe

class DoorOpeningAdmin(RelatedFieldAdmin):
    search_fields = ('date', 'time', 'user__first_name', 'user__last_name', 'user__id_card', 'user__id_card_rfid', 'user__entities__entity_name')
    list_filter = ('user__entities__entity_name', )
    list_display = ('user', 'image_tag', 'date', 'time', 'get_entities')
    list_select_related = True
    readonly_fields = ['image_tag']
    #inlines = (CityInline,)

    def get_entities(self, obj):
        return "\n".join([e.entity_name for e in obj.user.entities.all()])
    get_entities.short_description = 'Empresas'

    def image_tag(self, obj):
        return mark_safe('<img src="/media/%s" width="100" height="100" />' % (obj.user.profile_image))
    image_tag.short_description = 'Foto'
    image_tag.allow_tags = True



admin.site.register(DoorOpening, DoorOpeningAdmin)
