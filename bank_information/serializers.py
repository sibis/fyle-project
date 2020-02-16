from rest_framework import serializers
from bank_information.models import Banks, BankBranches


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankBranches
        fields = ('ifsc', 'bank_id', 'branch', 'address', 'city', 'district', 'state')