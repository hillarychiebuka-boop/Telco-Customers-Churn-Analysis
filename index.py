from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__, template_folder='templates')

# Load your model
# Ensure this file is in the same folder as main.py
model = joblib.load("model_rf_smote.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def make_prediction():
    try:
        # 1. The exact list of features your model was trained on
        # Note: 'SeniorCitizen' is a single column, others are dummy variables
        model_columns = [
            'SeniorCitizen', 'MonthlyCharges', 'TotalCharges', 
            'gender_Female', 'gender_Male', 'Partner_No', 'Partner_Yes', 
            'Dependents_No', 'Dependents_Yes', 'PhoneService_No', 'PhoneService_Yes', 
            'MultipleLines_No', 'MultipleLines_No phone service', 'MultipleLines_Yes', 
            'InternetService_DSL', 'InternetService_Fiber optic', 'InternetService_No', 
            'OnlineSecurity_No', 'OnlineSecurity_No internet service', 'OnlineSecurity_Yes', 
            'OnlineBackup_No', 'OnlineBackup_No internet service', 'OnlineBackup_Yes', 
            'DeviceProtection_No', 'DeviceProtection_No internet service', 'DeviceProtection_Yes', 
            'TechSupport_No', 'TechSupport_No internet service', 'TechSupport_Yes', 
            'StreamingTV_No', 'StreamingTV_No internet service', 'StreamingTV_Yes', 
            'StreamingMovies_No', 'StreamingMovies_No internet service', 'StreamingMovies_Yes', 
            'Contract_Month-to-month', 'Contract_One year', 'Contract_Two year', 
            'PaperlessBilling_No', 'PaperlessBilling_Yes', 'PaymentMethod_Bank transfer (automatic)', 
            'PaymentMethod_Credit card (automatic)', 'PaymentMethod_Electronic check', 
            'PaymentMethod_Mailed check', 'tenure_group_1 - 12', 'tenure_group_13 - 24', 
            'tenure_group_25 - 36', 'tenure_group_37 - 48', 'tenure_group_49 - 60', 'tenure_group_61 - 72'
        ]

        # 2. Initialize a dictionary with all 52 features set to 0
        input_data = {col: [0] for col in model_columns}

        # 3. Get numerical values from the form
        # Matches 'name' attributes in your index.html
        tenure = float(request.form.get('tenure', 0))
        monthly_charges = float(request.form.get('monthly_charges', 0))
        
        input_data['tenure'] = [tenure]
        input_data['MonthlyCharges'] = [monthly_charges]
        input_data['TotalCharges'] = [tenure * monthly_charges]
        
        # 4. Handle Categorical Logic (Turning 0s into 1s)
        # Gender
        gender = request.form.get('gender')
        if gender == 'male':
            input_data['gender_Male'] = [1]
        else:
            input_data['gender_Female'] = [1]

        # Contract
        contract = request.form.get('contract')
        if contract == 'month-to-month':
            input_data['Contract_Month-to-month'] = [1]
        elif contract == 'one-year':
            input_data['Contract_One year'] = [1]
        else:
            input_data['Contract_Two year'] = [1]

        # 5. Create DataFrame with specific column order
        final_df = pd.DataFrame(input_data)[model_columns]

        # 6. Generate Prediction
        prediction = model.predict(final_df)[0]
        proba = model.predict_proba(final_df)[0]
        
        # Format results
        outcome = "Churner" if prediction == 1 else "Non-Churner"
        prob_val = f"{round(proba[1] * 100, 2)}%"

        # 7. Render result
        return render_template('index.html', 
                               prediction=outcome, 
                               probability=prob_val)

    except Exception as e:
        return f"Prediction Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)