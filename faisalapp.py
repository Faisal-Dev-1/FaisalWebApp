from flask import Flask, render_template_string

app = Flask(__name__)

html_content = """
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Microsoft and Oman Vision 2040</title>

  <!-- FontAwesome Icons -->
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet" />

  <style>
    body {
      margin: 0;
      font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
      background: #0a1f44;
      color: #eee;
      overflow-x: hidden;
      min-height: 100vh;
    }

    body::before {
      content: "";
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: radial-gradient(circle, #1e3c72 1px, transparent 1px);
      background-size: 40px 40px;
      animation: moveGrid 30s linear infinite;
      opacity: 0.15;
      z-index: 0;
    }

    @keyframes moveGrid {
      from { background-position: 0 0; }
      to { background-position: 40px 40px; }
    }

    .container {
      position: relative;
      z-index: 1;
      max-width: 900px;
      margin: auto;
      padding: 20px;
    }

    header {
      text-align: center;
      margin-bottom: 40px;
    }

    header h1 {
      font-size: 2.8rem;
      margin-bottom: 10px;
      color: #4fc3f7;
      text-shadow: 0 0 8px #2196f3;
    }

    header p {
      font-size: 1.2rem;
      color: #b0bec5;
    }

    .video-wrapper {
      position: relative;
      padding-bottom: 56.25%;
      height: 0;
      overflow: hidden;
      border-radius: 12px;
      box-shadow: 0 0 15px #2196f3;
      margin-bottom: 40px;
    }

    .video-wrapper iframe {
      position: absolute;
      top: 0; left: 0;
      width: 100%;
      height: 100%;
      border: none;
    }

    section.articles h2 {
      border-bottom: 2px solid #4fc3f7;
      padding-bottom: 8px;
      margin-bottom: 20px;
      font-weight: 700;
    }

    article {
      background: rgba(33, 150, 243, 0.15);
      border-radius: 10px;
      padding: 15px 20px;
      margin-bottom: 15px;
      transition: background-color 0.3s ease;
    }

    article:hover {
      background: rgba(33, 150, 243, 0.3);
    }

    article h3 {
      margin-top: 0;
      color: #82cfff;
    }

    article p {
      line-height: 1.5;
      margin-bottom: 8px;
    }

    article a {
      color: #03a9f4;
      text-decoration: none;
      font-weight: 600;
    }

    article a:hover {
      text-decoration: underline;
    }

    footer {
      margin-top: 50px;
      padding: 15px 0;
      border-top: 1px solid #4fc3f7;
      text-align: center;
      color: #81d4fa;
      font-size: 0.9rem;
    }

    footer a {
      color: #4fc3f7;
      text-decoration: none;
      font-weight: 600;
    }

    footer a:hover {
      text-decoration: underline;
    }

    @media (max-width: 600px) {
      header h1 {
        font-size: 2rem;
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>Microsoft’s Partnership with Oman Vision 2040</h1>
      <p>Empowering digital transformation and sustainable development in Oman</p>
    </header>

    <div class="video-wrapper">
      <iframe src="https://www.youtube.com/embed/5N6Ww85GUlo" title="Microsoft Oman Vision 2040" allowfullscreen></iframe>
    </div>

    <section class="articles">
      <h2>Latest Insights</h2>

      <article>
        <h3>Driving Innovation for Oman’s Future</h3>
        <p>Microsoft supports Oman’s Vision 2040 through initiatives in cloud computing, AI, and smart infrastructure to foster economic diversification and digital skills development.</p>
        <a href="https://news.microsoft.com/2021/03/15/microsoft-partners-with-oman-for-digital-transformation/" target="_blank" rel="noopener noreferrer">Read more</a>
      </article>

      <article>
        <h3>Accelerating Oman’s Digital Economy</h3>
        <p>Collaborations with the Omani government focus on building digital infrastructure and smart city projects, enabling innovation hubs and empowering local startups.</p>
        <a href="https://www.microsoft.com/en-om/transform" target="_blank" rel="noopener noreferrer">Read more</a>
      </article>
    </section>

    <footer>
      <p>Contact: <a href="mailto:faisal.alsukiti.01@gmail.com">faisal.alsukiti.01@gmail.com</a></p>
    </footer>
  </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(debug=True)
