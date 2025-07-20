from django.db import models

# Create your models here.

class Block(models.Model):
    index = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()
    previous_hash = models.CharField(max_length=64)
    hash = models.CharField(max_length=64)
    nonce = models.PositiveIntegerField()
    proof_of_work_time = models.FloatField()

    def __str__(self):
        return f"Block {self.index} - {self.hash[:10]}..."
