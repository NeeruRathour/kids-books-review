from django import template
from kidsbooks.models import Rating  

register = template.Library()

@register.filter
def rating_for_book(user, book_id):
    try:
        return user.ratings.get(book_id=book_id).rating
    except Rating.DoesNotExist:
        return ""
