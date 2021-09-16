from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ('-created',)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name


class Offer(models.Model):
    category = models.ForeignKey(
        Category, related_name='offer', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300, null=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = 'Offers'
        ordering = ('-created',)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name