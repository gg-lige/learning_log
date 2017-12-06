'''定义learning_logs的url模式'''
from django.urls import path

from . import views

app_name = 'learning_logs'  #注意在这里添加
urlpatterns = [
    path('', views.index, name='index'),  # 主页
    # 正则表达式为请求的匹配，r将接下来的字符串视为原始字符串，^开头$结束为python 字符串始终与什么都没有的url，对应基础url
    # view.index 指定要调用的视图函数，
    # 将这个url模式指定为index,不用在编写url
    path('topics/', views.topics, name='topics'),  # 显示所有主题，/省略也可以
    path('topics/<int:topic_id>/', views.topic, name='topic')  # 显示所有主题，/省略也可以
]

