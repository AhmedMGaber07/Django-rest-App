# Generated by Django 4.1.7 on 2023-07-22 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0003_contuctform_alter_contuctus_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContuctForm',
            new_name='ContactForm',
        ),
        migrations.RenameModel(
            old_name='ContuctUs',
            new_name='ContactUs',
        ),
    ]
