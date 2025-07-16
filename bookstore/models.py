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
    
class BookImage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)

    def __str__(self):
        return f"Image for {self.book.title}"
    