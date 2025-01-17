# Generated by Django 3.2.16 on 2024-09-23 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('icon', models.CharField(max_length=255)),
                ('status', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'categories',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('team_one_id', models.PositiveIntegerField()),
                ('team_two_id', models.PositiveIntegerField()),
                ('league_id', models.PositiveIntegerField()),
                ('slug', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('start_time', models.DateTimeField()),
                ('bet_start_time', models.DateTimeField(blank=True, null=True)),
                ('bet_end_time', models.DateTimeField(blank=True, null=True)),
                ('status', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'games',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('category_id', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=40)),
                ('short_name', models.CharField(max_length=40)),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'leagues',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('question_id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('odds', models.DecimalField(decimal_places=8, max_digits=28)),
                ('status', models.PositiveIntegerField()),
                ('locked', models.IntegerField()),
                ('winner', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'options',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.PositiveIntegerField()),
                ('locked', models.IntegerField()),
                ('result', models.PositiveIntegerField()),
                ('refund', models.PositiveIntegerField()),
                ('amount_refunded', models.IntegerField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'questions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('short_name', models.CharField(blank=True, max_length=40, null=True)),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'teams',
                'managed': False,
            },
        ),
    ]
