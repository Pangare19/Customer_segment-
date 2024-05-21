from flask import Flask, render_template, request, redirect
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'  # Replace with a secure key

# Load pre-trained model and customer data
loaded_model = pickle.load(open('Customer_model.pkl', 'rb'))  # Assuming model is saved as `.sav`
df = pd.read_csv('Cluster_Customer.csv')  # Assuming data file is named correctly

def predict_cluster(data):
    """Predicts the cluster label for a given customer data point."""
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    cluster_label = loaded_model.predict(scaled_data)[0]
    return cluster_label

@app.route('/')
def index():
    """Renders the main form page."""
    return render_template('index.html')  # Assuming you have the template

@app.route('/predict', methods=['POST'])
def submit_form():
    """Handles form submission, predicts cluster, and redirects to results."""
    balance = float(request.form.get('balance'))
    balance_frequency = float(request.form.get('balance_frequency'))
    purchases = float(request.form.get('purchases'))
    oneoff_purchases = float(request.form.get('oneoff_purchases'))
    installments_purchases = float(request.form.get('installments_purchases'))
    cash_advance = float(request.form.get('cash_advance'))
    purchases_frequency = float(request.form.get('purchases_frequency'))
    oneoff_purchases_frequency = float(request.form.get('oneoff_purchases_frequency'))
    purchases_installments_frequency = float(request.form.get('purchases_installments_frequency'))
    cash_advance_frequency = float(request.form.get('cash_advance_frequency'))
    cash_advance_trx = int(request.form.get('cash_advance_trx'))
    purchases_trx = int(request.form.get('purchases_trx'))
    credit_limit = float(request.form.get('credit_limit'))
    payments = float(request.form.get('payments'))
    minimum_payments = float(request.form.get('minimum_payments'))
    prc_full_payment = float(request.form.get('prc_full_payment'))
    tenure = int(request.form.get('tenure'))

    data = [[
        balance,
        balance_frequency,
        purchases,
        oneoff_purchases,
        installments_purchases,
        cash_advance,
        purchases_frequency,
        oneoff_purchases_frequency,
        purchases_installments_frequency,
        cash_advance_frequency,
        cash_advance_trx,
        purchases_trx,
        credit_limit,
        payments,
        minimum_payments,
        prc_full_payment,
        tenure
    ]]

    cluster_label = predict_cluster(data)

    # No visualization component included as per your request

    return redirect(f'/results?cluster={cluster_label}')

@app.route('/results')
def results():
    """Displays the predicted cluster label."""
    cluster_label = int(request.args.get('cluster'))
    cluster_info = f"Customer belongs to cluster {cluster_label}"  # Modify based on your data/model

    return render_template('results.html', cluster_info=cluster_info)  # Assuming you have the template

if __name__ == '__main__':
    app.run(debug=True)
