# Generated by Django 5.0.6 on 2024-05-30 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('ISBN', models.CharField(max_length=13)),
                ('author', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('availability', models.CharField(choices=[('true', 'True'), ('false', 'False')], default='false', max_length=5)),
            ],
        ),
    ]
