from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Block
from .serializers import BlockSerializer
from django.utils import timezone
import hashlib, json, time

# Create your views here.

class BlockListView(generics.ListAPIView):
    queryset = Block.objects.all().order_by('index')
    serializer_class = BlockSerializer
    permission_classes = [permissions.AllowAny]

# Utility to create a new block (to be called from other apps)
def create_block(data):
    last_block = Block.objects.order_by('-index').first()
    index = 1 if not last_block else last_block.index + 1
    previous_hash = '0' * 64 if not last_block else last_block.hash
    nonce = 0
    start_time = time.time()
    while True:
        block_string = f'{index}{timezone.now()}{json.dumps(data, sort_keys=True)}{previous_hash}{nonce}'
        block_hash = hashlib.sha256(block_string.encode()).hexdigest()
        if block_hash.startswith('0000'):
            break
        nonce += 1
    proof_of_work_time = time.time() - start_time
    block = Block.objects.create(
        index=index,
        data=data,
        previous_hash=previous_hash,
        hash=block_hash,
        nonce=nonce,
        proof_of_work_time=proof_of_work_time
    )
    return block
