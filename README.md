<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Josefin+Sans&pause=1000&color=9D00FF&center=true&vCenter=true&width=435&lines=Sign+Language+to+Speech+Conversion;Real-time+ASL+Recognition+System)](https://github.com/RhythmusByte/Sign-Language-to-Speech)

<img src="banner.png" alt="Project demonstration" width="100%"/>

[![License](https://img.shields.io/badge/License-BSD_3--Clause-8A2BE2.svg?style=for-the-badge)](https://opensource.org/licenses/BSD-3-Clause)
![Status](https://img.shields.io/badge/Status-Active_Development-8A2BE2?style=for-the-badge&logo=vercel)

</div>

---

## 🎯 Project Overview
Real-time American Sign Language (ASL) translation system using computer vision and deep learning. Combines custom hand tracking with gesture classification to create accessible communication solutions.

> 🔮 **Development Update:** Core functionality implemented - refining accuracy and expanding gesture library

---

## ✨ Key Features
- 🔮 Real-time hand detection & gesture tracking
- 🧠 CNN-based classification using TensorFlow/Keras
- 🔊 Simultaneous text & speech output

---

## 📊 Project Documentation

### Use Case Diagram
![Use Case Diagram](Use-Case.png)

### Data Flow Diagrams
| Level 0 | Level 1 | Level 2 |
|---------|---------|---------|
| ![DFD Level 0](DFD_0.png) | ![DFD Level 1](DFD_1.png) | ![DFD Level 2](DFD_2.png) |

---

## 🛠 Tech Stack
### **Core Technologies**
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-9D00FF?style=for-the-badge&logo=tensorflow&logoColor=white)

### **Supporting Libraries**
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![cvzone](https://img.shields.io/badge/cvzone-Community-9D00FF?style=for-the-badge)
![pyttsx3](https://img.shields.io/badge/pyttsx3-TTS_Engine-8B0000?style=for-the-badge)

---

## 📂 Repository Structure
```text
Sign-Language-to-Speech/
├── data/                  # Training datasets and gesture samples
├── Application.py        # Main application logic
├── trainedModel.h5       # Pretrained CNN model
├── requirements.txt      # Dependency specifications
└── white.jpg             # Background reference image
```

---

## 🚀 Installation Guide

### **Prerequisites**
- Python 3.9+ (Recommended)
- Webcam-enabled device
- 4GB+ RAM recommended

### **Setup Instructions**
1. Clone repository:
   ```bash
   git clone https://github.com/RhythmusByte/Sign-Language-to-Speech.git
   cd Sign-Language-to-Speech
   ```

2. Create virtual environment:
   ```bash
   python -m venv .venv
   ```

3. Activate environment:
   - Windows: `.venv\Scripts\activate`
   - Linux/MacOS: `source .venv/bin/activate`

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🖥 Usage
Launch the recognition system:
```bash
python Application.py
```

**System Flow:**
1. Webcam initialization
2. Hand detection & ROI extraction
3. Gesture preprocessing & normalization
4. CNN-based classification
5. Real-time text & speech output

---

## 📜 License
Distributed under BSD 3-Clause License. See [LICENSE](LICENSE).
