# Generated by Django 5.0.1 on 2024-02-12 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0006_alter_daysaving_april_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='amount_deposited',
            field=models.IntegerField(default=0, max_length=12),
            preserve_default=False,
        ),
    ]