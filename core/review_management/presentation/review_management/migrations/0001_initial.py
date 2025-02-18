# Generated by Django 5.0.6 on 2025-02-09 12:33

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inner_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('public_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('rating', models.DecimalField(decimal_places=1, editable=False, max_digits=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inner_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('public_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('text', models.TextField()),
                ('rating', models.PositiveSmallIntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
