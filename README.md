# 📄 Resume Web Application (Flask + xhtml2pdf)

A simple **Flask web application** that displays your resume in the browser and allows visitors to **download it as a PDF**.  
The app uses **xhtml2pdf** to convert your existing HTML template (`templates/index.html`) into a PDF dynamically.

## 📂 Project Structure
```
resume-app/
├─ app.py              # Flask application
├─ requirements.txt    # Python dependencies
├─ templates/
│    └─ index.html     # Resume HTML template
├─ static/
│    └─ style.css      # CSS styling for resume
├─ Dockerfile          # Container setup
└─ README.md           # Project documentation
```

## ⚙️ Requirements
- Python 3.11+
- Flask
- xhtml2pdf


## ▶️ Run Locally

1. **Clone the repo**:
   ```bash
   git clone git@github.com:KailashS3/resume-app.git
   cd resume-app
   ```
2. **Install dependencies:**
   ``` 
     pip install -r requirements.txt
   ```
3. **Start the app:**
    ```
       python app.py
    ```
4. **Open in browser:**
    ```
      http://localhost:8080/
    ```
## 🐳 Run with Docker
1. **Build the image:**

```bash
    docker build -t resume-app .
```    
2. **Run the container:**

```
    docker run -p 8080:8080 resume-app
```
3. **Access the app:**
```
    http://localhost:8080/
```

## 📖 Features

- Resume displayed via `templates/index.html`
- Styled with `static/style.css`
- Download Resume (PDF) button generates a PDF using `xhtml2pdf`
- Runs locally or inside Docker


## 📸 Screenshots

### Resume Home Page
<img width="480" height="240" alt="image" src="https://github.com/user-attachments/assets/c0ad00b4-5c3d-4721-8095-da780d9f8dcd" />

### Download Resume (PDF)
<img width="500" height="280" alt="image" src="https://github.com/user-attachments/assets/e2277717-1e78-4617-aae2-e23b98219664" />
