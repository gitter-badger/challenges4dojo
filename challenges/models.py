from __future__ import unicode_literals

from django.db import models


class Challenge(models.Model):
    title = models.CharField(max_length=100)
    used = models.PositiveIntegerField(default=0)
    DIFFICULTY_CHOICES = (
        (1, 'Beginner'),
        (2, 'Medium'),
        (1, 'Hard'),
    )
    difficulty = models.CharField(
        max_length=100,
        choices=DIFFICULTY_CHOICES,
        default=1
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
