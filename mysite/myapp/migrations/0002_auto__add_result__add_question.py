# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Result'
        db.create_table(u'myapp_result', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myapp.Question'])),
        ))
        db.send_create_signal(u'myapp', ['Result'])

        # Adding model 'Question'
        db.create_table(u'myapp_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('platform_choice', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('platform_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('game_preference', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'myapp', ['Question'])


    def backwards(self, orm):
        # Deleting model 'Result'
        db.delete_table(u'myapp_result')

        # Deleting model 'Question'
        db.delete_table(u'myapp_question')


    models = {
        u'myapp.question': {
            'Meta': {'object_name': 'Question'},
            'game_preference': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'platform_choice': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'platform_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'myapp.result': {
            'Meta': {'object_name': 'Result'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myapp.Question']"})
        }
    }

    complete_apps = ['myapp']