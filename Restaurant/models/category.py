from django.db import models

class Category(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100, unique=True)

    is_visible = models.BooleanField(default=True)
    sort = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['sort']
        db_table = 'category'

    def __str__(self):
        return self.name