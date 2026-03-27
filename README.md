## **Project Overview**

This project focuses on a comprehensive Exploratory Data Analysis (EDA) of the telcommunication company.  Customer churn, also know as customer attrition, refers to as. The goal is to move beyond raw numbers and identify the behavioral patterns that signal a customer is about to leave. By understanding the factors that contribute to customer churn and building predictive models, business can take proactive measures to retain customers.

## **The Business Challenge**

In the highly competitive telecommunications industry, acquiring a new customer is 5x more expensive than retaining an existing one. Our objective is to pinpoint high-risk segment such as those on specific contract types or facing high monthly costs to help the marketing team design proactive retention campaigns.

## **Dataset**

* Source: Kaggle (Telco Customer Churn).

* Scale: 7,043 rows and 21 feature columns.

* Key Attributes: Demographics (Gender, Seniority), Services (Internet, Tech Support), and Financials (Monthly/Total Charges).

## **Exploratory Data Analysis (EDA)**

The EDA phase involves exploring the dataset to gain insights into the underlying patterns and relationship. Key steps in the EDA process includes:

+ **Data Sanitization:** Converting TotalCharges to numeric and handling missing values.

- **Feature Engineering:** Binning tenure into 12-month cohorts to track lifecycle trends.

* **Univariate Exploration:** Analyzing the distribution of the Churn target variable.

* **Bivariate Correlation:** Using Kernel Density Estimation (KDE) plots to compare charge distributions between churners and non-churners. 

## **Findings from Analysis**

Based on the EDA conducted in the analysis, several high-impact insights were discovered:

1. A significant spike in churn occurs during the first few months of tenure. New customers are the highest risk group.

2. Customers on Month-to-Month contracts are significantly more likely to churn compared to those on One or Two-year plans.

3. Churners typically have higher Monthly Charges than retained customers, suggesting a price wall where customers seek cheaper alternatives.

4. Customers without Tech Support or Online Security show a higher propensity to leave, highlighting the value of sticky services.

5. There is a notable correlation between churn and the Electronic Check payment method.

## **Modeling & Performance**
   
To move from analysis to action, I developed a machine learning pipeline focused on high sensitivity (recall) to ensure we don't miss potential churners.

1. **Handling Class Imbalance**
   
The original dataset was imbalanced (roughly 27% churn). I applied SMOTE to oversample the minority class, ensuring the model is equally proficient at identifying both Churners and Non-Churners.

2. **The Model: Random Forest Classifier**
   
I chose the Random Forest algorithm for its robustness and ability to handle the various categorical features (Internet Service, Contract Type, etc.) present in the Telco data.

3. **Report Card (Results)**

* **High Recall:** The model is optimized to capture the maximum number of actual churners.

* **Evaluation Metrics:** (Note: You can fill these in from your Notebook output, but typically with SMOTE/Random Forest, you'll see a balanced accuracy across both classes).

## **Project Deployment (The Web App)**
   
I didn't stop at the notebook, I built a functional web interface using Flask to make these predictions accessible to non-technical users.

* **Backend:** Flask API (main.py)

* **Model Storage:** The trained model is serialized using joblib for real-time inference.

* **Input Handling:** Users can input customer details (Tenure, Monthly Charges, Contract Type) through a web form to receive an instant churn probability score.

To simplify user input in the web app, I automated the calculation of Total Charges by using the relationship between Tenure and Monthly Fees.

## **Strategic Business Recommendations**

Based on the patterns identified during the EDA and Model segments, I recommend the following actions for the retention team:

* Incentivize Long-Term Contracts: Since Month-to-Month customers are the highest churn risk, offer a **First Month Free **or **Loyalty Discount** for users who switch to a 1-year or 2-year contract.

* Targeted Onboarding Support: Churn is highest in the first 6 months. Implement a **Welcome Success Prog**ram where new users receive a check-in call or specialized tech support within their first 90 days.

* Bundle Sticky Services: Customers without Online Security or Tech Support leave at higher rates. Bundling these services into the "Fiber Optic" package could create more hooks that keep customers from leaving.

* Proactive High-Charge Alerts: For customers whose monthly charges exceed a certain threshold, the system should trigger a proactive outreach to offer a more cost-effective plan before they decide to cancel.

## **How to Run This Project**

* Clone the repo

* Install dependencies: pip install -r requirements.txt

* Run the Web App: python main.py

* Access: Open http://127.0.0.1:5000/ in your browser.

  ## **Author**
  
  Hillary Onah
  *Finance and Data Science Analyst*
