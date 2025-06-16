from flask import Flask, render_template_string, send_file
from fpdf import FPDF
from io import BytesIO

app = Flask(__name__)

ARTICLE_TEXT = """
As part of its efforts to achieve Oman Vision 2040, Microsoft plays a vital role in supporting the country's digital transformation.
Through various initiatives, Microsoft has contributed to developing digital skills, supporting education,
and enabling organizations to adopt cloud computing and artificial intelligence tools.
"""

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>Microsoft & Oman Vision 2040</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet" />
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
        body {
            font-family: 'Roboto', Arial, sans-serif;
            background: linear-gradient(135deg, #e0f0ff, #ffffff);
            margin: 0; padding: 40px;
            color: #222;
            direction: ltr;
            line-height: 1.6;
        }
        header {
            display: flex;
            align-items: center;
            gap: 20px;
            margin-bottom: 30px;
        }
        header img {
            width: 80px;
        }
        header h1 {
            color: #0078D4;
            font-weight: 700;
            font-size: 2.2rem;
            margin: 0;
        }
        main {
            max-width: 800px;
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        }
        main p {
            font-size: 1.1rem;
            margin-bottom: 25px;
        }
        iframe {
            border-radius: 10px;
            box-shadow: 0 6px 15px rgba(0,0,0,0.15);
            width: 100%;
            height: 400px;
            margin-bottom: 30px;
        }
        .btn-download {
            display: inline-flex;
            align-items: center;
            background-color: #0078D4;
            color: white;
            text-decoration: none;
            padding: 12px 22px;
            border-radius: 8px;
            font-weight: 600;
            font-size: 1rem;
            transition: background-color 0.3s ease;
            box-shadow: 0 5px 15px rgba(0,120,212,0.4);
        }
        .btn-download:hover {
            background-color: #005a9e;
        }
        .btn-download i {
            margin-left: 8px;
            font-size: 1.2rem;
        }
        footer {
            margin-top: 50px;
            text-align: center;
            color: #555;
            font-size: 0.9rem;
            font-style: italic;
        }
    </style>
</head>
<body>
    <header>
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Microsoft_logo_%282012%29.svg/320px-Microsoft_logo_%282012%29.svg.png" alt="Microsoft Logo" />
        <h1>Microsoft's Role in Supporting Oman Vision 2040 <i class="fa-solid fa-flag"></i></h1>
    </header>

    <main>
        <p>{{ article }}</p>

        <iframe
          src="https://www.youtube.com/embed/VqUPMMpJ-CI"
          title="Microsoft and Oman Vision 2040"
          allowfullscreen
        ></iframe>

        <a class="btn-download" href="/download-pdf">
            Download PDF Report <i class="fa-solid fa-file-pdf"></i>
        </a>
    </main>

    <footer>
        <p>Created by Faisal &nbsp; <i class="fa-regular fa-copyright"></i> 2025</p>
    </footer>
</body>
</html>
"""

class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.set_text_color(0, 120, 212)
        self.cell(0, 10, "Microsoft's Role in Supporting Oman Vision 2040", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.set_text_color(169, 169, 169)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, article=ARTICLE_TEXT)

@app.route('/download-pdf')
def download_pdf():
    pdf = PDFReport()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, ARTICLE_TEXT)

    pdf_buffer = BytesIO()
    pdf.output(pdf_buffer)
    pdf_buffer.seek(0)

    return send_file(pdf_buffer, as_attachment=True, download_name="OmanVision_Report.pdf")

if __name__ == '__main__':
    app.run(debug=True)
