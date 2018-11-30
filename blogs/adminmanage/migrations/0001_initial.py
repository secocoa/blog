# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-27 21:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btitle', models.CharField(max_length=20, null=True)),
                ('creat_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('abstract', models.CharField(max_length=100, null=True)),
                ('body', models.CharField(max_length=150)),
                ('is_savedraft', models.BooleanField(default=False)),
                ('is_delete', models.BooleanField(default=False)),
                ('is_prvite', models.BooleanField(default=False)),
                ('is_comment', models.BooleanField(default=False)),
                ('files', models.CharField(max_length=150, null=True)),
            ],
            options={
                'db_table': 'blog',
            },
            managers=[
                ('bmymanager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=15, unique=True)),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'category',
            },
            managers=[
                ('cmanager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('is_delete', models.BooleanField(default=False)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminmanage.Blog')),
            ],
            options={
                'db_table': 'comments',
            },
            managers=[
                ('commanager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lname', models.CharField(max_length=15)),
                ('is_delete', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminmanage.Category')),
            ],
            options={
                'db_table': 'label',
            },
            managers=[
                ('lmanager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=11)),
                ('is_delete', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user',
            },
            managers=[
                ('umanager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='User_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcard', models.CharField(max_length=18)),
                ('realname', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('lastlogin', models.DateTimeField(default=datetime.datetime(2018, 11, 27, 21, 38, 50, 389115))),
                ('headportrait', models.CharField(max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='adminmanage.User')),
            ],
            options={
                'db_table': 'user_info',
            },
        ),
        migrations.CreateModel(
            name='Visitnum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_like', models.BooleanField(default=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminmanage.Blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminmanage.User')),
            ],
            options={
                'db_table': 'visitnum',
            },
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminmanage.User'),
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminmanage.User'),
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminmanage.Category'),
        ),
        migrations.AddField(
            model_name='blog',
            name='label',
            field=models.ManyToManyField(to='adminmanage.Label'),
        ),
    ]