from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import Group
from .models import User

@receiver(post_save, sender=User)
def user_post_save(sender, **kwargs):
    if settings.IS_THERAPY_DEMOSITE:
        g = Group.objects.get_or_create(name=settings.THERAPY_DEFAULT_GROUP)
        kwargs['instance'].groups.add(g[0].pk)


