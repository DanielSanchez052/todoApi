# Generated by Django 3.2.4 on 2021-07-12 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0003_auto_20210712_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grouptask',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Name'),
        ),
    ]