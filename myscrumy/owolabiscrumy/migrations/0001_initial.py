# Generated by Django 2.0.4 on 2018-04-21 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoalStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('WT', 'Weekly Task'), ('DT', 'Daily Task'), ('V', 'Verified'), ('D', 'Done')], default='WT', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ScrumyGoals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals', models.CharField(max_length=50)),
                ('descriptions', models.TextField()),
                ('date_created', models.DateTimeField(verbose_name='date created')),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScrumyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='scrumygoals',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owolabiscrumy.ScrumyUser'),
        ),
        migrations.AddField(
            model_name='goalstatus',
            name='scrumygoals',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owolabiscrumy.ScrumyGoals'),
        ),
    ]