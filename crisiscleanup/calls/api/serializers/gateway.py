from rest_framework import serializers

from crisiscleanup.calls.models import Gateway

class GatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gateway
        fields = ('id','agent_id', 'name', 'agent_username', 'agent_password')
