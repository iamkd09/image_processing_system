import csv
import io
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product, Image
from .tasks import process_images

@csrf_exempt  # Allow POST requests without CSRF token for simplicity; consider removing in production.
def upload_csv(request):
    if request.method == 'POST':
        if 'file' not in request.FILES:
            return JsonResponse({"error": "No file uploaded."}, status=400)
        
        file = request.FILES['file']
        decoded_file = file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        reader = csv.reader(io_string)
        
        # Skip header
        next(reader)

        for row in reader:
            product_name = row[1]
            image_urls = row[2].split(',')

            # Create or get the product
            product, created = Product.objects.get_or_create(name=product_name)

            for url in image_urls:
                # Create image entry and enqueue image processing task
                image = Image.objects.create(product=product, input_url=url)
                process_images.delay(image.id)

        return JsonResponse({"message": "CSV file uploaded successfully."}, status=201)

    return JsonResponse({"error": "Only POST requests are allowed."}, status=405)

def check_status(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        images = product.images.all()
        statuses = {image.input_url: image.status for image in images}
        return JsonResponse(statuses, status=200)
    except Product.DoesNotExist:
        return JsonResponse({"error": "Product not found."}, status=404)
