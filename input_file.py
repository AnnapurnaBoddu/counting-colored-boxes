import cv2
import numpy as np


def detect_colors(image_np):
    # Convert image to HSV color space
    hsv_image = cv2.cvtColor(image_np, cv2.COLOR_BGR2HSV)
    # Blue Color Range
    lower_blue = np.array([100, 70, 70])  # Adjusted lower bound for blue
    upper_blue = np.array([140, 255, 255])  # Upper bound for blue

    # Red Color Ranges (two ranges)
    lower_red_1 = np.array([0, 100, 100])  # Lower bound for red (first range)
    upper_red_1 = np.array([10, 255, 255])  # Upper bound for red (first range)

    lower_red_2 = np.array([170, 100, 100])  # Lower bound for red (second range)
    upper_red_2 = np.array([180, 255, 255])  # Upper bound for red (second range)

    # Yellow Color Range
    lower_yellow = np.array([20, 100, 100])  # Lower bound for yellow
    upper_yellow = np.array([30, 255, 255])  # Upper bound for yellow

    # Create masks for each color
    mask_blue = cv2.inRange(hsv_image, lower_blue, upper_blue)
    mask_red_1 = cv2.inRange(hsv_image, lower_red_1, upper_red_1)
    mask_red_2 = cv2.inRange(hsv_image, lower_red_2, upper_red_2)
    mask_yellow = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

    # Find contours for the blue boxes
    contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_red_1, _ = cv2.findContours(mask_red_1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_red_2, _ = cv2.findContours(mask_red_2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_yellow, _ = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Count the boxes
    count_blue = len(contours_blue)
    count_red = len(contours_red_1) + len(contours_red_2)  # Add counts from both red ranges
    count_yellow = len(contours_yellow)

    return {'Blue Boxes': count_blue, 'Red Boxes': count_red, 'Yellow Boxes': count_yellow}

    #print(f"Blue Boxes: {count_blue}, Red Boxes: {count_red}, Yellow Boxes: {count_yellow}")


