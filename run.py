import os
from app import create_app

app = create_app()
 
os.environ['FLASK_ENV'] = 'development'
os.environ['FLASK_DEBUG'] = True

if __name__ == '__main__':
    app.run(debug=True)