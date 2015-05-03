# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HomeInfo'
        db.create_table(u'home_homeinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.TextField')()),
            ('site_intro', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal(u'home', ['HomeInfo'])


    def backwards(self, orm):
        # Deleting model 'HomeInfo'
        db.delete_table(u'home_homeinfo')


    models = {
        u'home.category': {
            'Meta': {'object_name': 'Category'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'displayed_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'home.event': {
            'Meta': {'object_name': 'Event'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_pinned': ('django.db.models.fields.BooleanField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'home.goodsite': {
            'Meta': {'object_name': 'GoodSite'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'home.homeinfo': {
            'Meta': {'object_name': 'HomeInfo'},
            'contact': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site_intro': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        }
    }

    complete_apps = ['home']