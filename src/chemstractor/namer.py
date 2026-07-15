import pubchempy as pcp

def standardize_solvent(raw_name: str) -> str:
    try:
        # Search PubChem for the compound
        compounds = pcp.get_compounds(raw_name, 'name')
        if compounds:
            # Return the canonical IUPAC name
            return compounds[0].iupac_name
    except:
        pass
    return raw_name

print(standardize_solvent("THF-d8")) # Outputs: 2,2,3,3,4,4,5,5-octadeuteriooxolane
print(standardize_solvent("CDCl3"))  # Outputs: trichloro(deuterio)methane
print(standardize_solvent("Toluene"))  # Outputs: toluene
print(standardize_solvent("t0luene"))  # Outputs: t0luene

