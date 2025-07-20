from rest_framework import serializers
from .models import Block

class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ['id', 'index', 'timestamp', 'data', 'previous_hash', 'hash', 'nonce', 'proof_of_work_time'] 