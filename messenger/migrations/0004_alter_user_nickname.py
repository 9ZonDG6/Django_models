# Generated by Django 5.1.2 on 2024-10-09 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0003_user_nickname_alter_post_post_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=50, verbose_name='Никнейм'),
        ),
    ]
