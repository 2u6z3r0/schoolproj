# Generated by Django 2.0.2 on 2018-03-05 17:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import schoolmanagement.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('village', models.CharField(max_length=60)),
                ('taluk', models.CharField(max_length=60)),
                ('dist', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=60)),
                ('schoolCode', models.IntegerField(default=999999)),
                ('staffCount', models.IntegerField(default=0)),
                ('stdCount', models.IntegerField(default=0)),
                ('schoolUser', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('registerNum', models.CharField(max_length=60)),
                ('registerBookNum', models.CharField(max_length=10)),
                ('bloodGroup', models.CharField(max_length=3)),
                ('dob', models.DateField(default=datetime.date.today)),
                ('fatherName', models.CharField(max_length=60)),
                ('motherName', models.CharField(max_length=60)),
                ('grandFatherName', models.CharField(max_length=60)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Transgender')], max_length=1)),
                ('pd', models.CharField(choices=[('Y', 'YES'), ('N', 'NO')], max_length=1)),
                ('pdtype', models.CharField(blank=True, max_length=40, null=True)),
                ('pdPercentage', models.IntegerField(default=0)),
                ('admissionDate', models.DateTimeField(auto_now=True)),
                ('standard', models.CharField(max_length=10)),
                ('division', models.CharField(max_length=3)),
                ('adharcardNum', models.IntegerField(default=0)),
                ('caste', models.CharField(max_length=30)),
                ('income', models.FloatField(max_length=30)),
                ('medium', models.CharField(choices=[('K', 'Kannada'), ('E', 'English'), ('H', 'Hindi'), ('M', 'Marathi'), ('U', 'Urdu')], max_length=2)),
                ('casteCertificateNum', models.CharField(max_length=30)),
                ('incomeCertificateNum', models.CharField(max_length=30)),
                ('bankAccNum', models.IntegerField(default=0)),
                ('bank', models.CharField(max_length=30)),
                ('ifscCode', models.CharField(max_length=11)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=schoolmanagement.models.upload_location)),
            ],
        ),
    ]