# Generated by Django 2.2 on 2021-01-28 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0002_receita_pessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='receita',
            name='redimento',
            field=models.IntegerField(),
        ),
    ]