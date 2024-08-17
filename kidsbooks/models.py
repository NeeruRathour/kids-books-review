from django.db import models
from django.contrib.auth.models import User
from django.forms import IntegerField

# Create your models here.
class Kidsbook(models.Model):
    """
    Stores a single kids book entry related to :modle: =`auth.User`
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                             related_name='user_books')
    title = models.CharField(max_length=200, null=False,
                             blank=False, unique=True)
    author = models.CharField(max_length=200, null=False, blank=False)
    price = models.IntegerField()
    ages = models.IntegerField()
    image = models.CharField(max_length=200, default='defaultimageurl')
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Title:{self.title} | author:{self.author}"


class Review(models.Model):
    """
    Stores a single review entry related to :model:=`auth.User`
    and model:`Kidsbook`
    """
    book = models.ForeignKey(Kidsbook, on_delete=models.CASCADE,
                             related_name="kidsbook_reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="kidsbook_reviewers")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review: {self.content} by {self.user} for {self.book}"

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Kidsbook, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('user', 'book')  
    def __str__(self):
        return f"{self.user.username} rated {self.book.title} with {self.rating} stars"
