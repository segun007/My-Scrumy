# Generated by Django 2.0.4 on 2018-04-21 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owolabiscrumy', '0003_auto_20180421_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scrumygoals',
            name='goal_status',
        ),
        migrations.AddField(
            model_name='goalstatus',
            name='goal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='owolabiscrumy.ScrumyGoals'),
            preserve_default=False,
        ),
    ]