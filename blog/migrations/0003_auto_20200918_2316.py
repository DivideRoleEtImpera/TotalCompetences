# Generated by Django 2.2.16 on 2020-09-18 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_plan_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plan',
            old_name='name',
            new_name='program_name',
        ),
        migrations.AddField(
            model_name='plan',
            name='program_leader',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plan',
            name='program_sub_name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plan',
            name='year',
            field=models.CharField(default=1, max_length=4),
            preserve_default=False,
        ),
    ]
