## Insurance Premium Prediction (Django + ML)

This project is a web application that predicts health insurance premiums using a trained machine learning model served through a Django backend.​
Users can enter basic information (age, sex, BMI, number of children, smoking status, and region) and get an estimated insurance cost in seconds.
​

## Features

Insurance premium prediction using a trained ML regression model.
​Clean Django frontend with pages: Home, About, Contact, and Prediction.
​User registration with email field and password confirmation.
​Email verification form for entering a verification code (UI ready).
​Bootstrap‑styled forms and templates for a simple, modern UI.
​

## Tech Stack
Backend: Django (Python) with standard project structure (settings.py, urls.py, wsgi.py, asgi.py).
Machine Learning: Model trained in a Jupyter Notebook and saved as insurance_premium_model.pkl using joblib.
Dataset: insurance.csv (columns: age, sex, bmi, children, smoker, region, expenses).
Auth: Django authentication with a custom UserRegisterForm based on UserCreationForm.
Templates: Django templates (base.html, index.html, about.html, contract.html, prediction.html).
​

## Project Structure (Main Files)

project_root/
├── insurance/                 # Django project (settings, URLs, WSGI/ASGI)
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── home/                      # Main app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── about.html
│       ├── contract.html
│       └── prediction.html
├── static/
│   └── insurance_premium_model.pkl
├── insurance.csv              # Training data
└── Premium-Prediction.ipynb   # Notebook for training the model


views.py: Handles pages and the prediction logic (loads the model, reads form data, returns prediction).
forms.py: Contains UserRegisterForm and EmailVerificationForm for authentication flow.
templates/: All HTML pages extend base.html and show navigation and content blocks.
​

## How the Prediction Works
The model is trained in Premium-Prediction.ipynb on insurance.csv using features: age, sex, bmi, children, smoker, region.
The trained model is saved as insurance_premium_model.pkl and placed in the static/ directory.
In views.py, the model is loaded with joblib.load('static/insurance_premium_model.pkl') when the app starts.
On the prediction page, the user submits a form with input fields that match the model features.
The app passes the inputs to the model’s predict method and shows the predicted premium (rounded) on prediction.html.
​

## Setup and Installation

1. Clone the repository
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

2. Create and activate a virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate

3. Install dependencies
Make sure Django, joblib, and the ML libraries used in the notebook are installed.

pip install -r requirements.txt

If you do not have a requirements.txt yet, you can include at least:
Django
joblib
scikit-learn
pandas
numpy

4. Apply migrations
python manage.py migrate

6. Create a superuser (optional, for admin)
python manage.py createsuperuser

8. Ensure the model file exists
Confirm that static/insurance_premium_model.pkl is present.
If not, open Premium-Prediction.ipynb, run the notebook, train the model, and export it as insurance_premium_model.pkl to the static/ folder.
​
7. Run the development server
   
python manage.py runserver
Then open:
http://127.0.0.1:8000/

You can access:
Home page: /
About page: /about/
Contact/contract page: /contract/
Prediction page: /prediction/
​

## Usage

Go to the Prediction page (/prediction/).
Fill in the form fields: age, sex, BMI, number of children, smoking status, and region.
Submit the form to get an estimated insurance premium displayed on the same page.
​

If user registration is wired in your URLs:

Register a new account using the registration page (based on UserRegisterForm).
​
(Optional) Use the email verification screen to enter a verification code (if you add backend logic for sending/checking codes).
​

## Authentication Forms

UserRegisterForm extends Django’s UserCreationForm, adds a required email field, and applies Bootstrap classes for styling.
EmailVerificationForm is a simple form with a 6‑digit verification_code field and Bootstrap styling.
These forms are designed to integrate into views/URLs in views.py and urls.py inside the app.
​

## Notes and Limitations

This project is for educational and informational purposes only; it does not provide official insurance quotes.
Real insurance premiums depend on more factors than the ones in insurance.csv and usually require a full underwriting process.
The model quality depends on the training process in the notebook and on the dataset used.
​

## Possible Improvements

Add proper email sending and verification logic to match EmailVerificationForm.
Improve preprocessing and model selection in Premium-Prediction.ipynb for higher accuracy.
Add better input validation, error messages, and unit tests.
Containerize the app with Docker and deploy on a cloud platform.
