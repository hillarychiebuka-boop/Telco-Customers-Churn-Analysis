**Project Overview**

This project focuses on a comprehensive Exploratory Data Analysis (EDA) of the telcommunication company.  Customer churn, also know as customer attrition, refers to as. The goal is to move beyond raw numbers and identify the behavioral patterns that signal a customer is about to leave. By understanding the factors that contribute to customer churn and building predictive models, business can take proactive measures to retain customers.

**The Business Challenge**

In the highly competitive telecommunications industry, acquiring a new customer is 5x more expensive than retaining an existing one. Our objective is to pinpoint high-risk segment such as those on specific contract types or facing high monthly costs to help the marketing team design proactive retention campaigns.

**Dataset**

* Source: Kaggle (Telco Customer Churn).

* Scale: 7,043 rows and 21 feature columns.

* Key Attributes: Demographics (Gender, Seniority), Services (Internet, Tech Support), and Financials (Monthly/Total Charges).

**Exploratory Data Analysis (EDA)**

The EDA phase involves exploring the dataset to gain insights into the underlying patterns and relationship. Key steps in the EDA process includes:

+ **Data Sanitization:** Converting TotalCharges to numeric and handling missing values.

- **Feature Engineering:** Binning tenure into 12-month cohorts to track lifecycle trends.

* **Univariate Exploration:** Analyzing the distribution of the Churn target variable.

* **Bivariate Correlation:** Using Kernel Density Estimation (KDE) plots to compare charge distributions between churners and non-churners. 

**Findings from Analysis**

Based on the EDA conducted in the analysis, several high-impact insights were discovered:

1. A significant spike in churn occurs during the first few months of tenure. New customers are the highest risk group.

2. Customers on Month-to-Month contracts are significantly more likely to churn compared to those on One or Two-year plans.

3. Churners typically have higher Monthly Charges than retained customers, suggesting a price wall where customers seek cheaper alternatives.

4. Customers without Tech Support or Online Security show a higher propensity to leave, highlighting the value of sticky services.

5. There is a notable correlation between churn and the Electronic Check payment method.
