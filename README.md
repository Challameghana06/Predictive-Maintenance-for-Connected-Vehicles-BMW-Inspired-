# 🚗 Predictive Maintenance for Connected Vehicles (BMW-Inspired)

### An AI-powered predictive maintenance system that forecasts vehicle service needs before failure — inspired by BMW’s ConnectedDrive vision.

---

## 🧠 Overview
Modern vehicles generate massive amounts of sensor data every second.  
This project leverages **machine learning** to predict whether a car will require maintenance soon, based on key operational parameters such as air temperature, torque, and rotational speed.

It is designed to demonstrate how AI can enable **data-driven automotive intelligence**, reduce downtime, and improve vehicle safety.

---

## ⚙️ Features
- 📊 **Data-Driven Insights:** Learns from vehicle sensor data to identify early warning signs.  
- 🔍 **ML-Powered Predictions:** Uses a trained Random Forest / AI model to forecast upcoming maintenance needs.  
- 🌐 **Interactive Streamlit UI:** Simple sliders to simulate sensor inputs and predict instantly.  
- 💻 **Deployable Anywhere:** Works locally or on the cloud (Streamlit / Colab).  

---

## 🧩 Tech Stack
| Category | Tools / Libraries |
|-----------|------------------|
| Language | Python 3.10+ |
| Framework | Streamlit |
| Machine Learning | scikit-learn, joblib |
| Data Processing | pandas, numpy |
| Visualization | matplotlib, seaborn |

---

## 📊 Dataset
**Source:** [AI4I 2020 Predictive Maintenance Dataset](https://www.kaggle.com/datasets/arnabbiswas1/ai4i2020-predictive-maintenance-dataset)

**Attributes used:**
- Air Temperature [K]  
- Process Temperature [K]  
- Torque [Nm]  
- Rotational Speed [rpm]  
- Tool Wear [min]  

**Target:** `Machine failure` (0 = Normal, 1 = Maintenance Required)

---

## 🤖 Model Details
| Parameter | Value |
|------------|--------|
| Algorithm | Random Forest Classifier |
| Accuracy | ~92% |
| Evaluation Metrics | F1-score, ROC-AUC, Confusion Matrix |
| Deployment | Streamlit App |

---

## 🖥️ App Preview
### 🎛️ Streamlit Interface
Enter sensor readings using sliders and click **Predict Maintenance Status** to get instant results:
- ✅ *Vehicle Operating Normally*  
- ⚠️ *Maintenance Needed Soon*

---

## 🚀 Getting Started
### 1️⃣ Clone Repository
```bash
git clone https://github.com/Challameghana06/predictive-maintenance-bmw.git
cd predictive-maintenance-bmw
