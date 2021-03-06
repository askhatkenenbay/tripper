# Generated by Django 3.1.6 on 2021-03-20 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210320_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='trip_id',
            field=models.AutoField(db_column='trip_id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tripfollower',
            name='trip',
            field=models.ForeignKey(db_column='trip_id', on_delete=django.db.models.deletion.DO_NOTHING, to='main.trip'),
        ),
    ]
