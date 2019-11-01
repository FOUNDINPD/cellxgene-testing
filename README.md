# Cellxgene Test README
11/01/2019
Michelle Webb

The scRNA visualization tool cellxgene currently accepts .h5ad formatted files as input. The scripts in this directory show how to convert a seurat object .RDS file to .h5ad for visualization. The process entails conversion from seurat object to loom in R, followed by conversion of loom to scanpy AnnData format in python. 

Alternatively,
One can create .h5ad files for individual samples by running 
`cellxgene prepare [pathTo10xDirectory] --output [outputFile.h5ad]`

To visualize an .h5ad file using cellxgene locally:
`cellxgene launch [outputFile.h5ad] --open`

Scripts tested with:
R 3.6.1
seurat 3.1.0
loomR 0.2.1.9000

Python 3.7.4
pandas 0.25.1
scanpy 1.4.4.post1
cellxgene 0.12.0

Cellxgene: https://chanzuckerberg.github.io/cellxgene/            
AnnData: https://icb-anndata.readthedocs-hosted.com/en/stable/anndata.AnnData.html      
Loom: http://loompy.org/         
