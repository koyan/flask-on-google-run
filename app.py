import os
import secrets
import logging

from flask import Flask
from views.user import user_bp
from views.upload import upload_bp
from extensions import login_manager
from celery_config import make_celery

app = Flask(__name__)

# Secret key generation
foo = secrets.token_urlsafe(16)
app.secret_key = foo

# Register blueprints
app.register_blueprint(user_bp)
app.register_blueprint(upload_bp)

# Initialize extensions
login_manager.init_app(app)

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level as per your need
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('app.log'),  # Log to a file
        logging.StreamHandler()  # Log to console
    ]
)
logger = logging.getLogger("my_app_logger")  # Use the same name when retrieving the logger

# Initialize Celery
# logger.info("Initializing Celery...")
celery = make_celery(app)
# logger.info("Celery initialized successfully!")


from tasks import fastqc_multiqc_files_async, upload_raw_file_to_storage_async, unzip_raw_file_async

    
if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=True, port=server_port, host='0.0.0.0')
