# Image Processing System

This project is a backend system designed to process image data from CSV files. The system validates, processes, and stores images, providing APIs to interact with the processed data.

## Features

- **Upload CSV**: Accepts a CSV file containing product names and image URLs.
- **Image Processing**: Asynchronously compresses images by 50% of their original quality.
- **Status API**: Allows users to query the processing status using a request ID.
- **Database Integration**: Stores processed image data and associated product information.
- **Optional Webhook**: Can trigger a webhook after processing all images (Bonus Feature).

## Tech Stack

- **Python**
- **Django**: Web framework
- **Celery**: Task queue for asynchronous processing
- **Redis**: Message broker for Celery
- **PostgreSQL/MySQL/SQLite**: Database (Choose as per your preference)
- **Pillow**: Image processing library

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

- Python 3.x
- Virtualenv
- Redis (for Celery)
- MySQL
