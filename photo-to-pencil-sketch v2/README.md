# Live Photo-to-Pencil Sketch

A small Flask web application that turns your webcam feed into a live pencil-sketch effect. The browser captures camera frames and sends them to a Python backend, where OpenCV converts each frame to grayscale and applies a pencil-sketch filter. The processed image is then shown in the page, with an option to download the current sketch.

## Features

- Live webcam preview
- Real-time pencil-sketch conversion
- Start and stop camera controls
- Download the current sketch as a JPG

## Requirements

- Python 3
- A webcam and a browser that supports camera access

## Setup and run (Windows)

Open Command Prompt or PowerShell in this project folder (`photo-to-pencil-sketch v2`) and run:

```bat
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

> The dependency file in this repository is named `requirement.txt` (singular), so use that filename in the install command. If you rename it to `requirements.txt`, update the command accordingly.

When the server starts, open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser and allow camera access.

## Camera access

Click **Start Camera** to begin processing, **Stop Camera** to turn it off, and **Download Sketch** to save the current result. Camera access generally requires opening the app on `localhost` or a secure HTTPS origin.

## Project files

- `app.py` — Flask server and OpenCV image-processing endpoint
- `requirement.txt` — Python dependencies
- `templates/index.html` — Web interface and webcam capture logic
- `static/` — Static assets such as stylesheets
