# Generated by Django 4.1.3 on 2022-11-24 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charge_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=200, null=True)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='time',
            new_name='charge_time',
        ),
        migrations.AddField(
            model_name='customer',
            name='charge',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='business_name',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='charge_management.business'),
        ),
    ]
