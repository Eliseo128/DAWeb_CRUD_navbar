# Generated by Django 5.1.1 on 2024-11-19 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('pago_total', models.DecimalField(decimal_places=2, max_digits=100)),
                ('telefono', models.IntegerField()),
                ('hora_compra', models.TimeField()),
                ('cantidad_productos', models.IntegerField()),
                ('dia_compra', models.DateTimeField()),
            ],
        ),
    ]