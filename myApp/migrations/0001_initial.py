# Generated by Django 2.0.3 on 2018-03-16 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='')),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]