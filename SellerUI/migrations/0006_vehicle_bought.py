# Generated by Django 3.0.5 on 2020-06-26 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SellerUI', '0005_auto_20200626_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='bought',
            field=models.BooleanField(default=False),
        ),
    ]
