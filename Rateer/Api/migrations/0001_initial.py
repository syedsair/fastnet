# Generated by Django 4.0.2 on 2022-06-21 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiComplain',
            fields=[
                ('ComplainId', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=512)),
                ('Complain', models.CharField(max_length=2048)),
                ('ComplainStatus', models.CharField(choices=[('1', 'Submitted'), ('2', 'Accepted'), ('3', 'Rejected')], max_length=500)),
                ('Complainer', models.CharField(max_length=200)),
                ('Time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ApiFilters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GroupId', models.CharField(max_length=20)),
                ('Batch', models.CharField(max_length=10)),
                ('Dept', models.CharField(max_length=20)),
                ('Less_Workload', models.BooleanField(default=False)),
                ('Clashes', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ApiGroup',
            fields=[
                ('GroupId', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=2048)),
                ('Archived', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ApiGroupMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GroupId', models.CharField(max_length=100)),
                ('UserId', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ApiGroupPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GroupId', models.CharField(max_length=100)),
                ('PostId', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ApiMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sender', models.CharField(max_length=200)),
                ('Receiver', models.CharField(max_length=200)),
                ('Message', models.CharField(max_length=5000)),
                ('Time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ApiNotifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Receiver', models.CharField(max_length=50)),
                ('Sender', models.CharField(max_length=50)),
                ('Content', models.CharField(max_length=2048)),
                ('Time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ApiPost',
            fields=[
                ('PostId', models.AutoField(primary_key=True, serialize=False)),
                ('Caption', models.CharField(max_length=1024)),
                ('Poster', models.CharField(max_length=100)),
                ('PostingTime', models.TimeField()),
                ('Image', models.ImageField(max_length=1024, upload_to='Posts/')),
            ],
        ),
        migrations.CreateModel(
            name='ApiRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentId', models.CharField(max_length=50)),
                ('CourseId', models.CharField(max_length=50)),
                ('Dept', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ApiTimetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dept', models.CharField(max_length=30)),
                ('CourseCode', models.CharField(max_length=10)),
                ('CourseName', models.CharField(max_length=50)),
                ('Day', models.CharField(max_length=8)),
                ('Venue', models.CharField(max_length=15)),
                ('StartsAt', models.CharField(max_length=5)),
                ('EndsAt', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='ApiPrivacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShowAge', models.BooleanField(default=True)),
                ('ShowEmail', models.BooleanField(default=True)),
                ('ShowGender', models.BooleanField(default=True)),
                ('ShowAddress', models.BooleanField(default=True)),
                ('ShowPhone', models.BooleanField(default=True)),
                ('ShowPosts', models.BooleanField(default=True)),
                ('ThisUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_friend_first', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ApiPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Age', models.IntegerField(blank=True)),
                ('Status', models.CharField(blank=True, max_length=1024)),
                ('Address', models.CharField(blank=True, max_length=1024)),
                ('Phone', models.CharField(blank=True, max_length=254)),
                ('ProfilePicture', models.ImageField(blank=True, default='ProfilePictures/DefaultDP.jpg', max_length=1024, upload_to='ProfilePictures/')),
                ('Role', models.CharField(max_length=20)),
                ('RawPassword', models.CharField(max_length=300)),
                ('Name', models.CharField(max_length=1024)),
                ('Gender', models.CharField(max_length=10)),
                ('Dept', models.CharField(max_length=30)),
                ('ThisUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ApiLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LikedPostId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.apipost')),
                ('LikerId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ApiFriendship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Friend_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_friend_first', to=settings.AUTH_USER_MODEL)),
                ('Friend_2', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_friend_second', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ApiFriendRequests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Receiver', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_friend_receiver', to=settings.AUTH_USER_MODEL)),
                ('Sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_friend_sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ApiComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment', models.CharField(max_length=1024)),
                ('Time', models.DateTimeField()),
                ('CommentorId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('PostId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.apipost')),
            ],
        ),
    ]
