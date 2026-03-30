# Computer-Vision-Project
This is a Face Detection Model
# 🎯 Face Detection with OpenCV

A simple face detection project using OpenCV's Haar Cascade classifier. Runs directly in **Google Colab** — no GPU or local setup required.

---

## 📋 Project Overview

| Property       | Details                          |
|----------------|----------------------------------|
| Language       | Python 3                         |
| Library        | OpenCV (`opencv-python-headless`)|
| Method         | Haar Cascade Classifier          |
| Platform       | Google Colab                     |
| GPU Required   | ❌ No — runs on CPU              |

---

## 🚀 How to Run in Google Colab

1. Go to [colab.research.google.com](https://colab.research.google.com)
2. Create a new notebook
3. Copy and paste the code from `face_detection_colab.py` into a cell
4. Click **Run** (Shift + Enter)
5. Upload your image when prompted
6. View the result and download it

---

## 📁 Files

```
face_detection/
├── face_detection_colab.py   # Main script to run in Google Colab
└── README.md                 # This file
```

---

## ⚙️ How It Works

```
Input Image
     │
     ▼
Convert to Grayscale
     │
     ▼
Histogram Equalization (improves contrast)
     │
     ▼
Haar Cascade Detection
     │
     ▼
Draw Bounding Boxes
     │
     ▼
Display + Download Result
```

1. **Upload** — Upload any image containing human faces
2. **Grayscale** — Image is converted to grayscale for faster processing
3. **Equalization** — Contrast is improved to handle dark/bright lighting
4. **Detection** — Haar Cascade scans the image at multiple scales
5. **Output** — Green boxes are drawn around detected faces

---

## 🔧 Detection Parameters

You can tune these values in the code:

| Parameter       | Default | Effect                                      |
|-----------------|---------|---------------------------------------------|
| `scaleFactor`   | `1.1`   | How much to shrink image each scan pass     |
| `minNeighbors`  | `8`     | Higher = stricter, fewer false positives    |
| `minSize`       | `(60,60)` | Minimum face size to detect (pixels)     |

### Tuning Tips

| Problem                  | Fix                              |
|--------------------------|----------------------------------|
| Missing real faces       | Lower `minNeighbors` (e.g. `5`) |
| Too many false detections| Raise `minNeighbors` (e.g. `10`)|
| Missing small faces      | Lower `minSize` (e.g. `30, 30`) |
| Detecting tiny fake faces| Raise `minSize` (e.g. `80, 80`) |

---

## ⚠️ Known Limitations

- Works best on **front-facing faces** (not side profiles)
- May struggle with **very dark or overexposed images**
- Bright light sources (like ceiling lights) can sometimes cause **false positives** — increase `minNeighbors` to fix
- Not suitable for real-time video in Colab (no webcam access)

---

## 📦 Dependencies

```
opencv-python-headless
matplotlib
```

Install with:
```bash
pip install opencv-python-headless matplotlib
```

> These are auto-installed by the script in Colab.

---

## 📊 Example Output

- ✅ Green rectangle drawn around each detected face
- ✅ Label "Face" shown above each box
- ✅ Total face count displayed in the top-left corner
- ✅ Result saved as `result.jpg` and downloaded automatically

---

## 📄 License

This project is for educational purposes. OpenCV is licensed under the [Apache 2.0 License](https://opencv.org/license/).
