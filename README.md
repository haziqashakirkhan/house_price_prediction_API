# House Price Prediction API

A beginner-friendly Machine Learning deployment project that predicts house prices based on house area using **Linear Regression** and serves predictions through a **FastAPI** REST API.

## Features

* Train a Linear Regression model using Scikit-learn
* Predict house prices based on house area
* Save the trained model using Pickle
* Deploy the model with FastAPI
* Interactive API documentation using Swagger UI

## Project Structure

```text
House_Price_Prediction_API/
│
├── house_data.csv
├── train.py
├── model.pkl
├── app.py
├── requirements.txt
└── README.md
```

## Technologies Used

* Python
* Pandas
* Scikit-learn
* FastAPI
* Uvicorn
* Pickle

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd House_Price_Prediction_API
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Train the Model

Run the training script:

```bash
python train.py
```

This will train the Linear Regression model and generate a `model.pkl` file.

## Run the FastAPI Application

Start the API server:

```bash
uvicorn app:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Interactive API documentation:

```
http://127.0.0.1:8000/docs
```

## API Endpoints

### Home

**GET /**

Response:

```json
{
  "message": "Welcome to House Price Prediction API"
}
```

### Predict House Price

**POST /predict**

Request:

```json
{
  "area": 1500
}
```

Response:

```json
{
  "predicted_price": 4500000.0
}
```

## Author

**Haziqa Shakir**
