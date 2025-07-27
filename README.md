# 🔊 Volume Hand Control

Control your system volume using **just your hand gestures** via webcam!  
This project uses **OpenCV**, **MediaPipe**, and **Python** to recognize your hand in real-time and adjust the volume level dynamically.

---

## 🎯 Features

- 🖐️ Real-time hand tracking using **MediaPipe**
- 📏 Distance between fingers controls volume
- 🎚️ Smooth and responsive volume adjustment
- 🧠 Intuitive UI overlay with feedback
- 💻 Works on Windows/Linux (with OS-specific audio control)

---

## 📹 How It Works

1. Uses your webcam to capture hand gestures
2. Detects landmarks like the **thumb** and **index finger**
3. Measures the distance between them
4. Maps that distance to system volume level
5. Updates volume in real time while showing feedback on screen

---

## 🛠️ Requirements

Install dependencies with pip:

bash
pip install opencv-python mediapipe numpy pycaw

Python 3.x

Webcam

For Windows: pycaw handles volume control

For Linux: use amixer or pulsectl (modify script)

🚀 Getting Started
Clone the repository:

bash
Copy
Edit
git clone https://github.com/rockers2232/Volume-Hand-Control.git
cd Volume-Hand-Control
Run the main script:

bash
Copy
Edit
python3 main.py
🎮 Controls
Gesture	Action
Thumb + Index finger far apart	Increase Volume
Thumb + Index finger close	Decrease Volume

Visual feedback on screen will show:

Volume Bar

Volume Percentage

FPS

Hand Tracking Status

## 📁 Project Structure

Volume Hand Control/
├── handcontrol.py # Main script to control volume
├── handtracking.py # Hand detection logic using MediaPipe
├── handtrackingmodule.py # Supporting module for hand tracking
├── venv/ # Python virtual environment (optional)
└── pycache/ # Auto-generated Python bytecode

📄 License
This project is licensed under the MIT License.

🙋‍♂️ Author
Ayush Saini
GitHub: @rockers2232
