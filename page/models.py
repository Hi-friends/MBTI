# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Match(models.Model):
    mbti1 = models.CharField(primary_key=True, max_length=4)
    mbti2 = models.CharField(max_length=4)
    match_score = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'match'
        unique_together = (('mbti1', 'mbti2'),)


class MbtiUser(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    mbti1 = models.CharField(max_length=4)
    region = models.CharField(max_length=10)
    age = models.IntegerField()
    sex = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'mbti_user'

class Joined(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    mbti1 = models.CharField(max_length=4)
    region = models.CharField(max_length=10)
    match_score = models.IntegerField()
    age = models.IntegerField()
    sex = models.CharField(max_length=6)

    class Meta:
        managed = False
