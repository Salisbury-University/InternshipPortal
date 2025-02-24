# Internship Portal Web App
# main.py for API


"""
Clients: Dr. Joseph Anderson, Dr. Giulia Franchi
Team: Blaine Mason, Jacob Duncan, Justin Ventura, Margaret Finnegan

Run this: `python3 main.py` in order to start flask app.
To stop: ctrl+C to interrupt program.
"""

# Import the API app creation:
from api import create_app


# This is the flask app:
app = create_app()


# Main function:
def _main():
    app.run(debug=True)


# Run the script directly:
if __name__ == '__main__':
    _main()
    print('end of main.py')
