# Generated by Django 4.1.7 on 2023-07-22 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('footer', '0002_alter_certificate_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certificate',
            options={'verbose_name': 'Certificate', 'verbose_name_plural': 'Certificates'},
        ),
    ]
