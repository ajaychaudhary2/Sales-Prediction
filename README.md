

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-%20web%20app-green?logo=flask)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

# 🧠 Sales Prediction Web App 🚀

![Sales Icon](https://img.icons8.com/color/96/000000/sales-performance.png)

**Predict your sales instantly by entering your ad spend for TV, Radio, and Newspaper!**

---

## ✨ Features

- 🌟 **Instant Sales Prediction** from your ad spend
- 📊 **Breakdown** of each channel's contribution
- 🎨 **Modern, clean, and responsive UI**
- 💾 **Easy to use and extend**

---


## 🗂️ Project Structure

```text
Sales Prediction/
│
├── Advertising.csv         # Dataset used for training
├── app.py                 # Flask web application
├── train_model.py         # Script to train and save the model
├── test_model.py          # Script to test the model with sample input
├── requirements.txt       # Python dependencies
├── models/
│   └── model.pkl          # Trained ML model
├── utils/
│   ├── predictor.py       # Model loading and prediction functions
│   ├── data_cleaning.py   # Data cleaning utilities
│   └── logger.py          # Logging utilities
├── setup.py              # Project packaging and installation script
└── templates/
    ├── index.html         # Home page (input form)
    └── result.html        # Results page (prediction output)
```

---

## 🛠️ Utilities (`utils/`)

- **predictor.py**: Functions to load the trained model and make predictions. Used by both the web app and test scripts.
- **data_cleaning.py**: Utilities for cleaning and preprocessing the dataset before training or prediction.
- **logger.py**: Handles logging of important events, errors, and information during model training and prediction.


These utility modules help keep the code modular, reusable, and easy to maintain.

---

## 📦 Packaging & Installation (`setup.py`)

The `setup.py` file allows you to package your project and install it as a Python module. This is useful for distribution or for installing dependencies in a standardized way.

**To install the project locally (editable mode):**
```bash
pip install -e .
```
This will let you import your project modules anywhere in your environment while you continue to develop.

---

## ⚡ Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ajaychaudhary2/Sales-Prediction.git
   cd "Sales Prediction"
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Train the model (if not already trained):**
   ```bash
   python train_model.py
   ```

4. **Test the model from the command line:**
   ```bash
   python test_model.py
   ```
   This will print a sample prediction using the trained model.

5. **Run the app:**
   ```bash
   python app.py
   ```
6. **Open in browser:** [http://127.0.0.1:5000](http://127.0.0.1:5000)

---
