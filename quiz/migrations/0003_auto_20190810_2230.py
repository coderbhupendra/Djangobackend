# Generated by Django 2.2.4 on 2019-08-10 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_submission'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='text',
            new_name='answer_text',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='is_valid',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='is_published',
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='correct_answer', to='quiz.Answer'),
        ),
        migrations.AddField(
            model_name='question',
            name='choices',
            field=models.ManyToManyField(related_name='choices', to='quiz.Answer'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='answers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='answer', to='quiz.Answer'),
        ),
    ]
