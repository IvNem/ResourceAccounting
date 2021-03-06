# Generated by Django 3.1.1 on 2021-04-14 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Количество')),
                ('unit', models.CharField(max_length=255, verbose_name='Единица измерения')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена за у.е.')),
                ('date', models.DateField(verbose_name='Дата последнего поступления')),
            ],
        ),
    ]
