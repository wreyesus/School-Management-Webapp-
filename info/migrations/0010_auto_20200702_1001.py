# Generated by Django 3.0.6 on 2020-07-02 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0009_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('standard', models.IntegerField(blank=True, null=True)),
                ('section', models.CharField(blank=True, max_length=10, null=True)),
                ('branch', models.CharField(blank=True, max_length=10, null=True)),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=100)),
                ('textcontent', models.TextField(blank=True, null=True)),
                ('Fileupload', models.FileField(blank=True, null=True, upload_to='')),
            ],
            options={
                'ordering': ['-published'],
            },
        ),
        migrations.AlterModelOptions(
            name='notice',
            options={'ordering': ['-published']},
        ),
    ]
