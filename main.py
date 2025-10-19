import cv2
import mediapipe as mp
import numpy as np
import imageio
import time
from pathlib import Path

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=True)

output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

# GIF paths
tongue_gif = "assets/tongue.gif"
closed_eyes_gif = "assets/closed_eyes.gif"

# Load GIFs
def load_gif(path):
    try:
        gif_frames = imageio.mimread(path)
        frames_bgr = [cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) for frame in gif_frames]
        return frames_bgr
    except Exception as e:
        print(f"Error loading GIF: {e}")
        return None

tongue_frames = load_gif(tongue_gif)
eyes_frames = load_gif(closed_eyes_gif)

def eye_aspect_ratio(landmarks, eye_indices):
    p1, p2, p3, p4, p5, p6 = [np.array([landmarks[i].x, landmarks[i].y]) for i in eye_indices]
    v1 = np.linalg.norm(p2 - p6)
    v2 = np.linalg.norm(p3 - p5)
    h = np.linalg.norm(p1 - p4)
    ear = (v1 + v2) / (2.0 * h)
    return ear

def mouth_aspect_ratio(landmarks):
    top = np.array([landmarks[13].x, landmarks[13].y])
    bottom = np.array([landmarks[14].x, landmarks[14].y])
    left = np.array([landmarks[78].x, landmarks[78].y])
    right = np.array([landmarks[308].x, landmarks[308].y])
    mar = np.linalg.norm(top - bottom) / np.linalg.norm(left - right)
    return mar

EYE_AR_THRESH = 0.20
MOUTH_AR_THRESH = 0.55

cap = cv2.VideoCapture(0)
frames_for_gif = []

reaction_mode = None
reaction_index = 0

print("Press Q to quit...")

while True:
    success, frame = cap.read()
    if not success:
        break
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0].landmark

        left_eye_idx = [33, 160, 158, 133, 153, 144]
        right_eye_idx = [263, 387, 385, 362, 380, 373]
        left_EAR = eye_aspect_ratio(landmarks, left_eye_idx)
        right_EAR = eye_aspect_ratio(landmarks, right_eye_idx)
        avg_EAR = (left_EAR + right_EAR) / 2.0
        mar = mouth_aspect_ratio(landmarks)

        eyes_closed = avg_EAR < EYE_AR_THRESH
        tongue_out = mar > MOUTH_AR_THRESH

        if eyes_closed:
            reaction_mode = "eyes"
            cv2.putText(frame, "hell nah", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        elif tongue_out:
            reaction_mode = "tongue"
            cv2.putText(frame, "freak of nature", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
        else:
            reaction_mode = None
            cv2.putText(frame, "Normal", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    # Display main camera feed
    cv2.imshow("Freak Detector", frame)

    # Reaction window
    if reaction_mode == "eyes" and eyes_frames:
        gif_frame = eyes_frames[reaction_index % len(eyes_frames)]
        cv2.imshow("Reaction", gif_frame)
        reaction_index += 1
    elif reaction_mode == "tongue" and tongue_frames:
        gif_frame = tongue_frames[reaction_index % len(tongue_frames)]
        cv2.imshow("Reaction", gif_frame)
        reaction_index += 1
    else:
        blank = np.zeros((200, 300, 3), dtype=np.uint8)
        cv2.putText(blank, "Not Freaky", (30, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (200,200,200), 2)
        cv2.imshow("Reaction", blank)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
