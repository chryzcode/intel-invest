# Generated by Django 3.2.4 on 2021-10-21 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intel_invest_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]