# Generated by Django 4.2.4 on 2023-09-02 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_carrinho_valorunitario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrinho',
            name='valorUnitario',
        ),
    ]