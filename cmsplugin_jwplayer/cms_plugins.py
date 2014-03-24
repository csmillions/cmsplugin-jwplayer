from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import JWVideo
from .admin import VideoSourceInline

@plugin_pool.register_plugin
class JWVideoPlugin(CMSPluginBase):
    """ Create JW Player """

    model = JWVideo
    name = _("JWPlayer Video")
    render_template = "plugins/jwvideo/video.html"
    text_enabled = True

    fieldsets = [
        (None, {
            'fields': ['name', 'controls', ('autostart', 'repeat'),]
            }),
        (_('Dimensions'), {
            'fields': [('width', 'height'), ('use_aspect_ratio', 'aspect_ratio'), ('use_reserve_height', 'reserve_height')],
            }),
        (_('Advanced Display Options'), {
            'fields': [('image', 'final_frame'), 'skin', 'primary'],
            'classes': ('collapse',),
            }),
        
        (_('Advanced JW Player Options'), {
            'fields': ['jwplayer_script', 'jwplayer_license'],
            'classes': ('collapse',),
            }),
    ]
    inlines = (VideoSourceInline,)

    def render(self, context, instance, placeholder):

        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context
