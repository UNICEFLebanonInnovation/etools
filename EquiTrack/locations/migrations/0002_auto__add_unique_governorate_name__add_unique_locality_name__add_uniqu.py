# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Governorate', fields ['name']
        db.create_unique(u'locations_governorate', ['name'])

        # Adding unique constraint on 'Locality', fields ['name']
        db.create_unique(u'locations_locality', ['name'])

        # Adding unique constraint on 'GatewayType', fields ['name']
        db.create_unique(u'locations_gatewaytype', ['name'])

        # Adding unique constraint on 'Region', fields ['name']
        db.create_unique(u'locations_region', ['name'])

        # Adding unique constraint on 'Location', fields ['name']
        db.create_unique(u'locations_location', ['name'])


    def backwards(self, orm):
        # Removing unique constraint on 'Location', fields ['name']
        db.delete_unique(u'locations_location', ['name'])

        # Removing unique constraint on 'Region', fields ['name']
        db.delete_unique(u'locations_region', ['name'])

        # Removing unique constraint on 'GatewayType', fields ['name']
        db.delete_unique(u'locations_gatewaytype', ['name'])

        # Removing unique constraint on 'Locality', fields ['name']
        db.delete_unique(u'locations_locality', ['name'])

        # Removing unique constraint on 'Governorate', fields ['name']
        db.delete_unique(u'locations_governorate', ['name'])


    models = {
        u'locations.gatewaytype': {
            'Meta': {'object_name': 'GatewayType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64L'})
        },
        u'locations.governorate': {
            'Meta': {'object_name': 'Governorate'},
            'area': ('django.contrib.gis.db.models.fields.MultiPointField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45L'})
        },
        u'locations.locality': {
            'Meta': {'object_name': 'Locality'},
            'area': ('django.contrib.gis.db.models.fields.MultiPointField', [], {'null': 'True', 'blank': 'True'}),
            'cad_code': ('django.db.models.fields.CharField', [], {'max_length': '11L'}),
            'cas_code': ('django.db.models.fields.CharField', [], {'max_length': '11L'}),
            'cas_code_un': ('django.db.models.fields.CharField', [], {'max_length': '11L'}),
            'cas_village_name': ('django.db.models.fields.CharField', [], {'max_length': '128L'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128L'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.Region']"})
        },
        u'locations.location': {
            'Meta': {'object_name': 'Location'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'locality': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.Locality']", 'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45L', 'blank': 'True'}),
            'p_code': ('django.db.models.fields.CharField', [], {'max_length': '32L', 'blank': 'True'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'})
        },
        u'locations.region': {
            'Meta': {'object_name': 'Region'},
            'area': ('django.contrib.gis.db.models.fields.MultiPointField', [], {'null': 'True', 'blank': 'True'}),
            'governorate': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.Governorate']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45L'})
        }
    }

    complete_apps = ['locations']