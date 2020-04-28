from django.db import models

# Create your models here.

class information(models.Model):
    标题 = models.CharField(max_length=100, unique=True)
    日期 = models.DateField()
    会场 = models.CharField(max_length=100, blank=True)
    出演 = models.TextField()
    详情 = models.TextField(blank=True)

    #数据表

    class Meta:
        verbose_name_plural = "information"
        db_table = "information"

    def __str__(self):
        return self.出演