# Generated by Django 4.2.5 on 2023-09-18 12:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_projectcategories_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
