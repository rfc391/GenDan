
from flask import Flask, render_template, request, jsonify
from genetic_database_api import LoggedGeneticDatabaseAPI
from logger import Logger

app = Flask(__name__)

# Initialize the Genetic Database API
database_api = LoggedGeneticDatabaseAPI(email="your_email@example.com")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch-genbank', methods=['POST'])
def fetch_genbank():
    accession_id = request.form.get('accession_id')
    Logger.log_info(f"Received request to fetch GenBank record for: {accession_id}")
    result = database_api.fetch_genbank_record(accession_id)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)



@app.route('/fetch-ensembl', methods=['POST'])
def fetch_ensembl():
    gene_id = request.form.get('gene_id')
    Logger.log_info(f"Received request to fetch Ensembl gene info for: {gene_id}")
    from genetic_database_api import EnsemblAPI
    result = EnsemblAPI.fetch_gene_by_id(gene_id)
    return jsonify(result)



@app.route('/fetch-clinvar', methods=['POST'])
def fetch_clinvar():
    variant_id = request.form.get('variant_id')
    email = "your_email@example.com"  # Replace with a valid email for API access
    Logger.log_info(f"Received request to fetch ClinVar variant info for: {variant_id}")
    from genetic_database_api import ClinVarAPI
    result = ClinVarAPI.fetch_variant(variant_id, email)
    return jsonify(result)

@app.route('/fetch-omim', methods=['POST'])
def fetch_omim():
    disease_id = request.form.get('disease_id')
    api_key = "your_api_key"  # Replace with a valid OMIM API key
    Logger.log_info(f"Received request to fetch OMIM disease info for: {disease_id}")
    from genetic_database_api import OMIMAPI
    result = OMIMAPI.fetch_disease(disease_id, api_key)
    return jsonify(result)



@app.route('/visualize-data', methods=['GET'])
def visualize_data():
    """Endpoint to provide data for visualization."""
    storage = SecureStorage(storage_path="./secure_data")
    files = os.listdir(storage.storage_path)

    labels = []
    values = []
    for file in files:
        labels.append(file)
        file_path = os.path.join(storage.storage_path, file)
        values.append(os.path.getsize(file_path))  # Use file size as an example metric

    return jsonify({'labels': labels, 'values': values})
