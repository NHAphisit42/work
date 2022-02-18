# Generated by Django 4.0.2 on 2022-02-14 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginrischest', '0006_remove_order_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('income', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('datetime', models.DateField()),
            ],
            options={
                'verbose_name': 'ยอดขาย',
                'verbose_name_plural': 'ข้อมูลยอดขาย',
                'db_table': 'income',
                'managed': True,
            },
        ),
    ]
