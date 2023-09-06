from django.db import models


class MaleQuestion(models.Model):
    text = models.CharField('Текст вопроса', max_length=300)

    def __str__(self):
        return self.text


class FemaleQuestion(models.Model):
    text = models.CharField('Текст вопроса', max_length=300)

    def __str__(self):
        return self.text


class AverageData(models.Model):
    scale = models.CharField('Шкала', max_length=5)
    yes = models.CharField('Ответы "да"', max_length=500, blank=True)
    no = models.CharField('Ответы "Нет"', max_length=500, blank=True)
    m_male = models.FloatField('Мужчины M')
    sigma_male = models.FloatField('Мужчины  δ')
    m_female = models.FloatField('Женщины M')
    sigma_female = models.FloatField('Женщины  δ')

    def __str__(self):
        return self.scale


class ResultsData(models.Model):
    id = models.UUIDField('Идентификатор', primary_key=True)
    results = models.JSONField()
