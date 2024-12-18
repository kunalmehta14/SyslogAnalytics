# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Devicelist(models.Model):
    devicename = models.CharField(max_length=255, blank=True, null=True)
    devid = models.CharField(max_length=20)
    devicevendor = models.CharField(max_length=20, blank=True, null=True)
    devip = models.CharField(primary_key=True, max_length=15)

    class Meta:
        managed = False
        db_table = 'devicelist'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Fortinetlogs(models.Model):
    logid = models.CharField(primary_key=True, max_length=50)  # The composite primary key (logid, timestamp) found, that is not supported. The first column is selected.
    priority = models.CharField(max_length=20, blank=True, null=True)
    tz = models.CharField(max_length=5, blank=True, null=True)
    subtype = models.CharField(max_length=20, blank=True, null=True)
    vd = models.CharField(max_length=50, blank=True, null=True)
    srcip = models.CharField(max_length=15, blank=True, null=True)
    srcintf = models.CharField(max_length=50, blank=True, null=True)
    srcport = models.IntegerField(blank=True, null=True)
    srcintfrole = models.CharField(max_length=20, blank=True, null=True)
    dstip = models.CharField(max_length=15, blank=True, null=True)
    dstintf = models.CharField(max_length=50, blank=True, null=True)
    dstport = models.IntegerField(blank=True, null=True)
    dstintfrole = models.CharField(max_length=15, blank=True, null=True)
    srccountry = models.CharField(max_length=50, blank=True, null=True)
    dstcountry = models.CharField(max_length=50, blank=True, null=True)
    sessionid = models.BigIntegerField(blank=True, null=True)
    proto = models.IntegerField(blank=True, null=True)
    action = models.CharField(max_length=15, blank=True, null=True)
    policyid = models.IntegerField(blank=True, null=True)
    policytype = models.CharField(max_length=50, blank=True, null=True)
    policyname = models.CharField(max_length=50, blank=True, null=True)
    service = models.CharField(max_length=20, blank=True, null=True)
    fortiuser = models.CharField(max_length=50, blank=True, null=True)
    fortigroup = models.CharField(max_length=50, blank=True, null=True)
    app = models.CharField(max_length=50, blank=True, null=True)
    authserver = models.CharField(max_length=50, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    sentbyte = models.BigIntegerField(blank=True, null=True)
    rcvdbyte = models.BigIntegerField(blank=True, null=True)
    sentpkt = models.BigIntegerField(blank=True, null=True)
    rcvdpkt = models.BigIntegerField(blank=True, null=True)
    vpntype = models.CharField(max_length=20, blank=True, null=True)
    dstmac = models.CharField(max_length=20, blank=True, null=True)
    dsthwvendor = models.CharField(max_length=20, blank=True, null=True)
    timestamp = models.DateTimeField()
    type = models.CharField(max_length=20, blank=True, null=True)
    logdesc = models.CharField(max_length=255, blank=True, null=True)
    devip = models.ForeignKey(Devicelist, models.DO_NOTHING, db_column='devip', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fortinetlogs'
        unique_together = (('logid', 'timestamp'),)
