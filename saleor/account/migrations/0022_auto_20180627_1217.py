# Generated by Django 2.0.3 on 2018-06-27 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0021_unique_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('is_active', models.BooleanField(default=True)),
                ('addresses', models.ManyToManyField(blank=True, to='account.Address')),
                ('default_billing_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='account.Address')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='addresses',
        ),
        migrations.AddField(
            model_name='user',
            name='user_addresses',
            field=models.ManyToManyField(blank=True, to='account.Address'),
        ),
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='account.Company'),
        ),
    ]
