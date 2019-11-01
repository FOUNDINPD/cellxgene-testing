import scanpy as sc
import pandas as pd

#define output file
results_file = 'file.h5ad'

# Read in loom data
data = sc.read_loom(integratedData.loom')

# Read in metadata
# Ensure that dataframe dimensions match data.obs 

metadata = pd.read_csv('metaData.csv')

# Rename Cell Batch column to match metadata file
data.obs['CDI_DZNE'] = data.obs.pop('')
pd.merge(data.obs, metadata, by = 'CDI_DZNE')

# Rename seurat embeddings to match cellxgene convention
data.obs['X_pca'] = data.obsm.pop('pca_cell_embeddings')
data.obs['X_tsne'] = data.obsm.pop('tsne_cell_embeddings')
data.obs['X_umap'] = data.obsm.pop('umap_cell_embeddings')

adata.write(results_file)
