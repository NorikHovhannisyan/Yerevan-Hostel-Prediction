# 🏨 Yerevan Hotel Price Predictor
This project is an End-to-End Machine Learning application designed to predict the nightly price of hotels in Yerevan, Armenia. By analyzing features such as star ratings, customer reviews, and facilities, the model provides data-driven estimates for the local hospitality market.

## 🚀 Live Demo
You can try the live application here: [[Streamlit Cloud](http://192.168.1.100:8501)]

## 🧐 Overview
The hotel industry in Yerevan is diverse. This project aims to bridge the gap between subjective hotel ratings and objective market pricing. The workflow involves data collection, rigorous cleaning, exploratory data analysis, and the deployment of a predictive model.

## 🛠 Tech Stack
- Language: Python 3.10+
- Data Processing: Pandas, NumPy
- Machine Learning: Scikit-learn (Random Forest Regressor, Linear Regression)
- Web Framework: Streamlit
- Serialization: Pickle & JSON


## 📊 Key Insights from EDA
- Star Ratings: The strongest predictor of price, showing a clear linear trend.

- Feature Correlation: Cleanliness and Comfort scores are highly correlated, suggesting that hotels focusing on one usually excel in both.

- Model Performance: The Random Forest model outperformed Linear Regression, achieving a Root Mean Square Error (RMSE) of ~$34.


## 🏗 Project Structure

```Plaintext
├── data/                   # Raw and cleaned datasets
├── models/                 # Saved .pkl model and scaler files
├── house.py                # Streamlit web application code
├── model_columns.json      # Feature names for consistency
├── requirements.txt        # List of dependencies
├── README.md               # Project documentation
└── .gitignore              # Files to be excluded from the repo
```
## 💻 Installation & Usage
- Clone the repository:

```
git clone https://github.com/your-username/yerevan-hotel-prediction.git
cd yerevan-hotel-prediction
```
- Install dependencies:

```
pip install -r requirements.txt
```

- Run the application:

```
streamlit run house.py
```

## 📈 Future Improvements
- Add Location-based analysis (mapping prices to specific districts).

- Incorporate Seasonality (prices change during summer/winter).

- Implement a Web Scraper to update the dataset in real-time.

## Author: Norik Hovhannisyan

## [[LinkedIn:](https://www.linkedin.com/in/norik-hovhannisyan-780130323/)]
