from django.urls import path
from image_processor.views import upload_csv, check_status

urlpatterns = [
    path('upload/', upload_csv, name='upload_csv'),
    path('status/<int:product_id>/', check_status, name='check_status'),
]


