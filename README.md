# 😜 Freak Detector

**Freak Detector** is a fun real-time AI app that uses your webcam to detect when you **stick your tongue out** 😝 or **close your eyes** 😴 — and flashes matching GIFs or images in a **separate reaction window** as long as you maintain that expression.

It’s powered by [MediaPipe Face Mesh](https://developers.google.com/mediapipe) for landmark detection and [OpenCV](https://opencv.org/) for video processing.

---

## 🎮 Demo

> 👀 The app opens two windows:
>
> * **Freak Detector:** your live webcam feed
> * **Reaction:** shows GIFs or images based on your expression

Press **Q** anytime to close both windows.

---

## 🧬 Features

* 🎥 Real-time webcam tracking
* 😝 Detects **tongue out**
* 😴 Detects **eyes closed**
* 🪟 Shows reaction GIFs in a separate window
* ⚙️ Simple setup, no external AI API required

---

## 📦 Requirements

* **Python 3.12.x** (⚠️ `mediapipe` doesn’t support Python 3.13 yet)
* A **webcam**
* Works on **Windows**, **macOS**, and **Linux**

---

## 🗂️ Folder Structure

```
Freak-Detector/
│
├── assets/
│   ├── tongue.gif
│   ├── closed_eyes.gif
│
├── output/
│
├── main.py
└── README.md
```

---

## 🚀 How To Use 

### 1️⃣ Clone the Repository
Open the Terminal app CMD/Powershell and type: 

```bash
git clone https://github.com/masifislamm/Freak-Detector
cd Freak-Detector
```

### 2️⃣ Install Python 3.12

Download from the official site:
🔗 [https://www.python.org/downloads/release/python-3126/](https://www.python.org/downloads/release/python-3126/)
During installation:

* ✅ Check **“Add Python 3.12 to PATH”**
* Then click **Install Now**

Verify:

```bash
python --version
```

---

### 3️⃣ Create a Virtual Environment
Once done typle this command: 
```bash
python -m venv .venv
```

Activate it:

* **Windows:**

  ```bash
  .venv\Scripts\activate
  ```
* **Mac/Linux:**

  ```bash
  source .venv/bin/activate
  ```

---

### 4️⃣ Install Dependencies

With your environment activated:



```bash
pip install opencv-python mediapipe imageio numpy
```

---

### 5️⃣ Run the App

```bash
python main.py
```

Two windows will appear:

* 🎥 `Freak Detector` → your camera feed
* 🪟 `Reaction` → the GIF or image that matches your face action

Press **Q** to quit.

---

## 🧠 Customize GIFs

Replace the files in the **`assets/`** folder:

| Expression  | File Name         | Notes               |
| ----------- | ----------------- | ------------------- |
| Tongue out  | `tongue.gif`      | Any funny/silly GIF |
| Eyes closed | `closed_eyes.gif` | Sleepy or calm GIF  |

You can use `.jpg`, `.png`, or `.mp4` files too — just rename and adjust the code paths.

---

## 💾 requirements.txt Example

If you want to make your own:

```
opencv-python
mediapipe
imageio
numpy
```

Then users can just run:

```bash
pip install -r requirements.txt
```

---

## ⚙️ One-Click Run (Windows)

Create a **`run.bat`** file in the project folder:

```bat
@echo off
call .venv\Scripts\activate
python main.py
pause
```

Double-click `run.bat` to launch Freak Detector easily.

---

## 🧮 Troubleshooting

| Problem                                    | Fix                                                        |
| ------------------------------------------ | ---------------------------------------------------------- |
| ❌ `No matching distribution for mediapipe` | You’re using Python 3.13 — install 3.12.                   |
| 🖼️ GIF not showing                        | Check that the GIFs exist in `assets/` with correct names. |
| 🎥 Camera not opening                      | Make sure no other app (Zoom, Discord, etc.) is using it.  |
| 🪞 Reaction window too small               | Resize it manually or change resolution in code.           |

---

## 💡 Future Ideas

* 🔊 Add sound effects for each reaction
* 🧠 Connect GPT or Gemini for smart captions
* 📈 Log emotions or create a timeline
* 🌐 Launch reactions in a browser tab

---

## 👨‍💻 Author

**Md Asif Islam**
🧠 Software Engineer & AI Developer
🇲🇾by Based in Malaysia
📧 [GitHub Profile](https://github.com/masifislamm)

---

## 🪪 License

This project is open-source under the **GPL License**.
Feel free to fork, modify, and have fun with it!

---

### ⭐ Don’t forget to star the repo if you li
