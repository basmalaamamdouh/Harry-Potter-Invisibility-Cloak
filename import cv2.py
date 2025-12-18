import cv2
import numpy as np
import time

# Initialize webcam
cap = cv2.VideoCapture(0)
time.sleep(2)  # Give the camera some time to warm up

# Capture background (empty scene)
ret, background = cap.read()
background = np.flip(background, axis=1)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = np.flip(frame, axis=1)  # Flip horizontally

    # Apply Gaussian blur to reduce noise
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)

    # Convert to HSV color space
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    # Define red color range (two parts due to HSV wraparound)
    lower_red1 = np.array([0, 100, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 100, 50])
    upper_red2 = np.array([180, 255, 255])

    # Create masks for red
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2

    # Refine the mask (remove noise and fill gaps)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))

    # Create inverted mask for the rest of the frame
    inverse_mask = cv2.bitwise_not(mask)

    # Segment the cloak area from background
    cloak_area = cv2.bitwise_and(background, background, mask=mask)
    # Segment the rest of the frame
    rest_of_frame = cv2.bitwise_and(frame, frame, mask=inverse_mask)

    # Combine both to create the final output
    final_output = cv2.addWeighted(cloak_area, 1, rest_of_frame, 1, 0)

    # Display the output
    cv2.imshow('Harry Potter Cloak', final_output)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
