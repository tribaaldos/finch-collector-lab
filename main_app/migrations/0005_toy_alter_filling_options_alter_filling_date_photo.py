# Generated by Django 4.2.2 on 2023-06-20 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_rename_fillingdeposit_filling'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='filling',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='filling',
            name='date',
            field=models.DateField(verbose_name='filling date'),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.bike')),
            ],
        ),
    ]
