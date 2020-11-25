# Generated by Django 3.1.1 on 2020-11-25 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logitem',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='照片'),
        ),
        migrations.AlterField(
            model_name='logitem',
            name='utime',
            field=models.DateTimeField(auto_now=True, verbose_name='最後更新時間'),
        ),
    ]
