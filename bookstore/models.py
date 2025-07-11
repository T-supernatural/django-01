from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField("Book Title", max_length=255)
    description = models.TextField("Description")
    price = models.PositiveIntegerField("Price (₦)", default=0)
    add_date = models.DateTimeField("Date Added", auto_now=True)
    cover = models.ImageField("Cover Image", upload_to="covers")

    def __str__(self):
        return self.title
    
