# Generated by Django 4.2.5 on 2023-10-15 19:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0003_alter_articulo_autor_alter_articulo_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='texto',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
