import graphene
import graphql_geojson
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from server.models import PatientHistory, Patient, Location


class PatientNode(DjangoObjectType):
    class Meta:
        model = Patient
        filter_fields = {
            'name': ['exact', 'icontains'],
            'hkid': ['exact', 'icontains'],
            'case_num': ['exact', 'icontains']
        }
        interfaces = (relay.Node,)


class LocationNode(graphql_geojson.GeoJSONType):
    class Meta:
        model = Location
        geojson_field = 'coordinate'
        filter_fields = {
            'name': ['exact', 'icontains'],
            'address': ['exact', 'icontains'],
            'district': ['exact', 'icontains']
        }
        interfaces = (relay.Node,)


class PatientHistoryNode(DjangoObjectType):
    class Meta:
        model = PatientHistory
        filter_fields = {
            "category": ['exact', 'icontains'],
        }
        interfaces = (relay.Node,)


class Query(object):
    patient = relay.Node.Field(PatientNode)
    location = relay.Node.Field(LocationNode)
    patient_history = relay.Node.Field(PatientHistoryNode)

    all_patients = DjangoFilterConnectionField(PatientNode)
    all_locations = DjangoFilterConnectionField(PatientHistoryNode)
    all_patient_histories = DjangoFilterConnectionField(PatientHistoryNode)
