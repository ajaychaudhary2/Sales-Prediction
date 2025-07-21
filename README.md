
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Flask-%20web%20app-green?logo=flask" alt="Flask">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
</p>

<h1 align="center">🧠 Sales Prediction Web App 🚀</h1>

<p align="center">
  <img src="https://img.icons8.com/color/96/000000/sales-performance.png" width="100" alt="Sales Icon"/>
</p>

<p align="center">
  <b>Predict your sales instantly by entering your ad spend for TV, Radio, and Newspaper!</b>
</p>

---

## ✨ Features

🌟 <b>Instant Sales Prediction</b> from your ad spend<br>
📊 <b>Breakdown</b> of each channel's contribution<br>
🎨 <b>Modern, clean, and responsive UI</b><br>
💾 <b>Easy to use and extend</b>

---

## �️ Project Structure

```text
Sales Prediction/
│
├── Advertising.csv         # Dataset used for training
├── app.py                 # Flask web application
├── train_model.py         # Script to train and save the model
├── requirements.txt       # Python dependencies
├── models/
│   └── model.pkl          # Trained ML model
└── templates/
    ├── index.html         # Home page (input form)
    └── result.html        # Results page (prediction output)
```

---

## ⚡ Quick Start

<details>
<summary><b>Setup in 3 Steps</b></summary>

1. <b>Clone the repository:</b>
   ```bash
   git clone https://github.com/ajaychaudhary2/Sales-Prediction.git
   cd "Sales Prediction"
   ```
2. <b>Install dependencies:</b>
   ```bash
   pip install -r requirements.txt
   ```
3. <b>Train the model (if not already trained):</b>
   ```bash
   python train_model.py
   ```
4. <b>Run the app:</b>
   ```bash
   python app.py
   ```
5. <b>Open in browser:</b> [http://127.0.0.1:5000](http://127.0.0.1:5000)

</details>

---
