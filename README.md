# 🌟 KairosPredict

📈 **Predicting Future Stock Market Trends with Machine Learning**

KairosPredict is an intelligent stock trend prediction application that analyzes historical patterns using clustering algorithms and machine learning to forecast future market behavior. It provides real-time insights through a user-friendly graphical interface backed by robust data processing and model evaluation.

---

## 🚀 Key Features

✅ Predict future stock market trends using advanced **Machine Learning**  
✅ Real-time stock data fetched using **TradingView API**  
✅ Interactive and modern **Graphical User Interface (GUI)** built with CustomTkinter  
✅ Supports multiple **clustering algorithms** (KMeans, DBSCAN, Agglomerative)  
✅ Intelligent pattern detection using **Perceptually Important Points (PIPs)**  
✅ **Multi-threaded** execution for smooth and responsive performance  
✅ Customizable themes and chart configurations (Dark/Light mode, colors, MA lines)  
✅ **Authentication system** with OTP-based password recovery  
✅ Pattern cluster visualization and future pattern simulation  
✅ Future-ready: Designed to scale as a **SaaS** platform

---

### ⚠️ Note

If you're facing issues running `app.py`, you can use the lightweight version:  
```bash
python app_lite.py
```

---

## 🛠 Installation & Setup

1️⃣ Install **Python** (version ≥ 3.8)

2️⃣ Install dependencies:  
```bash
pip install -r requirements.txt
```

3️⃣ Run the application:  
```bash
python app.py
```

---

## 📂 Modules & Their Role

| 🏷 Module           | 📌 Usage                                         |
|--------------------|--------------------------------------------------|
| 📊 **NumPy**        | Efficient numerical computations                 |
| 🧠 **Scikit-learn** | ML algorithms: clustering, classification        |
| 🖼 **CustomTkinter**| Beautiful, modern GUI for dashboard              |
| 📑 **Pandas**       | Data handling, analysis, and transformations     |
| ⚙️ **Threading**     | Enhances app responsiveness and multitasking     |
| 📈 **TradingView API** | Fetches live stock market data              |
| 🖼 **Pillow (PIL)** | For image and icon rendering in GUI              |

---

## 🔍 How It Works

1. **Pattern Extraction**: Uses a PIP algorithm to extract significant trend points from historical data using various distance metrics (Euclidean, Perpendicular, Vertical).

2. **Clustering**: Clusters the patterns using KMeans, DBSCAN, and Agglomerative clustering. Only unique patterns (based on ID) are stored.

3. **Classification**: Current trend is analyzed and classified using a Random Forest model to find the most similar historical pattern.

4. **Prediction**: The matched pattern’s future segment is scaled and aligned with the current trend, providing a **visual forecast** of the upcoming movement.

5. **Voting System**: Among different cluster outputs, a voting mechanism selects the most accurate matching pattern for display.

---

## 📈 Performance

✔️ **Achieves over 65% prediction accuracy**  
📄 Check detailed reports in [`model_evaluation_report.md`](model_evaluation_report.md)

✔️ Scalable architecture designed for future integration with additional models and datasets.

---

## 🔮 Planned Enhancements

- ✅ Expand ML model variety including **AI-driven deep learning** methods  
- ✅ Add support for more **stocks and indices**  
- ✅ Release **mobile and web versions**  
- ✅ Enable full **SaaS deployment** with subscription-based access  
- ✅ Integration of technical indicators and auto-detection tools

---

## 🧠 Architecture Diagram

<img src="https://github.com/user-attachments/assets/26fa180c-d3ee-45ff-b305-d34d34b1a4e3" width="650" height="650" alt="KairosPredict Architecture"/>

---

## 📞 Contact & Support

📧 **Email**: [KairosPredict@gmail.com](mailto:pkrprem2005@gmail.com)  
📱 **Phone**: +91 63804 98136
