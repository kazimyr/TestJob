# Generated by Django 4.2.10 on 2024-03-02 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("training_systems", "0002_alter_lesson_product_id_alter_lesson_video_link"),
    ]

    operations = [
        migrations.RenameField(
            model_name="group",
            old_name="product_id",
            new_name="product",
        ),
        migrations.RenameField(
            model_name="lesson",
            old_name="product_id",
            new_name="product",
        ),
    ]