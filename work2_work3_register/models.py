# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Member(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=128)
    user_email = models.CharField(unique=True, max_length=100)
    user_birth = models.DateField(blank=True, null=True)
    user_avator = models.CharField(max_length=50, blank=True, null=True)
    user_age = models.IntegerField(blank=True, null=True)
    # last_update = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'member'
