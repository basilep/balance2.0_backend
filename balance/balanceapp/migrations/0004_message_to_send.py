# Generated by Django 4.1 on 2023-02-28 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balanceapp', '0003_alter_message_message_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message_to_send',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=128)),
                ('permanent', models.BooleanField()),
                ('frequence', models.FloatField(default=0.0)),
            ],
        ),
    ]