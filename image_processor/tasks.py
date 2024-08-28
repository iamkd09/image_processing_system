from celery import shared_task
from PIL import Image as PILImage
from django.core.files.base import ContentFile
from .models import Image
import requests
from io import BytesIO

@shared_task
def process_images(image_id):
    image = Image.objects.get(id=image_id)
    response = requests.get(image.input_url)
    img = PILImage.open(BytesIO(response.content))
    
    # Compress image
    buffer = BytesIO()
    img.save(buffer, format='JPEG', quality=50)
    
    # Save compressed image (e.g., to a file storage service)
    image.output_url = "compressed_image_url"  # Placeholder, save the image as per your storage method
    image.status = 'processed'
    image.save()
