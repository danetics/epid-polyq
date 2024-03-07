"""
Tools to manipulate ExpansionHunter variant catalogs
"""

def get_random_subset(varcatalog: str, n: float, outfile: str):
    # Sufficient to just use pandas JSON manipulation
    data = pd.read_json(varcatalog)
    data.subset(n=n).to_json(outfile, orient='records')

def get_named_locus(varcatalog: str, names: list[str], outfile: str):
    data = pd.read_json(varcatalog)
    data = data[data['LocusId'].isin(names)]
    data.to_json(outfile, orient='records')
    