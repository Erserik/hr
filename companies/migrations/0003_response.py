# Generated by Django 5.1.6 on 2025-02-17 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_vacancy_alter_company_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('experience', models.CharField(max_length=255)),
                ('photo', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
