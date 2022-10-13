# Generated by Django 4.0.3 on 2022-05-19 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=120, verbose_name='name')),
                ('body', models.CharField(db_index=True, max_length=500, verbose_name='body')),
                ('like_count', models.IntegerField(verbose_name='Like_Count')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created DateTime')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Created DateTime')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.item')),
            ],
            options={
                'db_table': 'review',
            },
        ),
    ]
