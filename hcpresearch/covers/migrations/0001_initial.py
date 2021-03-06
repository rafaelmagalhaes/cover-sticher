# Generated by Django 2.2.8 on 2020-03-11 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Covers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('cover_image', models.FileField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(max_length=255)),
                ('total_amount', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
