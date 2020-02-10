# Generated by Django 2.2 on 2020-01-19 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20200111_1413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='title',
            new_name='product_name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='pdf',
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default='null', upload_to='media'),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(),
        ),
    ]
