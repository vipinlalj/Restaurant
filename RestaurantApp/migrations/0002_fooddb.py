# Generated by Django 5.1.3 on 2024-11-10 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CatName', models.CharField(blank=True, max_length=50, null=True)),
                ('FoodName', models.CharField(blank=True, max_length=50, null=True)),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
                ('Price', models.IntegerField(blank=True, max_length=3, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]