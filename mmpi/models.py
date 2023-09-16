from django.db import models


class MaleQuestion(models.Model):
    text = models.CharField('Текст вопроса', max_length=300)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы (женская версия)'


class FemaleQuestion(models.Model):
    text = models.CharField('Текст вопроса', max_length=300)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы (женская версия)'


class AverageData(models.Model):
    scale = models.CharField('Шкала', max_length=100)
    yes = models.JSONField('Ответы "да"', blank=True)
    no = models.JSONField('Ответы "Нет"', blank=True)
    m_male = models.FloatField('Мужчины M')
    sigma_male = models.FloatField('Мужчины  δ')
    m_female = models.FloatField('Женщины M')
    sigma_female = models.FloatField('Женщины  δ')
    description = models.TextField('Описание', max_length=1000, default='', blank=True)

    def __str__(self):
        return self.scale

    class Meta:
        verbose_name = 'Расшифровка вопроса'
        verbose_name_plural = 'Расшифровка вопросов'


class ResultsData(models.Model):
    id = models.UUIDField('Идентификатор', primary_key=True)
    main_scales = models.JSONField('Основные шкалы')
    additional_scales = models.JSONField('Дополнительные шкалы')

    class Meta:
        verbose_name = 'Результаты'
        verbose_name_plural = 'Результаты'
