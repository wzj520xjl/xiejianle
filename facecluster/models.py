from django.db import models


# Create your models here.

# 用户列表
class UserList(models.Model):
    EXPERIENCE_CHOICES = (
        (1, '标注员'),
        (2, '审核员'),
        (3, '管理员'),
    )
    role = models.IntegerField(choices=EXPERIENCE_CHOICES, verbose_name='角色选择')
    name = models.CharField(max_length=20, verbose_name='用户姓名')
    create_time = models.DateTimeField(verbose_name='创建时间')
    update_time = models.DateTimeField(verbose_name='修改时间')

    class Meta:
        verbose_name = '用户列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 用户标注关系表
class Person(models.Model):
    # 所标注的文件夹记录名字
    dir_name = models.CharField(max_length=50)
    # 关联的用户
    user = models.ForeignKey(UserList)
    # 记录标注时间
    log_time = models.DateTimeField()

    class Meta:
        verbose_name = '用户标注关系表'
        verbose_name_plural = verbose_name


# 标注结果表
class ResultTable(models.Model):
    # 保存的文件夹
    save_dir = models.CharField(max_length=20)
    # 保存路径的记录
    save_path = models.CharField(max_length=50)
    # 标注状态
    STATUS_CHOICES = ((0, '未标注'),
                      (1, '已标注'),
                      )
    status = models.IntegerField(choices=STATUS_CHOICES)
    # person
    person = models.ForeignKey(Person)

    class Meta:
        verbose_name = '标注结果表'
        verbose_name_plural = verbose_name


# 文件夹路径表
class Path(models.Model):
    # 文件夹名称
    p_name = models.CharField(max_length=50)
    # 保存文件的路径
    p_path = models.FileField(max_length=128)

    class Meta:
        verbose_name = '文件路径表'
        verbose_name_plural = verbose_name


# 遍历结果表
class TraTable(models.Model):
    # 关联路径表
    path_id = models.ForeignKey(Path)
    # 遍历结果
    tra_result = models.CharField(max_length=64)
    # 遍历时间
    tra_time = models.DateTimeField()
    # 类型
    type = models.CharField(max_length=128)

    class Meta:
        verbose_name = '遍历结果表'
        verbose_name_plural = verbose_name


# 图片展示表
class ImgModel(models.Model):
    # 路径
    path = models.CharField(max_length=68)
    # 图片路径
    num = models.IntegerField()
    # 关联person表
    per_id = models.ForeignKey(Person)
    # 创建时间
    create_time = models.DateTimeField()
    # 更新时间
    update_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '图片展示表'
        verbose_name_plural = verbose_name
