#Harry Potter Invisibility Cloak 🧙‍♂️🪄

A fun computer vision project that makes a red cloak “invisible” in real-time, inspired by Harry Potter’s Invisibility Cloak.

Demo

<img width="1673" height="709" alt="image" src="https://github.com/user-attachments/assets/f18540b2-1c33-4369-8e31-9cbb7a437646" />


Description

This project uses Python and OpenCV to create an augmented reality invisibility effect.

Detects a red cloak in the video feed.

Replaces the cloak area with the background.

Creates the effect that the person wearing the cloak is invisible.

This is a beginner-friendly project that demonstrates:

Color detection in HSV color space

Masking and bitwise operations

Morphological operations to clean masks

Real-time video processing

Requirements

Python 3.x

OpenCV

NumPy

Install dependencies using pip:

pip install opencv-python numpy

How to Run

Clone the repository:

git clone https://github.com/basmalaamamdouh/Harry-Potter-Invisibility-Cloak


Run the script:

python invisibility_cloak.py


Instructions:

Make sure the webcam is working.

Keep the cloak fully red for best results.

Wait a few seconds at the start for the background capture.

Press 'q' to exit the program.

How It Works

Captures a frame of the background before you enter the frame.

Detects the red cloak using HSV color range.

Creates a mask to separate the cloak from the rest of the frame.

Replaces the cloak area with the background.

Combines everything to create the invisibility effect in real-time.

Future Improvements

Detect any colored cloak (not just red).

Make the cloak semi-transparent or add virtual effects.

Use deep learning for more robust cloak detection in complex backgrounds.

Credits

Inspired by the Harry Potter Invisibility Cloak

Uses OpenCV and NumPy
