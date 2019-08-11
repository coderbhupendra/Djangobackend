# Generated by Django 2.2.4 on 2019-08-10 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20190810_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='question',
            name='exam',
        ),
        migrations.AddField(
            model_name='exam',
            name='question',
            field=models.ManyToManyField(blank=True, to='quiz.Question'),
        ),
    ]