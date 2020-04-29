import graphene
import graphql_geojson
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from server.models import PatientHistory, Patient, Location
from server.serializers import LocationSerializer, PatientHistorySerializer, \
    PatientSerializer
from graphene_django.rest_framework.mutation import SerializerMutation
from graphql_relay import from_global_id, to_global_id
from django.contrib.gis.geos import Point
from django.contrib.auth import authenticate, login, logout


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


class PatientType(DjangoObjectType):
    class Meta:
        model = Patient


class PatientHistoryType(DjangoObjectType):
    class Meta:
        model = PatientHistory


class LocationType(DjangoObjectType):
    class Meta:
        model = Location


class CreatePatientMutation(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        hkid = graphene.String(required=True)
        birthday = graphene.Date(required=True)
        confirmed_day = graphene.Date(required=True)
        case_num = graphene.Int(required=True)

    id = graphene.ID(required=True)
    name = graphene.String(required=True)
    hkid = graphene.String(required=True)
    birthday = graphene.Date(required=True)
    confirmed_day = graphene.Date(required=True)
    case_num = graphene.Int(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, name, hkid, birthday,
        confirmed_day, case_num, client_mutation_id):
        if not info.context.user.is_authenticated():
            raise PermissionError("user not logged in")

        p = Patient.objects.create(
            name=name,
            hkid=hkid.upper().replace('(', '').replace(')', ''),
            birthday=birthday,
            confirmed_day=confirmed_day,
            case_num=case_num,
        )
        p.save()
        return CreatePatientMutation(
            id=to_global_id(PatientNode.__name__, p.id),
            name=p.name,
            hkid=p.hkid,
            birthday=p.birthday,
            confirmed_day=p.confirmed_day,
            case_num=p.case_num
        )


class UpdatePatientMutation(relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)
        name = graphene.String()
        hkid = graphene.String()
        birthday = graphene.Date()
        confirmed_day = graphene.Date()
        case_num = graphene.Int()

    id = graphene.ID(required=True)
    name = graphene.String(required=True)
    hkid = graphene.String(required=True)
    birthday = graphene.Date(required=True)
    confirmed_day = graphene.Date(required=True)
    case_num = graphene.Int(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, name, hkid, birthday,
        confirmed_day, case_num, client_mutation_id):
        if not info.context.user.is_authenticated():
            raise PermissionError("user not logged in")

        p = Patient.objects.get(
            pk=from_global_id(id)[1]
        )
        if name is not None:
            p.name = name
        if hkid is not None:
            p.hkid = hkid.upper().replace('(', '').replace(')', '')
        if birthday is not None:
            p.birthday = birthday
        if confirmed_day is not None:
            p.confirmed_day = confirmed_day
        if case_num is not None:
            p.case_num = case_num
        p.save()
        return UpdatePatientMutation(
            id=to_global_id(PatientNode.__name__, p.id),
            name=p.name,
            hkid=p.hkid,
            birthday=p.birthday,
            confirmed_day=p.confirmed_day,
            case_num=p.case_num
        )


class DeletePatientMutation(relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)

    id = graphene.ID(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, client_mutation_id):
        if not info.context.user.is_authenticated():
            raise PermissionError("user not logged in")

        p = Patient.objects.get(
            pk=from_global_id(id)[1]
        )
        oid = to_global_id(PatientNode.__name__, p.id)
        p.delete()
        return DeletePatientMutation(id=oid)


class CreateLocationMutation(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        address = graphene.String(required=True)
        district = graphene.String(required=True)
        coordinate_x = graphene.Float(required=True)
        coordinate_y = graphene.Float(required=True)

    id = graphene.ID(required=True)
    name = graphene.String(required=True)
    address = graphene.String(required=True)
    district = graphene.String(required=True)
    coordinate_x = graphene.Float(required=True)
    coordinate_y = graphene.Float(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, name, address, district,
        coordinate_x, coordinate_y, client_mutation_id):
        if not info.context.user.is_authenticated():
            raise PermissionError("user not logged in")

        p = Location.objects.create(
            name=name,
            address=address,
            district=district,
            coordinate=Point(x=coordinate_x, y=coordinate_y)
        )
        p.save()
        return CreateLocationMutation(
            id=to_global_id(LocationNode.__name__, p.id),
            name=p.name,
            address=p.address,
            district=p.district,
            coordinate_x=p.coordinate.x,
            coordinate_y=p.coordinate.y
        )


class UpdateLocationMutation(relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)
        name = graphene.String()
        address = graphene.String()
        district = graphene.String()
        coordinate_x = graphene.Float()
        coordinate_y = graphene.Float()

    id = graphene.ID(required=True)
    name = graphene.String(required=True)
    address = graphene.String(required=True)
    district = graphene.String(required=True)
    coordinate_x = graphene.Float(required=True)
    coordinate_y = graphene.Float(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, name, address, district,
        coordinate_x, coordinate_y, client_mutation_id):
        if not info.context.user.is_authenticated():
            raise PermissionError("user not logged in")

        p = Location.objects.get(
            pk=from_global_id(id)[1]
        )
        if name is not None:
            p.name = name
        if address is not None:
            p.address = address
        if district is not None:
            p.district = district
        if coordinate_x is not None:
            p.coordinate.x = coordinate_x
        if coordinate_y is not None:
            p.coordinate.y = coordinate_y

        p.save()

        return UpdateLocationMutation(
            id=to_global_id(LocationNode.__name__, p.id),
            name=p.name,
            address=p.address,
            district=p.district,
            coordinate_x=p.coordinate.x,
            coordinate_y=p.coordinate.y
        )


class DeleteLocationMutation(relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)

    id = graphene.ID(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, client_mutation_id):
        if not info.context.user.is_authenticated():
            raise PermissionError("user not logged in")

        p = Location.objects.get(
            pk=from_global_id(id)[1]
        )
        oid = to_global_id(LocationNode.__name__, p.id)
        p.delete()
        return DeleteLocationMutation(id=oid)


class CreatePatientHistoryMutation(relay.ClientIDMutation):
    class Input:
        patient_id = graphene.ID(required=True)
        location_id = graphene.ID(required=True)
        start = graphene.Date(required=True)
        end = graphene.Date(required=True)
        detail = graphene.String(required=True)
        category = graphene.String(required=True)

    id = graphene.ID(required=True)
    patient_id = graphene.ID()
    location_id = graphene.ID()
    start = graphene.Date(required=True)
    end = graphene.Date(required=True)
    detail = graphene.String(required=True)
    category = graphene.String(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, patient_id, location_id,
        start, end, detail, category, client_mutation_id):
        if not info.context.user.is_authenticated():
            raise PermissionError("user not logged in")

        p = PatientHistory.objects.create(
            patient_id=from_global_id(patient_id)[1],
            location_id=from_global_id(location_id)[1],
            start=start,
            end=end,
            detail=detail,
            category=category
        )
        p.save()
        return CreatePatientHistoryMutation(
            id=to_global_id(PatientHistoryNode.__name__, p.id),
            patient_id=to_global_id(PatientNode.__name__, p.patient_id),
            location_id=to_global_id(LocationNode.__name__, p.location_id),
            start=p.start,
            end=p.end,
            detail=p.detail,
            category=p.category
        )


class UpdatePatientHistoryMutation(relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)
        patient_id = graphene.ID()
        location_id = graphene.ID()
        start = graphene.Date()
        end = graphene.Date()
        detail = graphene.String()
        category = graphene.String()

    id = graphene.ID(required=True)
    patient_id = graphene.ID()
    location_id = graphene.ID()
    start = graphene.Date(required=True)
    end = graphene.Date(required=True)
    detail = graphene.String(required=True)
    category = graphene.String(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, patient_id, location_id,
        start, end, detail, category, client_mutation_id):
        if not info.context.user.is_authenticated():
            raise PermissionError("user not logged in")

        p = PatientHistory.objects.get(
            pk=from_global_id(id)[1]
        )
        if patient_id is not None:
            p.patient_id = from_global_id(patient_id)[1]
        if location_id is not None:
            p.location_id = from_global_id(location_id)[1]
        if start is not None:
            p.start = start
        if end is not None:
            p.end = end
        if detail is not None:
            p.detail = detail
        if category is not None:
            p.category = category

        p.save()

        return UpdatePatientHistoryMutation(
            id=to_global_id(PatientHistoryNode.__name__, p.id),
            patient_id=to_global_id(PatientNode.__name__, p.patient_id),
            location_id=to_global_id(LocationNode.__name__, p.location_id),
            start=start,
            end=end,
            detail=detail,
            category=category
        )


class DeletePatientHistoryMutation(relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=True)

    id = graphene.ID(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, client_mutation_id):
        if not info.context.user.is_authenticated():
            raise PermissionError("user not logged in")

        p = PatientHistory.objects.get(pk=from_global_id(id)[1])
        oid = to_global_id(PatientHistoryNode.__name__, p.id)
        p.delete()
        return DeletePatientHistoryMutation(id=oid)


class LoginMutation(relay.ClientIDMutation):
    class Input:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    success = graphene.Boolean(required=True)
    groups = graphene.List(graphene.String, required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, username, password):
        user = authenticate(info.context, username=username, password=password)
        if user is not None:
            login(info.context, user)
            return LoginMutation(success=True, groups=user.groups.all())
        else:
            return LoginMutation(success=False, groups=[])


class LogoutMutation(relay.ClientIDMutation):
    class Input:
        pass

    success = graphene.Boolean(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info):
        logout(info.context)
        return LogoutMutation(success=True)


# class PatientMutation(SerializerMutation):
#     class Meta:
#         serializer_class = PatientSerializer
#         model_class = Patient
#         lookup_field = 'id'
#
#
# class PatientHistoryMutation(SerializerMutation):
#     class Meta:
#         serializer_class = PatientHistorySerializer
#         model_class = PatientHistory
#         lookup_field = 'id'
#
#
# class LocationMutation(SerializerMutation):
#     class Meta:
#         serializer_class = LocationSerializer
#         model_class = Location
#         lookup_field = 'id'


class Query(object):
    patient = relay.Node.Field(PatientNode)
    location = relay.Node.Field(LocationNode)
    patient_history = relay.Node.Field(PatientHistoryNode)

    all_patients = DjangoFilterConnectionField(PatientNode)
    all_locations = DjangoFilterConnectionField(LocationNode)
    all_patient_histories = DjangoFilterConnectionField(PatientHistoryNode)


class Mutation(object):
    # mutate_patient = PatientMutation.Field()
    # mutate_location = LocationMutation.Field()
    # mutate_patient_history = PatientHistoryMutation.Field()

    create_patient = CreatePatientMutation.Field()
    update_patient = UpdatePatientMutation.Field()
    delete_patient = DeletePatientMutation.Field()

    create_location = CreateLocationMutation.Field()
    update_location = UpdateLocationMutation.Field()
    delete_location = DeleteLocationMutation.Field()

    create_patient_history = CreatePatientHistoryMutation.Field()
    update_patient_history = UpdatePatientHistoryMutation.Field()
    delete_patient_history = DeletePatientHistoryMutation.Field()
