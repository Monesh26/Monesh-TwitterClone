import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Name')),
                ('body', models.CharField(blank=True, db_index=True, max_length=140, null=True, verbose_name='Body')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created DateTime')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
            ],
            options={
                'db_table': 'post',
            },
        ),
    ]
