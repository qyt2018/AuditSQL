# Generated by Django 2.0.2 on 2018-02-06 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserManager', '0003_contactsdetail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactsdetail',
            options={'default_permissions': (), 'verbose_name': '联系人分组详情表', 'verbose_name_plural': '联系人分组详情表'},
        ),
        migrations.AlterModelOptions(
            name='groupsdetail',
            options={'default_permissions': (), 'verbose_name': '项目分组详情表', 'verbose_name_plural': '项目分组详情表'},
        ),
        migrations.AlterModelOptions(
            name='rolesdetail',
            options={'default_permissions': (), 'verbose_name': '用户角色分组详情表', 'verbose_name_plural': '用户角色分组详情表'},
        ),
    ]
