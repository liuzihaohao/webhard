from statistics import mode
from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
# Create your models here.
class messgaelist(models.Model):
    id=models.AutoField(primary_key=True,verbose_name='id')
    file=models.FileField(upload_to='file/',verbose_name="文件")
    allpeople=models.ForeignKey("auth.User",on_delete=models.CASCADE,to_field="username",verbose_name="文件所有者")
    text=models.TextField(max_length=4096,verbose_name="备注",null=True, blank=True)
    time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    class Meta:
        verbose_name='文件列表'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.text