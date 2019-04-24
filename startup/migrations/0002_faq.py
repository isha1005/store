# Generated by Django 2.2 on 2019-04-22 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('block_body', models.TextField(blank=True, max_length=5000, null=True)),
            ],
        ),
    ]