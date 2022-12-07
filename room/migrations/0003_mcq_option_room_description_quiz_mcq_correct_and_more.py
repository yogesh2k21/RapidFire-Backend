# Generated by Django 4.1.3 on 2022-12-06 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('room', '0002_rename_group_room_rename_group_chat_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='MCQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_statement', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'MCQs',
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.CharField(max_length=150)),
                ('valid', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Options',
            },
        ),
        migrations.AddField(
            model_name='room',
            name='description',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('questions', models.ManyToManyField(to='room.mcq')),
                ('room', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='room.room')),
            ],
            options={
                'verbose_name_plural': 'Quizes',
            },
        ),
        migrations.AddField(
            model_name='mcq',
            name='correct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='correct_for_mcqs', to='room.option'),
        ),
        migrations.AddField(
            model_name='mcq',
            name='options',
            field=models.ManyToManyField(to='room.option'),
        ),
    ]
