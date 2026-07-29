# tests/test_pubchem_connectivity.py
import json
import urllib.request
import urllib.parse
import pytest

pytestmark = pytest.mark.network

def test_pubchem_smiles_resolves():
    smiles = urllib.parse.quote("c1ccncc1")  # pyridine
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/{smiles}/cids/JSON"
    with urllib.request.urlopen(url, timeout=15) as resp:
        data = json.loads(resp.read())
    assert data["IdentifierList"]["CID"][0] > 0
