from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
DOWNLOAD_FOLDER = 'downloadables'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# homepage
@app.route('/')
def index():
    # Get a list of files in the upload folder
    files = os.listdir(app.config['DOWNLOAD_FOLDER'])
    return render_template('/static/index.html', files=files)

@app.route('/download/<filename>')
def download_file(filename):
    try:
        return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True)
    except FileNotFoundError:
        return "File not found", 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') # Run on all interfaces, for local network access