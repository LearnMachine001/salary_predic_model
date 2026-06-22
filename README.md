# 💰 Salary Prediction System

A Machine Learning based web application that predicts an employee's salary based on years of experience.

## 🚀 Features

- User Registration & Login
- Salary Prediction using Machine Learning
- SQLite Database Integration
- Prediction History Storage
- Responsive UI with Flask
- Secure Authentication System

## 🛠️ Technologies Used

### Frontend
- HTML
- CSS3
- Bootstrap

### Backend
- Python
- Flask

### Database
- SQLite3

### Machine Learning
- Scikit-Learn
- NumPy
- Joblib

## 📂 Project Structure

```bash
salary_prediction_model/
│
├── app.py
├── database.py
├── Salary_model.py
├── salary_model.pkl
├── salary_predict.db
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── predict.html
│
├── static/
│   ├── style.css
│   └── images/
│
└── README.md
```

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/LearnMachine001/salary_predic_model.git
cd salary_predic_model
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Application will start on:

```bash
http://127.0.0.1:5000
```

## 🤖 Machine Learning Model

The model is trained using:

- Linear Regression
- Years of Experience as Input
- Salary as Output

Example:

| Experience (Years) | Predicted Salary |
|-------------------|------------------|
| 1 | ₹30,000 |
| 3 | ₹50,000 |
| 5 | ₹70,000 |
| 10 | ₹1,20,000 |

## 📸 Screenshots

### Home Page
(Add Screenshot Here)

### Login Page
(Add Screenshot Here)

### Salary Prediction Page
(Add Screenshot Here)

## 🔮 Future Improvements

- Multiple ML Algorithms
- Salary Visualization Charts
- Admin Dashboard
- User Profile Management
- Model Accuracy Comparison
- Cloud Deployment

## 👨‍💻 Author

**Vikas kumar**

- MCA Student
- Machine Learning Enthusiast
- Python Developer

GitHub: https://github.com/LearnMachine001

## 📜 License

This project is licensed under the MIT License.
