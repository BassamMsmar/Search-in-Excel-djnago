# Generated by Django 5.0.6 on 2024-05-16 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='excel_files')),
                ('file_name', models.CharField(blank=True, max_length=100, null=True)),
                ('creation_time', models.DateTimeField(blank=True, null=True)),
                ('modification_time', models.DateTimeField(blank=True, null=True)),
                ('sheet_names', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(max_length=100)),
                ('receipt_number', models.CharField(max_length=100)),
                ('driver_name', models.CharField(max_length=100)),
                ('fare', models.IntegerField()),
                ('destination', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('shipment_number', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=200)),
                ('date', models.DateField(max_length=100)),
            ],
        ),
    ]
