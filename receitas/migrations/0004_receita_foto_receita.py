# Generated by Django 2.2 on 2021-01-28 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0003_auto_20210128_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/'),
        ),
    ]
