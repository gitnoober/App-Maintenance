from dataclasses import field
from rest_framework.serializers import Serializer
from .models import CommitteeMember

class AllMembersSerializer(Serializer):
    class Meta:
        model = CommitteeMember
        fields = '__all__'