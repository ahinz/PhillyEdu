# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'School.name'
        db.add_column('philly_school', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'School.locationNumber'
        db.add_column('philly_school', 'locationNumber',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'School.name'
        db.delete_column('philly_school', 'name')

        # Deleting field 'School.locationNumber'
        db.delete_column('philly_school', 'locationNumber')


    models = {
        'philly.school': {
            'Meta': {'object_name': 'School'},
            'allowed_absences': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'allowed_tardy': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'attendance_time': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'behavior_time': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'essay': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'essay_topic': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'extracurriculars': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'grading_style_c': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'grading_style_c_num': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'grading_style_c_time': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'highlights': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locationNumber': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'mission': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'national_norm': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'neighborhood': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'other': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'partnerships': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'pride': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'pssa_math': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pssa_reading': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sports': ('django.db.models.fields.TextField', [], {'default': "''"})
        }
    }

    complete_apps = ['philly']