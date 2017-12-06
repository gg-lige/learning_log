from django.db import models


# Create your models here.模型就是类，包含属性和方法

class Topic(models.Model):
    '''用户学习到的主题'''
    text = models.CharField(max_length=200)  # 字符或文本串
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Entry(models.Model):
    '''学的的某个主题的具体知识'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) #设置模型的删除级联属性
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:  #存储管理模型的额外信息，设置特殊属性，让Django在需要时使用Entries来表示多个条目
        verbose_name_plural='entries'

    def __str__(self):
        return self.text[:50]+'...'