#  Learning_Log

>  
>  这是一个基于python Django 搭建的小型项目
> 
> 

## 命令

E:\IDEAworkspace>cd learning_log

E:\IDEAworkspace\learning_log>python -m venv ll_env
>建立虚拟环境，名为ll_env

E:\IDEAworkspace\learning_log>ll_env\Scripts\activate
>激活启动环境 	

(ll_env) E:\IDEAworkspace\learning_log>pip install Django

(ll_env) E:\IDEAworkspace\learning_log>dir

(ll_env) E:\IDEAworkspace\learning_log>django-admin.py startproject learning_log .
>注意最后的点，让项目有合适的目录结构

(ll_env) E:\IDEAworkspace\learning_log>python manage.py migrate
>创建数据库db.sqlite3.sqlLite 是一种使用单个文件的数据库

(ll_env) E:\IDEAworkspace\learning_log>python manage.py runserver （8002）
>在http://127.0.0.1:8000/端口查看是否启动成功

(ll_env) E:\IDEAworkspace\learning_log>python manage.py startapp learning_logs
>另开一个terimal 。输上述命令让Django 创建应用所需的基础设施

(ll_env) E:\IDEAworkspace\learning_log>python manage.py makemigrations learning_logs
>让Django修改数据库，时期可以存储新定义的模型Topic

(ll_env) E:\IDEAworkspace\learning_log>python manage.py migrate
>让Django迁移项目

(ll_env) E:\IDEAworkspace\learning_log>python manage.py createsuperuser
>创建超级用户，通过http://127.0.0.1:8000/admin/    用户名/秘密：ll_admin/ll_admin

* 每次在model.py 中创建新的模型，都需要重新迁移数据库

* (ll_env) E:\IDEAworkspace\learning_log>python manage.py makemigrations learning_logs

* (ll_env) E:\IDEAworkspace\learning_log>python manage.py migrate
* admin.py中注册一下，即可在管理员页面看到


## 交互式终端会话
(ll_env) E:\IDEAworkspace\learning_log>python manage.py shell

/>>> from learning_logs.models import Topic

/>>> Topic.objects.all()

<QuerySet [<Topic: Chess>, <Topic: Rock Climbing>]>

//>>> topics=Topic.onjects.all()

Traceback (most recent call last):

  File "<console>", line 1, in <module>

AttributeError: type object 'Topic' has no attribute 'onjects'

/>>> topics=Topic.objects.all()

/>>> for topic in topics:

...     print(topic.id,topic)

...

1 Chess

2 Rock Climbing

/>>> t=Topic.objects.get(id=1)

/>>> t.text

'Chess'

/>>> t.date_added

datetime.datetime(2017, 12, 6, 2, 22, 41, 617396, tzinfo=<UTC>)

/>>> t.entry_set.all()

<QuerySet [<Entry: 象棋，亦作“象碁”、中国象棋（英文名Chinese chess），中国传统棋类益智游戏，在中国有着悠...>, <Entry: 棋盘
棋子活动的场所，叫作“棋盘”。在长方形的平面上，绘有九条平行的竖线和十条平行的横线相交组成，...>]>

> 通过外键关系获取时，可使用相关模型小写名称、下划线、单词set组合


## 部署
(ll_env) E:\IDEAworkspace\learning_log>pip install dj-database-url

(ll_env) E:\IDEAworkspace\learning_log>pip install dj-static

(ll_env) E:\IDEAworkspace\learning_log>pip install static3

(ll_env) E:\IDEAworkspace\learning_log>pip install gunicorn

(ll_env) E:\IDEAworkspace\learning_log>pip freeze > requirements.txt

>命令freeze 将项目中当前安装的所有包名都写入到文件 requirements.txt中。
