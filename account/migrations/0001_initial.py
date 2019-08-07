# Generated by Django 2.2.4 on 2019-08-07 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=3, max_digits=11)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=3, max_digits=11)),
                ('sentAt', models.DateTimeField(auto_now_add=True)),
                ('fromAccount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Account')),
                ('toAccount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_requests_to_account', to='account.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=3, max_digits=11)),
                ('balance', models.DecimalField(decimal_places=3, max_digits=11)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Account')),
            ],
        ),
    ]
