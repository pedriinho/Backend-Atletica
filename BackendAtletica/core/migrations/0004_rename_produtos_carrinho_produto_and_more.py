# Generated by Django 4.2.4 on 2023-09-02 16:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_carrinho'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carrinho',
            old_name='produtos',
            new_name='produto',
        ),
        migrations.RenameField(
            model_name='carrinho',
            old_name='total',
            new_name='quantidade',
        ),
        migrations.AddField(
            model_name='carrinho',
            name='data',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carrinho',
            name='idUsuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carrinho',
            name='valorTotal',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
