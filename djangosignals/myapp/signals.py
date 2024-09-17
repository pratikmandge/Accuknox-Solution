from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import MyModel
import threading
import logging
from django.db import transaction

logger = logging.getLogger(__name__)


@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    # Log thread information and transaction status
    logger.info(f"Signal handler running in thread: {threading.current_thread().name}")
    logger.info(f"Transaction in progress: {transaction.get_connection().in_atomic_block}")

    # Simulate some processing
    print(f"Signal handler executed: {instance.name}")
