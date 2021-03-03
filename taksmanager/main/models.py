from django.db import models


class Task(models.Model):
    title = models.CharField("Title", max_length=250)
    task = models.TextField('description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
