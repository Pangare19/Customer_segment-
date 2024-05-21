Project Title: Customer Segmentation with Machine Learning

● Description:
This project demonstrates unsupervised and supervised machine learning techniques for customer segmentation. It leverages K-Means clustering to automatically identify distinct customer groups based on their 
characteristics. Subsequently, a Decision Tree Classifier is employed to predict customer behavior or segment membership for new customers.

● Key Features:

•Unsupervised Learning (K-Means Clustering): Groups customers into meaningful segments without pre-defined labels.
•Supervised Learning (Decision Tree Classifier): Predicts customer segment membership for new data points.
•User Interface (Flask Framework): Provides a user-friendly interface for interacting with the model and visualizing results.


● Directory Structure:

customer_segmentation/
├── app.py                  # Flask application code
├── k-means.pkl              # Saved K-Means clustering model
├── Customer_model.pkl      # Saved Decision Tree Classifier model
├── customer_segmentation-checkpoint.ipynb  # Jupyter notebook with analysis and model training
├── templates/
│   ├── index.html          # HTML template for user input
│   └── results.html         # HTML template to display segmentation results
└── README.md               # This file (instructions and usage)


● Interact with the UI:

•Access the application URL in your web browser.
•Provide customer data in the input form on index.html.
•Click the submit button to trigger the segmentation process.
•The predicted segment and optionally, additional insights, will be displayed on results.html.


● Note:

•Ensure the K-Means and Decision Tree Classifier models (k-means.pkl and Customer_model.pkl) are present in the correct location for prediction purposes. You may need to generate these models using the 
•Jupyter notebook (customer_segmentation-checkpoint.ipynb) first.

