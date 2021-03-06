# Generated by Django 4.0.2 on 2022-02-13 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'ユーザー一覧表', 'verbose_name_plural': 'ユーザー一覧表'},
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='py',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='realname',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
