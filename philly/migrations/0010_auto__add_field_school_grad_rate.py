# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'School.grad_rate'
        db.add_column('philly_school', 'grad_rate',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'School.grad_rate'
        db.delete_column('philly_school', 'grad_rate')


    models = {
        'philly.school': {
            'Meta': {'object_name': 'School'},
            'allowed_absences': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'allowed_tardy': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'attendance_time': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'behavior_time': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'essay': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'essay_topic': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'extracurriculars': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'grad_rate': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'grading_style_c': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'grading_style_c_num': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'grading_style_c_time': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'highlights': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invite_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'locationnumber': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'mission': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'national_norm': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'other': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'partnerships': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'pride': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'pssa_math': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pssa_reading': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'school_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sports': ('django.db.models.fields.TextField', [], {'default': "''"})
        },
        'philly.schooladdress': {
            'Meta': {'object_name': 'SchoolAddress'},
            'address_street': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'address_zip': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.TextField', [], {}),
            'locationnumber': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['philly']