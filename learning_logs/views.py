from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    """学习笔记主页"""
    return render(request,'learning_logs/index.html')


def topics(request):
    '''显示所有主题'''
    topics=Topic.objects.order_by('date_added')  #返回查询到的结果
    context={'topics':topics}   #上下文，该字典键为将在模板中访问书库的名称，值为发送给模板的数据
    return render(request,'learning_logs/topics.html',context)

def topic(request,topic_id):
    '''显示单个主题及其所有条目'''
    topic=Topic.objects.get(id=topic_id)
    entries=topic.entry_set.order_by('-date_added')  #-表示降序排列
    context={'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)
