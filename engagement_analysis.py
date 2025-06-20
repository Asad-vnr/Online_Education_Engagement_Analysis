


import cv2
import csv
import time
from datetime import datetime
from deepface import DeepFace

# Initialize webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# CSV file to save engagement data
csv_file = "engagement_data.csv"
fieldnames = ["Timestamp", "Emotion", "Engagement_Level"]

# Create or open the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()  # Write the header only once

# Function to map emotions to engagement levels
def get_engagement_level(emotion):
    engagement_map = {
        "happy": "High",
        "surprise": "High",
        "neutral": "Moderate",
        "sad": "Low",
        "fear": "Low",
        "angry": "Low",
        "disgust": "Low",
    }
    return engagement_map.get(emotion.lower(), "Unknown")

# Timer for saving data every 10 minutes
last_save_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    try:
        # Analyze the frame for emotions
        analysis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

        # Check if the result is a list (multiple faces detected)
        if isinstance(analysis, list):
            analysis = analysis[0]  # Use the first face's analysis

        # Extract dominant emotion
        dominant_emotion = analysis.get('dominant_emotion', "Unknown")

        # Determine engagement level
        engagement_level = get_engagement_level(dominant_emotion)

        # Display emotion and engagement level on the frame
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, f"Emotion: {dominant_emotion}", (10, 50), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, f"Engagement: {engagement_level}", (10, 100), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Save engagement data every 10 minutes
        if time.time() - last_save_time >= 5: 
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(csv_file, mode='a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writerow({"Timestamp": timestamp, "Emotion": dominant_emotion, "Engagement_Level": engagement_level})
            last_save_time = time.time()  # Reset the timer

    except Exception as e:
        print(f"Emotion detection failed: {e}")
        dominant_emotion = "Unknown"
        engagement_level = "Unknown"
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, "Emotion: Unknown", (10, 50), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, "Engagement: Unknown", (10, 100), font, 1, (0, 0, 255), 2, cv2.LINE_AA)

    # Show the live camera feed
    cv2.imshow("Camera Feed", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
