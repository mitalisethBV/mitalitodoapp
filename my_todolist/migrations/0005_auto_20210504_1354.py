# Generated by Django 3.1.7 on 2021-05-04 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_todolist', '0004_auto_20210504_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[(1, 'Completed'), (2, 'TO be done')], default='to be done', max_length=250, null=True),
        ),
    ]
