from flask import Flask, render_template, send_from_directory
import os
from flask import *

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
DOWNLOAD_FOLDER = 'downloadables'
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# homepage
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movies')
def movies():
    files = os.listdir(app.config['DOWNLOAD_FOLDER']+'/movies/')
    return render_template('movies.html', files=files)

@app.route('/shows')
def shows():
    files = os.listdir(app.config['DOWNLOAD_FOLDER']+'/shows/')
    return render_template('shows.html', files=files)

@app.route('/misc')
def misc():
    files = os.listdir(app.config['DOWNLOAD_FOLDER']+'/misc/')
    return render_template('misc.html', files=files)

@app.route('/download/<category>/<filename>')
def download_file(filename, category):
    try:
        return send_from_directory(os.path.join(app.config['DOWNLOAD_FOLDER'], category), filename, as_attachment=True)
    except FileNotFoundError:
        return "File not found", 404

# uploads
@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'GET':
        return render_template('upload.html')
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return "File uploaded successfully"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') # Run on all interfaces, for local network access