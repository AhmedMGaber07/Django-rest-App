# Generated by Django 4.1.7 on 2023-07-22 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footer', '0004_rename_certificate_pdf_certificate_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='certificate',
            field=models.ImageField(default='', upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='pdf',
            field=models.FileField(default='', upload_to='documents/'),
        ),
    ]
