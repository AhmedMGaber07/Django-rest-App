# Generated by Django 4.1.7 on 2023-07-22 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_image_news_short_description_news_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newstitle',
            name='order',
            field=models.DecimalField(decimal_places=0, default='', max_digits=10),
        ),
    ]
