#🎓 Student Engagement Detection using Emotion Recognition

This project uses a webcam to analyze students' facial expressions in real time using DeepFace, classifies their emotions, and maps them to corresponding engagement levels. The data is stored every few minutes in a CSV file for future analysis and improvement in online education systems.
📌 Features

    ✅ Real-time webcam-based face emotion detection using DeepFace

    ✅ Maps emotion to an engagement level (High, Moderate, Low)

    ✅ Saves timestamped engagement data to a CSV file

    ✅ Displays live camera feed with emotion and engagement level overlay

    ✅ Useful for analyzing student behavior in e-learning environments

🧠 Emotion to Engagement Mapping
Emotion	Engagement Level
Happy	High
Surprise	High
Neutral	Moderate
Sad	Low
Fear	Low
Angry	Low
Disgust	Low
📁 Project Structure

student-engagement-emotion/
│
├── engagement_data.csv        # Stores timestamped emotion and engagement logs
├── engagement_analysis.py     # Main application file 
├── README.md                  # Project documentation

🚀 Getting Started
🔧 Prerequisites

Make sure you have Python installed. Then install the required packages:

pip install opencv-python deepface

▶️ Run the Project

python engagement_analysis.py 

The webcam will launch and begin real-time emotion detection. Press q to stop.
📝 Output

    Live feed with:

        Dominant Emotion

        Engagement Level

    CSV File: engagement_data.csv with columns:

        Timestamp

        Detected Emotion

        Engagement Level

💡 Use Cases

    Student engagement monitoring in online learning platforms

    Remote proctoring assistance

    User mood analytics for UX studies

🛡️ Disclaimer

This tool uses facial expressions as a proxy for engagement and may not reflect actual cognitive involvement. Use it as a support tool, not a sole indicator.
📌 Future Improvements

    Support for multiple face tracking

    Deep learning-based engagement prediction

    Integration with online classroom platforms (e.g., Zoom, Google Meet)

📷 Sample Output

Emotion: happy
Engagement: High

👨‍💻 Author

Arun Shakthi
If you use this code or project idea, feel free to give credit!
