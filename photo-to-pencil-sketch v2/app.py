
from flask import Flask, render_template, request, Response
import cv2
import numpy as np

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/sketch", methods=["POST"])
def create_sketch():

    try:
        # Receive camera frame
        image_data = np.frombuffer(
            request.get_data(),
            dtype=np.uint8
        )

        img = cv2.imdecode(
            image_data,
            cv2.IMREAD_COLOR
        )

        if img is None:
            return "Invalid image", 400

        # Resize for faster processing
        img = cv2.resize(img, (640, 480))

        # Original pencil sketch algorithm
        gray = cv2.cvtColor(
            img, cv2.COLOR_BGR2GRAY
        )

        inverted = 255 - gray

        blurred = cv2.GaussianBlur(
            inverted, (21, 21), 0
        )

        inverted_blur = 255 - blurred

        sketch = cv2.divide(
            gray,
            inverted_blur,
            scale=256
        )

        # Encode sketch as JPG
        success, encoded = cv2.imencode(
            ".jpg", sketch
        )

        if not success:
            return "Image encoding failed", 500

        return Response(
            encoded.tobytes(),
            mimetype="image/jpeg"
        )

    except Exception as e:
        return str(e), 500


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
