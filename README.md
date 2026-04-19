# Iris Flower Prediction App

This is a Machine Learning web application built using Streamlit that predicts the species of an Iris flower based on user input features.



## Project Overview

The app takes four input parameters:

* Sepal Length (cm)
* Sepal Width (cm)
* Petal Length (cm)
* Petal Width (cm)

Based on these inputs, the model predicts the flower category:

* Setosa
* Versicolor
* Virginica


## Technologies Used

* Python
* Streamlit
* NumPy
* Scikit-learn
* Pickle (for model loading)


## Project Structure

```
iris-prediction-app/
│
├── app.py                # Main Streamlit application
├── iris_model.pkl       # Trained ML model
├── iris.csv             # Dataset
├── requirements.txt     # Required libraries
└── README.md            # Project documentation
```



## How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/your-username/iris-prediction-app.git
cd iris-prediction-app
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the application

```
streamlit run app.py
```



##  Output

After running the app, it will open in your browser:

```
http://localhost:8501
```



##  Example Input

| Feature      | Value |
| ------------ | ----- |
| Sepal Length | 5.1   |
| Sepal Width  | 3.5   |
| Petal Length | 1.4   |
| Petal Width  | 0.2   |

 Output: **Setosa**


## Features

* Simple and interactive UI
* Real-time predictions
* Lightweight and fast
* Easy to deploy


## 📌 Future Improvements

* Improve UI design
* Add model accuracy display
* Deploy online (Streamlit Cloud)


##  Author

Bhavya Kusam



##  Support

If you like this project, consider giving it a ⭐ on GitHub!
