# Generated by Django 2.1.3 on 2018-11-05 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('showroom', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='seats',
        ),
        migrations.AddField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='showroom.Brand'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='manufacturer',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='showroom.Manufacturer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
    ]
