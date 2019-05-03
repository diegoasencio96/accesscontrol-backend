from suit.admin import RelatedFieldAdmin, get_related_field
from django.utils.safestring import mark_safe

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

admin.site.register(User, UserAdmin)



class ProfileAdmin(RelatedFieldAdmin):
    search_fields = ('first_name', 'last_name', 'user__username', 'id_card', 'id_card_rfid', 'entities__entity_name')
    list_filter = ('user__is_staff', 'user__is_active', 'user__is_superuser', 'entities__entity_name')
    list_display = ('image_tag', 'first_name', 'last_name', 'id_card', 'id_card_rfid', 'get_entities')
    list_select_related = True
    readonly_fields = ['image_tag']
    #inlines = (CityInline,)

    def get_entities(self, obj):
        return "\n".join([e.entity_name for e in obj.entities.all()])
    get_entities.short_description = 'Empresas'

    def image_tag(self, obj):
        return mark_safe('<img src="/media/%s" width="100" height="100" />' % (obj.profile_image))
    image_tag.short_description = 'Foto'
    image_tag.allow_tags = True

admin.site.register(Profile, ProfileAdmin)
