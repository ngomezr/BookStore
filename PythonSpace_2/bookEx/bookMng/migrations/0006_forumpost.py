# Generated by Django 3.1.6 on 2021-05-10 05:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookMng', '0005_shoppingcart'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForumPost',
            fields=[
                ('test', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='Guest', max_length=255)),
                ('body', models.TextField(max_length=500)),
                ('publishdate', models.DateField(blank=True, default=datetime.datetime(2021, 5, 10, 5, 9, 36, 585155))),
            ],
        ),
    ]
