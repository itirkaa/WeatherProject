# Generated by Django 2.2 on 2019-06-01 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('message', models.TextField(blank=True)),
            ],
        ),
    ]