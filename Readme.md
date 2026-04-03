# TruFor Splicing Detector — Hugging Face Space API Client (Windows + macOS)

This project calls a **Hugging Face Gradio Space** that runs the **TruFor splicing/manipulation detection model**.  
Given an input image, the API returns:

- **Global Score** (overall manipulation likelihood)
- **Anomaly Map** (localization heatmap)
- **Confidence Map** (per-pixel confidence)

The Space is hosted at:

- **Space UI / Base URL:** `https://123sashank12-trufor-splicing-detecto.hf.space`
- **Space ID for gradio_client:** `123Sashank12/trufor-splicing-detecto`

---

## Requirements

- Python **3.9+** recommended (works on Windows/macOS)
- Internet access to reach Hugging Face Space
- An input image file (e.g., `.jpg`, `.jpeg`, `.png`)

---

## 1) Setup (Windows)

### A) Create and activate a virtual environment
Open PowerShell:

```powershell
cd "C:\path\to\your\project"
python -m venv trufor_env
.\trufor_env\Scripts\Activate.ps1
```

### B) Install dependency
```powershell
python -m pip install --upgrade pip
python -m pip install gradio_client
```

---

## 2) Setup (macOS)

### A) Create and activate a virtual environment
Open Terminal:

```bash
cd /path/to/your/project
python3 -m venv trufor_env
source trufor_env/bin/activate
```

### B) Install dependency
```bash
python -m pip install --upgrade pip
python -m pip install gradio_client
```

---

## 3) Client Script (Cross-platform)

Create a file named `test_api.py`:

```python
from gradio_client import Client, handle_file

# Hugging Face Space ID (owner/space_name)
SPACE_ID = "123Sashank12/trufor-splicing-detecto"

client = Client(SPACE_ID)

# --- Set your local image path below ---
# Windows example:
# img_path = r"C:\Users\YourName\Desktop\sample5.jpeg"
#
# macOS example:
# img_path = "/Users/yourname/Desktop/sample5.jpeg"

img_path = "PUT_YOUR_IMAGE_PATH_HERE"

score, anomaly_img, confidence_img = client.predict(
    handle_file(img_path),
    api_name="/predict",
)

print("Score:", score)
print("Anomaly:", anomaly_img)
print("Confidence:", confidence_img)
```

### Important
- On **Windows**, it’s best to use a raw string (prefix with `r"..."`) for paths.
- On **macOS**, use standard Unix paths like `"/Users/.../image.jpg"`.

---

## 4) Run the client

### Windows
```powershell
python test_api.py
```

### macOS
```bash
python test_api.py
```

---

## 5) Understanding the output

The script prints:
- `Score:` a float value
- `Anomaly:` returned file info (often a path or a dict with a downloadable file path)
- `Confidence:` returned file info (same format)

Depending on your installed `gradio_client` version, the returned images might be:
- a **local downloaded file path** (string), or
- a **dictionary** (e.g., `{"path": "...", ...}`)

If you want to automatically save the outputs with consistent names, tell me what your printed output looks like and I’ll provide a small helper function that saves the returned anomaly/confidence images.

---

## 6) Troubleshooting

### A) Validation error about ImageData
If you see an error like:
`Input should be a valid dictionary or instance of ImageData`

Make sure you are using:
```python
handle_file(img_path)
```
and not passing the image path string directly.

### B) Space is sleeping / first request is slow
On the free plan, Spaces can go to sleep when idle. The first request after sleep may take longer.

### C) Wrong API name
If `/predict` changes in the Space code, you can inspect the available endpoints:

```python
from gradio_client import Client
client = Client("123Sashank12/trufor-splicing-detecto")
print(client.view_api())
```

---

## License / Notes
This client only calls the hosted Space API. Model performance and outputs depend on the TruFor model hosted in the Space.