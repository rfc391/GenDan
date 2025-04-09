from flask import request, jsonify, render_template
from genetic_database_api import LoggedGeneticDatabaseAPI
from logger import Logger
from config import Config

database_api = LoggedGeneticDatabaseAPI(email=Config.EMAIL)

def register_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/fetch-genbank', methods=['POST'])
    def fetch_genbank():
        accession_id = request.form.get('accession_id')
        Logger.log_info(f"Received request to fetch GenBank record: {accession_id}")
        result = database_api.fetch_genbank_record(accession_id)
        return jsonify(result)

    @app.route('/fetch-ensembl', methods=['POST'])
    def fetch_ensembl():
        gene_id = request.form.get('gene_id')
        Logger.log_info(f"Received request to fetch Ensembl record: {gene_id}")
        result = database_api.fetch_ensembl_record(gene_id)
        return jsonify(result)
