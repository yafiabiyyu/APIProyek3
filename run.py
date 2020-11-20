import os
from app import create_app

config_name = os.getenv("FLASK_ENV")
app = create_app(config_name)
port = os.getenv('PORT')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)