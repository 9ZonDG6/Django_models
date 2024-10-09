# Generated by Django 5.1.2 on 2024-10-09 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0002_post_post_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Никнейм'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_subject',
            field=models.CharField(max_length=100, verbose_name='Тема поста'),
        ),
    ]
