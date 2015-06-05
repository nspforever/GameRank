from __future__ import unicode_literals
import logging
from rest_framework import serializers
from django.db import models

logger = logging.getLogger(__name__)


class Rank (models.Model):
    # owner/name
    score = models.IntegerField(default=0, null=True)

    class Meta:
        ordering = ('-score',)

class ScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rank
        fields = ('score',)

