import graphene
import graphql_geojson
from graphene_django.types import DjangoObjectType
from server.models import PatientHistory, Patient, Location


class PatientType(DjangoObjectType):
    class Meta:
        model = Patient


class LocationType(graphql_geojson.GeoJSONType):
    class Meta:
        model = Location
        geojson_field = 'coordinate'


class PatientHistoryType(DjangoObjectType):
    class Meta:
        model = PatientHistory


class Query(object):
    all_patients = graphene.List(PatientType)
    all_locations = graphene.List(PatientHistoryType)

    def resolve_all_patients(self, info, **kwargs):
        return Patient.objects.prefetch_related("histories").all()

    def resolve_all_locations(self, info, **kwargs):
        return Location.objects.prefetch_related("histories").all()
