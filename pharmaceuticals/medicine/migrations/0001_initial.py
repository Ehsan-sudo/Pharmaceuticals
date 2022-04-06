# Generated by Django 4.0.3 on 2022-04-03 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('location', models.TextField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.company')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=100, unique=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('debt', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.customer')),
            ],
        ),
        migrations.CreateModel(
            name='MedicineType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100, unique=True)),
                ('medical_name', models.CharField(max_length=100, null=True)),
                ('formula', models.TextField(max_length=300, null=True)),
                ('expire_date', models.DateField()),
                ('unit_price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.medicinetype')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerPurchaseMedicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('unit_price', models.FloatField()),
                ('medicine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.medicine')),
                ('purchase_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.customerpurchase')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('payed_amount', models.FloatField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.customer')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyPurchaseMedicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('unit_price', models.FloatField()),
                ('medicine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.medicine')),
                ('purchase_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.companypurchase')),
            ],
        ),
    ]