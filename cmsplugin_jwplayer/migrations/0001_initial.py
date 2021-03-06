# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'JWVideo'
        db.create_table(u'cmsplugin_jwplayer_jwvideo', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('jwplayer_script', self.gf('django.db.models.fields.URLField')(default='/static/js/jwplayer/jwplayer.js', max_length=200)),
            ('jwplayer_license', self.gf('django.db.models.fields.CharField')(default='cWaauZOldSHd2qpqjoecJ6k3DAFsnZP1X0EKCw==', max_length=100, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('final_frame', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('skin', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('controls', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('width', self.gf('django.db.models.fields.CharField')(default='100%', max_length=4, null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('aspect_ratio', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('reserve_height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('autostart', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('stretching', self.gf('django.db.models.fields.CharField')(default='uniform', max_length=10)),
            ('primary', self.gf('django.db.models.fields.CharField')(default='html5', max_length=10)),
            ('repeat', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'cmsplugin_jwplayer', ['JWVideo'])

        # Adding model 'VideoSource'
        db.create_table(u'cmsplugin_jwplayer_videosource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('video', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='sources', null=True, to=orm['cmsplugin_jwplayer.JWVideo'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('default', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('media_type', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
        ))
        db.send_create_signal(u'cmsplugin_jwplayer', ['VideoSource'])


    def backwards(self, orm):
        # Deleting model 'JWVideo'
        db.delete_table(u'cmsplugin_jwplayer_jwvideo')

        # Deleting model 'VideoSource'
        db.delete_table(u'cmsplugin_jwplayer_videosource')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'cmsplugin_jwplayer.jwvideo': {
            'Meta': {'object_name': 'JWVideo', '_ormbases': ['cms.CMSPlugin']},
            'aspect_ratio': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'autostart': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'controls': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'final_frame': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'jwplayer_license': ('django.db.models.fields.CharField', [], {'default': "'cWaauZOldSHd2qpqjoecJ6k3DAFsnZP1X0EKCw=='", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'jwplayer_script': ('django.db.models.fields.URLField', [], {'default': "'/static/js/jwplayer/jwplayer.js'", 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'primary': ('django.db.models.fields.CharField', [], {'default': "'html5'", 'max_length': '10'}),
            'repeat': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reserve_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'skin': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'stretching': ('django.db.models.fields.CharField', [], {'default': "'uniform'", 'max_length': '10'}),
            'width': ('django.db.models.fields.CharField', [], {'default': "'100%'", 'max_length': '4', 'null': 'True', 'blank': 'True'})
        },
        u'cmsplugin_jwplayer.videosource': {
            'Meta': {'ordering': "('order',)", 'object_name': 'VideoSource'},
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'media_type': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'sources'", 'null': 'True', 'to': u"orm['cmsplugin_jwplayer.JWVideo']"})
        }
    }

    complete_apps = ['cmsplugin_jwplayer']