from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.conf import settings
from ordered_model.models import OrderedModel


class JWVideo(CMSPlugin):
	""" CMS Video Plugin for Embedding JWPLAYER """

	STRETCHING_MODES = (
		('uniforn', 'Uniform'),
		('none', 'None'),
		('fill', 'Fill'),
		('exactfit', 'ExactFit'),
	)

	PLAYER_MODES = (
		('html5', 'HTML5'),
		('flash', 'Flash'),
	)

	if settings.JWPLAYER_SCRIPT:
		jwplayer_script = settings.JWPLAYER_SCRIPT
	else:
		jwplayer_script = ''

	if settings.JWPLAYER_LICENSE:
		jwplayer_license = settings.JWPLAYER_LICENSE
	else:
		jwplayer_license = ''

	name = models.CharField(max_length=32, help_text='String to help identify player')
	jwplayer_script = models.URLField(default=jwplayer_script, help_text='URL to jwplayer JS file')
	jwplayer_license = models.CharField(max_length=100, blank=True, null=True, default=jwplayer_license, help_text='JWPlayer PRO and Premium license key')
	image = models.URLField(blank=True, null=True, help_text='(Optional) Placeholder image to start with.')
	final_frame = models.URLField(blank=True, null=True, help_text='(Optional) Placeholder image to end with.')
	skin = models.URLField(blank=True, null=True, help_text='(Optional) Url to script XML')
	controls = models.BooleanField(default=True, help_text='Whether to display controls')
	width = models.CharField(max_length=4, default='100%', blank=True, null=True, help_text='(Optional) Width, can be % or px')
	height = models.CharField(max_length=4, blank=True, null=True, help_text='(Optional) Height, can be % or px')
	aspect_ratio = models.CharField(max_length=10, blank=True, null=True, help_text='(Optional) Aspect ratio for responsive video in form of width:height, IE 16:9')
	reserve_height = models.IntegerField(blank=True, null=True, help_text='(Optional) If aspect ratio is set, you can reserve height to prevent flash.')
	autostart = models.BooleanField(default=False, help_text='Start video on load')
	stretching = models.CharField(max_length=10, choices=STRETCHING_MODES, default='uniform', help_text='See jwplayer documentation')
	primary = models.CharField(max_length=10, choices=PLAYER_MODES, default='html5', help_text='Which player type to use by default')
	repeat = models.BooleanField(default=False, help_text='Repeat video on end')

	def __unicode__(self):
		return u'%s' % (self.name)

	def copy_relations(self, old_instance):
		for source in old_instance.sources.all():
			# instance.pk = None; instance.pk.save() is the slightly odd but
			# standard Django way of copying a saved model instance
			source.pk = None
			source.video = self
			source.save()


class VideoSource(OrderedModel):
	""" URL to a video file for use in CMSVideoPlugin """

	video = models.ForeignKey(to=JWVideo, related_name="sources", null=True, blank=True)
	url = models.URLField()
	label = models.CharField(max_length=20, blank=True, null=True)
	default = models.BooleanField(default=False)
	media_type = models.CharField(max_length=10, blank=True, null=True)

	def __unicode__(self):
		return u'%s' % (self.url)