# Generated by Django 2.1.1 on 2018-09-26 06:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OutlineModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_id', models.IntegerField(choices=[(1, 'Python'), (2, 'Java')], default=0, verbose_name='学科id')),
                ('stage_id', models.IntegerField(choices=[(5, '第一阶段'), (8, '第二阶段'), (9, '第五阶段'), (12, '第二阶段'), (13, '第三阶段')], default=0, verbose_name='阶段id')),
                ('number', models.IntegerField(default=0, verbose_name='序列')),
                ('title', models.CharField(max_length=255, verbose_name='大纲标题')),
                ('days', models.IntegerField(default=0, verbose_name='学时')),
                ('advancing', models.CharField(max_length=255, verbose_name='高级内容')),
                ('remark', models.CharField(max_length=255, verbose_name='备注')),
                ('status', models.IntegerField(default=0, verbose_name='状态')),
                ('creater', models.CharField(max_length=255, verbose_name='创建者')),
                ('create_time', models.DateTimeField(default=datetime.datetime(2018, 9, 26, 14, 24, 24, 838664), verbose_name='创建时间')),
                ('updater', models.CharField(max_length=255, verbose_name='更新者')),
                ('update_time', models.DateTimeField(default=datetime.datetime(2018, 9, 26, 14, 24, 24, 838664), verbose_name='更新时间')),
            ],
            options={
                'db_table': 'outline',
            },
        ),
    ]