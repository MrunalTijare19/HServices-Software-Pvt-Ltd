# Generated by Django 5.0.1 on 2024-04-10 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_blogpost_id_alter_contact_id_alter_project_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='city',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default=' ', max_length=20),
            preserve_default=False,
        ),
    ]
