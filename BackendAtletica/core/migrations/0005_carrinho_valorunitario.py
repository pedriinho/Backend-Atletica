# Generated by Django 4.2.4 on 2023-09-02 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_produtos_carrinho_produto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrinho',
            name='valorUnitario',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
