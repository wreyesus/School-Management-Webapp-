# Generated by Django 3.0.6 on 2020-07-03 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0012_assignment_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='Filename',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='notice',
            name='Fileupload',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
