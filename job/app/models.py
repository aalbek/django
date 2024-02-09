from datetime import date
from django.db import models


class Skills(models.Model):
    title = models.CharField(max_length=50)
    percentage = models.CharField(max_length=5)

    def __str__(self):
        return self.title


class Languages(models.Model):
    lang = models.CharField(max_length=20)
    percentage = models.CharField(max_length=5)

    def __str__(self):
        return self.lang


class Exp(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(verbose_name='Description', blank=True)
    stack_tech = models.TextField(verbose_name='Stack of technologies', blank=True)
    start_date = models.DateField(verbose_name='Start Date')
    end_date = models.DateField(verbose_name='End Date', null=True, blank=True)

    def date_range(self):
        if self.end_date:
            return f"{self.start_date.strftime('%b %Y')} - {self.end_date.strftime('%b %Y')}"
        else:
            return f"{self.start_date.strftime('%b %Y')} - Present"

    def __str__(self):
        return f'{self.title} | {self.date_range()}'


class Education(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(verbose_name='What i learned', blank=True)
    start_date = models.DateField(verbose_name='Start Date', default=date.today)
    end_date = models.DateField(verbose_name='End Date', null=True, blank=True)

    def date_range(self):
        if self.end_date:
            return f"{self.start_date.strftime('%b %Y')} - {self.end_date.strftime('%b %Y')}"
        else:
            return f"{self.start_date.strftime('%b %Y')} - Present"

    def __str__(self):
        return self.title
