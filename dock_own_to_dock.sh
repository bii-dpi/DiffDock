echo "[1/3] Generating protein-ligand paths CSV."
python create_csvs.py

echo "[2/3] Generating embeddings with ESM2."
python datasets/esm_embedding_preparation.py --protein_ligand_csv own_to_dock/protein_ligand_paths.csv --out_file own_to_dock/prepared_for_esm.fasta
HOME=esm/model_weights python esm/scripts/extract.py esm2_t33_650M_UR50D own_to_dock/prepared_for_esm.fasta data/esm2_output --repr_layers 33 --include per_tok

echo "[3/3] Running inference."
python -m inference --protein_ligand_csv own_to_dock/protein_ligand_paths.csv --out_dir own_to_dock/user_predictions --inference_steps 20 --samples_per_complex 40 --batch_size 10 --actual_steps 18 --no_final_step_noise

