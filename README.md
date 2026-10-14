# Photo to Pencil Sketch 🎨

A simple Python project that converts a normal photograph into a pencil sketch using **OpenCV**.

## ✨ Features

- Convert color images into grayscale.
- Apply image inversion and Gaussian blur.
- Generate a pencil-sketch effect.
- Save the output as `sketch.jpg`.

## 🛠️ Technologies Used

- Python
- OpenCV
- Image Processing

## 📁 Project Structure

```text
photo-to-pencil-sketch/
├── sketch.py
├── photo.jpg
├── requirements.txt
├── sketch.jpg
├── .gitignore
└── README.md
```

## 🚀 Installation and Usage

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/photo-to-pencil-sketch.git
cd photo-to-pencil-sketch
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your image

Place an image named `photo.jpg` in the project folder.

### 4. Run the program

```bash
python sketch.py
```

### 5. View the output

The generated pencil sketch will be saved as `sketch.jpg`.

## ⚙️ How It Works

1. Load the input image using OpenCV.
2. Convert the image to grayscale.
3. Invert the grayscale image.
4. Apply Gaussian blur to the inverted image.
5. Divide the grayscale image by the inverted blurred image to create the sketch effect.
6. Save the resulting image.

## 📌 Future Improvements

- Add a graphical user interface.
- Support multiple image formats.
- Allow users to adjust sketch intensity.
- Add before-and-after image previews.

## 👨‍💻 Author

Your Name

## 📄 License

This project is open-source and available under the MIT License.
