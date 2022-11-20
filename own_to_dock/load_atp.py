from rdkit import Chem

mol = Chem.MolFromMol2File("atp.mol2", sanitize=False, removeHs=True,
cleanupSubstructures=False)
print(mol)
print(Chem.rdmolops.DetectChemistryProblems(mol))
#Chem.SanitizeMol(mol)
