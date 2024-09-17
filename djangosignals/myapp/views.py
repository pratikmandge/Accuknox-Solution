from django.shortcuts import render
from myapp.models import MyModel
import threading
import logging

# Create your views here.

logger = logging.getLogger(__name__)


def my_view(request):
    logger.info(f"View running in thread: {threading.current_thread().name}")
    # This will trigger the signal handler
    instance = MyModel.objects.create(name="test")
    return render(request, "template.html")
