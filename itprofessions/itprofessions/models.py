from django.db import models


class Profession(models.Model):
    title = models.CharField('Название', max_length=50)
    profession = models.TextField('Описание')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'


class Career(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    profession = models.TextField('Описание')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = 'Призвание'
        verbose_name_plural = 'Призвания'


class CareerProfs(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    duties = models.TextField('Обязанности')
    workplace = models.TextField('Где можно работать')
    pay = models.TextField('Зарплата')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'