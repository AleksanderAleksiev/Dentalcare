# Generated by Django 4.2.5 on 2024-02-04 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_rename_age_useraccount_years'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('start_date', models.CharField(max_length=30)),
                ('end_date', models.CharField(max_length=30)),
                ('creation_date_time', models.DateTimeField(auto_now_add=True)),
                ('is_all_day', models.BooleanField(blank=True, default=False, null=True)),
                ('recurrence_rule', models.CharField(blank=True, max_length=50, null=True)),
                ('excluded_dates', models.CharField(blank=True, max_length=400, null=True)),
                ('dentist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dentist', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]