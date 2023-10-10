# Generated by Django 4.2 on 2023-04-24 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.DateField()),
                ('cirado_em', models.DateField(auto_now_add=True)),
                ('modificado_em', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]