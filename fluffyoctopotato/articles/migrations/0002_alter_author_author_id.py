# Generated by Django 4.1.7 on 2023-03-04 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
