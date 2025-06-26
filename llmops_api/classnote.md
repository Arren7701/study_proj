# 第二天课程回顾
##### 1、30行实现聊天机器人，通过转发的方式。 
##### 2、依赖生成 requirements.txt文档，导出项目的依赖
##### 3、我们还实现了接口的校验，使用的是flask_wtf
##### 4、我们还实现了数据接口的统一返回，返回json数据和message数据
##### 5、我们使用dotenv，用于配置项目的环境
##### 6、实现了统一的异常数据封装，了解了什么是埋点



# 第三天课程内容
##### 1、我们学习搭建整个测试框架，通过pytest
    pytest简单易用，比unittest更好用。
    可以很好地与其他功能协同功能
pytest 代码编写的要求：
    
    1、测试文件必须以test开头或者_test结尾
    2、测试类必须以Test开头，并且不能带有__init__方法
    3、测试函数也要用test开头
    4、断言使用的是assert

```python
func(a,b):
    if  a not None:
        pass
    else:
        return xxx
# assert 写法
func (a,b):
    assert(a is not None)
    assert(b is not None)
```

##### 2、Fixture设置测试环境，并注入测试参数
    1、新建conftest 文件

##### 3、 通过pytest.ini 来配置运行时环境

##### 4、 为我们的项目装上数据库-Flask-SQLAlchemy
    1、创建数据模型，app的数据模型
    2、新建表，新增数据
    3、增删改查
    4、运用到我们的业务中，通过 http 增删改查


关注业务，搭积木就可以了。别想着从零到一写出个框架。
想想业务怎么实现，去搭插件就行了。
搞清楚自己想做什么，想要什么就可以了。




# 第四天课程内容
#### 回顾：昨天学了什么？
    1、学习了pytest框架
    2、pytest 通过 fixture 进行参数注入
    3、通过 pytest.ini 文件 去配置pytest运行时的规则
    4、学习了 flask-sqlalchemy相关的理论知识
    5、学习了什么是ORM
    6、学习了通过Pycharm手动连接 postgres数据库
    7、通过代码完成了App的数据模型
    8、通过代码建立创建了app模型数据表格

#### 重写sql类，实现自动提交以及异常回滚。
    1、通过代码操作、创建表格
    2、完成数据库接口测试
    3、完成数据接口的自定义封装
    4、数据库迁移、备份怎么搞？———— Flask-Migrate



 