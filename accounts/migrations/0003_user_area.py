# Generated by Django 2.1.7 on 2019-04-22 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190326_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='area',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
    ]
