# Generated by Django 5.0.10 on 2025-01-11 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategorySample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'CategorySample',
                'managed': False,
            },
        ),
    ]
