from enrollStaff.models import CreateStaff
from rest_framework import serializers


class CreateStaffSerializers(serializers.ModelSerializer):
    class Meta:
        model = CreateStaff
        fields = ['id', 'name', 'email', 'gender', 'staffType']
