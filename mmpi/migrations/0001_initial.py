# Generated by Django 4.2.5 on 2023-09-15 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AverageData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scale', models.CharField(max_length=100, verbose_name='Шкала')),
                ('yes', models.JSONField(blank=True, verbose_name='Ответы "да"')),
                ('no', models.JSONField(blank=True, verbose_name='Ответы "Нет"')),
                ('m_male', models.FloatField(verbose_name='Мужчины M')),
                ('sigma_male', models.FloatField(verbose_name='Мужчины  δ')),
                ('m_female', models.FloatField(verbose_name='Женщины M')),
                ('sigma_female', models.FloatField(verbose_name='Женщины  δ')),
                ('description', models.TextField(default='', max_length=1000, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Расшифровка вопроса',
                'verbose_name_plural': 'Расшифровка вопросов',
            },
        ),
        migrations.CreateModel(
            name='FemaleQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300, verbose_name='Текст вопроса')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы (женская версия)',
            },
        ),
        migrations.CreateModel(
            name='MaleQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300, verbose_name='Текст вопроса')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы (женская версия)',
            },
        ),
        migrations.CreateModel(
            name='ResultsData',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('results', models.JSONField(verbose_name='Результаты')),
            ],
            options={
                'verbose_name': 'Результаты',
                'verbose_name_plural': 'Результаты',
            },
        ),
    ]
