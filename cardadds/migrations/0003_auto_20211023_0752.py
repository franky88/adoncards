# Generated by Django 3.2.8 on 2021-10-22 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cardadds', '0002_alter_cardadd_ref_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='cardadd',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cardadds.cardcategory'),
        ),
    ]
