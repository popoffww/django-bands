# Generated by Django 3.1.1 on 2020-09-20 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_index=True, max_length=128, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Участник группы',
                'verbose_name_plural': 'Участники группы',
            },
        ),
    ]
