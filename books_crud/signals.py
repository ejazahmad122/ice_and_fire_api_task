from django.db.models.signals import post_save
from django.dispatch import receiver
from books_crud.models import BookShelf


@receiver(post_save, sender=BookShelf)
def update_description(sender, **kwargs):
    """This signal update the description of the book

    Args:
        sender (model): model where signal is calling
    """
    username = 'AnonymousUser'
    import inspect
    for frame_record in inspect.stack():
        if frame_record[3] == 'get_response':
            request = frame_record[0].f_locals['request']
            break
    else:
        request = None
    if request:
        username = request.user

    is_created = kwargs['created']
    instance = kwargs['instance']
    if is_created:
        message = f"This book is created by {username}"
    else:
        message = f"This book is updated by {username}"
    BookShelf.objects.filter(id=instance.id).update(description=message)
