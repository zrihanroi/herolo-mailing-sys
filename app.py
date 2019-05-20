from flask import Flask
from endpoints.endpoints import endpoints

app = Flask(__name__)
app.register_blueprint(endpoints)

if __name__ == "__main__":
    print "Starting server"
    app.run(port = 4200)