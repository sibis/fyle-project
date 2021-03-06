# Generated by Django 3.0.3 on 2020-02-11 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankBranches',
            fields=[
                ('ifsc', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('bank_name', models.CharField(max_length=49)),
                ('branch', models.CharField(max_length=74)),
                ('address', models.CharField(max_length=195)),
                ('city', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=26)),
            ],
            options={
                'db_table': 'bank_branches',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Banks',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=49)),
            ],
            options={
                'db_table': 'banks',
            },
        ),
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('ifsc', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('branch', models.CharField(max_length=74)),
                ('address', models.CharField(max_length=195)),
                ('city', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=26)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_information.Banks')),
            ],
            options={
                'db_table': 'branches',
            },
        ),
        migrations.AddIndex(
            model_name='banks',
            index=models.Index(fields=['id'], name='banks_id_pkey'),
        ),
        migrations.AddIndex(
            model_name='branches',
            index=models.Index(fields=['ifsc'], name='branches_ifsc_pkey'),
        ),
    ]
