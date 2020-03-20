# Generated by Django 2.1.1 on 2020-03-16 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200316_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addr', models.CharField(max_length=32)),
                ('tel', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='state',
        ),
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='api.Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='publish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Publish'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='publish',
            name='email',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='publish',
            name='name',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='ad',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.AuthorDetail'),
        ),
    ]