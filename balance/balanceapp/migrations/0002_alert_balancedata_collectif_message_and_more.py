# Generated by Django 4.1 on 2022-09-09 13:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('balanceapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('type', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'OverWeight'), (2, 'NoFut'), (3, 'EndFut'), (4, 'OverHeat'), (5, 'OverHumidity'), (6, 'NoBalance'), (7, 'NoLedScreen')], null=True)),
                ('data', models.TextField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='BalanceData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Collectif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=32)),
            ],
        ),
        migrations.RenameField(
            model_name='beer',
            old_name='tare',
            new_name='quantity',
        ),
        migrations.AddField(
            model_name='beer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='beer',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='beer',
            name='weight_empty',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)), #Todelete
                ('volume', models.FloatField(default=0.0)),
                ('related_beer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='balanceapp.beer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
