from django.db import models

# Create your models here.

class 艺人(models.Model):

    头像 = models.ImageField(upload_to='touxiang/')
    名字 = models.CharField(max_length=10, unique=True)
    性别 = models.CharField(max_length=5)
    出生 = models.DateField(blank=True)
    出生地 = models.CharField(max_length=10, blank=True)
    所属事务所 = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name_plural = "艺人"
        db_table = "艺人"

    def __str__(self):
        return self.名字

class 个人图片(models.Model):

    名字 = models.CharField(max_length=10)
    图片 = models.ImageField(upload_to='image/')
    关联 = models.ForeignKey(艺人, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "个人图片"
        db_table = "个人图片"

    def __str__(self):
        return self.名字
