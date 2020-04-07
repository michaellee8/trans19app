from server.models import Location, Patient, PatientHistory
from rest_framework.serializers import ModelSerializer, RelatedField


class PatientSerializer(ModelSerializer):
    histories = RelatedField(many=True,
                             read_only=True)

    class Meta:
        model = Patient
        fields = ['name', 'hkid', 'birthday', 'confirmed_day', 'case_num',
                  'histories']


class LocationSerializer(ModelSerializer):
    histories = RelatedField(many=True,
                             read_only=True)

    class Meta:
        model = Location
        fields = ['name', 'address', 'district', 'coordinate', 'histories']


class PatientHistorySerializer(ModelSerializer):
    class Meta:
        model = PatientHistory
        fields = ['patient', 'location', 'start', 'end', 'detail', 'category']
