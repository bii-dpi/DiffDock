import os
import glob


# Relative path of folder with PDBs and MOL2s to dock pairwise.
DATA_DIR = "own_to_dock"


def get_all_files(extension):
    """Return all file paths in DATA_DIR with the required extension."""

    return glob.glob(f"{DATA_DIR}/*.{extension}")


all_pdbs = get_all_files("pdb")
all_mol2s = get_all_files("mol2")

# Write the rows to dock every ligand into each protein.
rows = ["protein_path,ligand"]
for pdb in all_pdbs:
    for mol2 in all_mol2s:
        rows.append(f"{pdb},{mol2}")

with open(f"{DATA_DIR}/protein_ligand_paths.csv", "w") as f:
    f.write("\n".join(rows))

