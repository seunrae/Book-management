# Generated by Django 5.1.1 on 2024-09-12 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmanagement', '0005_alter_book_category_alter_book_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
