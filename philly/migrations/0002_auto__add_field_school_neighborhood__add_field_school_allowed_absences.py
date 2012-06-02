# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'School.neighborhood'
        db.add_column('philly_school', 'neighborhood',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'School.allowed_absences'
        db.add_column('philly_school', 'allowed_absences',
                      self.gf('django.db.models.fields.IntegerField')(default=10),
                      keep_default=False)

        # Adding field 'School.allowed_tardy'
        db.add_column('philly_school', 'allowed_tardy',
                      self.gf('django.db.models.fields.IntegerField')(default=5),
                      keep_default=False)

        # Adding field 'School.attendance_time'
        db.add_column('philly_school', 'attendance_time',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'School.behavior_time'
        db.add_column('philly_school', 'behavior_time',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'School.pssa_reading'
        db.add_column('philly_school', 'pssa_reading',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'School.pssa_math'
        db.add_column('philly_school', 'pssa_math',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'School.national_norm'
        db.add_column('philly_school', 'national_norm',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'School.essay'
        db.add_column('philly_school', 'essay',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'School.essay_topic'
        db.add_column('philly_school', 'essay_topic',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'School.grading_style_c'
        db.add_column('philly_school', 'grading_style_c',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'School.grading_style_c_num'
        db.add_column('philly_school', 'grading_style_c_num',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'School.grading_style_c_time'
        db.add_column('philly_school', 'grading_style_c_time',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'School.other'
        db.add_column('philly_school', 'other',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'School.mission'
        db.add_column('philly_school', 'mission',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'School.pride'
        db.add_column('philly_school', 'pride',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'School.highlights'
        db.add_column('philly_school', 'highlights',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'School.partnerships'
        db.add_column('philly_school', 'partnerships',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'School.extracurriculars'
        db.add_column('philly_school', 'extracurriculars',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'School.sports'
        db.add_column('philly_school', 'sports',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'School.neighborhood'
        db.delete_column('philly_school', 'neighborhood')

        # Deleting field 'School.allowed_absences'
        db.delete_column('philly_school', 'allowed_absences')

        # Deleting field 'School.allowed_tardy'
        db.delete_column('philly_school', 'allowed_tardy')

        # Deleting field 'School.attendance_time'
        db.delete_column('philly_school', 'attendance_time')

        # Deleting field 'School.behavior_time'
        db.delete_column('philly_school', 'behavior_time')

        # Deleting field 'School.pssa_reading'
        db.delete_column('philly_school', 'pssa_reading')

        # Deleting field 'School.pssa_math'
        db.delete_column('philly_school', 'pssa_math')

        # Deleting field 'School.national_norm'
        db.delete_column('philly_school', 'national_norm')

        # Deleting field 'School.essay'
        db.delete_column('philly_school', 'essay')

        # Deleting field 'School.essay_topic'
        db.delete_column('philly_school', 'essay_topic')

        # Deleting field 'School.grading_style_c'
        db.delete_column('philly_school', 'grading_style_c')

        # Deleting field 'School.grading_style_c_num'
        db.delete_column('philly_school', 'grading_style_c_num')

        # Deleting field 'School.grading_style_c_time'
        db.delete_column('philly_school', 'grading_style_c_time')

        # Deleting field 'School.other'
        db.delete_column('philly_school', 'other')

        # Deleting field 'School.mission'
        db.delete_column('philly_school', 'mission')

        # Deleting field 'School.pride'
        db.delete_column('philly_school', 'pride')

        # Deleting field 'School.highlights'
        db.delete_column('philly_school', 'highlights')

        # Deleting field 'School.partnerships'
        db.delete_column('philly_school', 'partnerships')

        # Deleting field 'School.extracurriculars'
        db.delete_column('philly_school', 'extracurriculars')

        # Deleting field 'School.sports'
        db.delete_column('philly_school', 'sports')


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
            'mission': ('django.db.models.fields.TextField', [], {'default': "''"}),
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