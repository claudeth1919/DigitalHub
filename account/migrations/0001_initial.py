# Generated by Django 2.2.3 on 2019-08-06 03:42

from django.db import migrations, models


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
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=3, max_digits=11)),
                ('balance', models.DecimalField(decimal_places=3, max_digits=11)),
                ('owner', models.IntegerField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromAccount', models.IntegerField()),
                ('toAccount', models.IntegerField()),
                ('amount', models.DecimalField(decimal_places=3, max_digits=11)),
                ('sentAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]