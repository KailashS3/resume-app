from flask import Flask, render_template, make_response
from xhtml2pdf import pisa
import io

app = Flask(__name__)

@app.route("/")
def index():
    # Show your resume page
    return render_template("index.html")

@app.route("/download")
def download_resume():
    # Render the same HTML template
    html = render_template("index.html")

    # Convert HTML → PDF
    pdf = io.BytesIO()
    pisa.CreatePDF(html, dest=pdf)

    # Serve PDF inline
    response = make_response(pdf.getvalue())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=resume.pdf'
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

