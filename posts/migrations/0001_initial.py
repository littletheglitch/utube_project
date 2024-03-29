# Generated by Django 5.0.2 on 2024-02-24 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('text', models.TextField()),
                ('is_enable', models.BooleanField(default=False)),
                ('publish_date', models.DateField()),
                ('created_time', models.DateTimeField()),
                ('updated_time', models.DateTimeField()),
            ],
        ),
    ]
