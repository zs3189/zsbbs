# Generated by Django 2.0 on 2018-01-17 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=32, unique=True)),
                ('superadmin', models.CharField(max_length=32)),
                ('admin', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='My_bbs_users',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('signature', models.CharField(default='这家伙也太懒了', max_length=128)),
                ('headshow', models.ImageField(default='upload_imgs/user0.png', upload_to='upload_imgs/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post_details',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('content', tinymce.models.HTMLField(verbose_name='文章详情')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('summary', models.CharField(blank=True, max_length=128, null=True)),
                ('view_count', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbsapp.My_bbs_users')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbsapp.Categories')),
            ],
        ),
        migrations.AddField(
            model_name='post_details',
            name='post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bbsapp.Posts', verbose_name='所属文章'),
        ),
        migrations.AddField(
            model_name='comments',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbsapp.My_bbs_users'),
        ),
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbsapp.Posts'),
        ),
    ]
