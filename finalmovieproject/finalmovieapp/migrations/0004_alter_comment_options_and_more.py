# Generated by Django 4.2.9 on 2024-02-01 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalmovieapp', '0003_alter_comment_options_rename_content_comment_body_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created_on',
            new_name='date_added',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='active',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
    ]
