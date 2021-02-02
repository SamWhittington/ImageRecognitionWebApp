from flask import Flask

UPLOAD_FOLDER = 'C:/Users/SamWh/Hex/TestApp/Uploads'

app = Flask(__name__)
app.secret_key = "hEx2o21"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER # Change this? 