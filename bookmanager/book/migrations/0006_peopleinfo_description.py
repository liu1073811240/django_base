# Generated by Django 2.2.5 on 2024-04-26 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20240426_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='peopleinfo',
            name='description',
            field=models.CharField(max_length=200, null=True, verbose_name='描述信息'),
        ),
    ]