# Sign Language to Speech Conversion

This project focuses on real-time American Sign Language (ASL) to speech conversion, leveraging OpenCV and TensorFlow/Keras for hand gesture recognition. The application incorporates custom hand tracking, image preprocessing, and gesture classification to translate ASL into both text and speech output, with accessibility in mind.

> ⚠️ **Note:** This project is currently under development.

## Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/RhythmusByte/Sign-Language-to-Speech.git
cd sign-language-to-speech
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
```

### 3️⃣ Activate the Virtual Environment  
- **Windows**  
  ```bash
  venv\Scripts\activate
  ```
- **Linux/macOS**  
  ```bash
  source venv/bin/activate
  ```

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Features

- Real-time hand gesture detection and tracking
- Image preprocessing pipeline
- Machine learning-based gesture classification
- Support for basic ASL gestures (letters A-Z)

## Technical Stack

- Python 3.9+
- OpenCV (Computer Vision)
- TensorFlow/Keras (Machine Learning)
- cvzone (Hand Tracking)
- NumPy (Numerical Processing)
- pyttsx3 (Text-to-Speech)

## Project Structure

```text
project /
│
├── data/
├── Application.py
├── README.md
├── requirements.txt
├── trainedModel.h5
└── white.jpg
```

- **Application.py**: Main Python script that runs the application.
- **trainedModel.h5**: The trained model for gesture classification.
- **requirements.txt**: List of dependencies needed to run the project.
- **white.jpg**: Background image.

## Features in Development

- Real-time gesture recognition
- Image processing pipeline for gesture analysis
- Gesture classification with TensorFlow/Keras
- Text and speech output for gesture translation

## Development Status

This project is in active development. The current focus is on:

- Improving hand tracking accuracy.
- Expanding the gesture recognition dataset.
- Enhancing real-time performance.

## Requirements

To run this project, you need Python 3.9 or higher. Install the necessary dependencies by running:

```bash
pip install -r requirements.txt
```

Key packages required:

- opencv-python
- tensorflow
- numpy
- cvzone
- pyttsx3

## Usage

To run the application, execute the following:

```bash
python Application.py
```

This will launch the gesture recognition system using your webcam or camera device and convert recognized gestures into text and speech output.

## Future Improvements

- Expand support for more ASL gestures.
- Optimize performance for faster recognition.
- Improve model accuracy with additional training data.
