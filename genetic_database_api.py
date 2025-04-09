
from Bio import Entrez

class GeneticDatabaseAPI:
    """A class to access genetic databases like NCBI GenBank."""

    def __init__(self, email):
        """Initialize with an email address for Entrez API."""
        Entrez.email = email

    def fetch_genbank_record(self, accession_id):
        """Fetch a GenBank record by accession ID."""
        try:
            with Entrez.efetch(db="nucleotide", id=accession_id, rettype="gb", retmode="text") as handle:
                record = handle.read()
            return record
        except Exception as e:
            return f"Error fetching record: {e}"

# Example usage:
# api = GeneticDatabaseAPI(email="your_email@example.com")
# record = api.fetch_genbank_record("NC_000852")
# print(record)



import requests

class EnsemblAPI:
    """A class to access Ensembl REST API for genetic data."""

    BASE_URL = "https://rest.ensembl.org"

    @staticmethod
    def fetch_gene_by_id(gene_id, content_type="application/json"):
        """Fetch gene information by Ensembl Gene ID."""
        endpoint = f"/lookup/id/{gene_id}"
        headers = {"Content-Type": content_type}
        try:
            response = requests.get(EnsemblAPI.BASE_URL + endpoint, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

# Example usage:
# ensembl_api = EnsemblAPI()
# gene_info = ensembl_api.fetch_gene_by_id("ENSG00000139618")
# print(gene_info)


from logger import Logger

# Adding logging to database operations
class LoggedGeneticDatabaseAPI(GeneticDatabaseAPI):
    def fetch_genbank_record(self, accession_id):
        Logger.log_info(f"Fetching GenBank record for accession ID: {accession_id}")
        result = super().fetch_genbank_record(accession_id)
        if "Error" in result:
            Logger.log_error(f"Error fetching GenBank record: {result}")
        else:
            Logger.log_info("Successfully fetched GenBank record.")
        return result
    


import requests

class ClinVarAPI:
    """A class to access ClinVar genetic variant data."""

    BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

    @staticmethod
    def fetch_variant(variant_id, email, api_key=None):
        """Fetch variant information from ClinVar by ID."""
        params = {
            "db": "clinvar",
            "id": variant_id,
            "rettype": "xml",
            "email": email,
            "api_key": api_key
        }
        try:
            response = requests.get(f"{ClinVarAPI.BASE_URL}/efetch.fcgi", params=params)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            return {"error": str(e)}

class OMIMAPI:
    """A class to access OMIM genetic disorder data."""

    BASE_URL = "https://api.omim.org/api"

    @staticmethod
    def fetch_disease(disease_id, api_key):
        """Fetch disease information from OMIM by ID."""
        headers = {"Content-Type": "application/json"}
        params = {"mimNumber": disease_id, "format": "json", "apiKey": api_key}
        try:
            response = requests.get(f"{OMIMAPI.BASE_URL}/entry", headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}



from secure_storage import SecureStorage

class SecureDatabaseAPI(LoggedGeneticDatabaseAPI):
    """Extends the LoggedGeneticDatabaseAPI with secure storage."""

    def __init__(self, email, storage_path, encryption_key=None):
        super().__init__(email)
        self.storage = SecureStorage(storage_path, encryption_key)

    def fetch_and_store_genbank_record(self, accession_id):
        """Fetch GenBank record and securely store the result."""
        result = self.fetch_genbank_record(accession_id)
        if "Error" not in result:
            self.storage.save(f"{accession_id}_genbank.txt", result)
            Logger.log_info(f"GenBank record for {accession_id} stored securely.")
        return result

    def fetch_and_store_ensembl_gene(self, gene_id):
        """Fetch Ensembl gene info and securely store the result."""
        result = EnsemblAPI.fetch_gene_by_id(gene_id)
        if "error" not in result:
            self.storage.save(f"{gene_id}_ensembl.txt", str(result))
            Logger.log_info(f"Ensembl gene info for {gene_id} stored securely.")
        return result
