# .CDS Seurat object to Loom
library(Seurat)
library(loomR)

# Read in Seurat object containing two assays: 
# RNA (27261 features), Integrated (2000 features)
integratedData <- readRDS("file.RDS")
DefaultAssay(integratedData) <- "integrated"

# Write seurat object to loom format 
integratedData.loom <- as.loom(integratedData,filename = "integratedData.loom")

# Close loom file
integratedData.loom$close_all()
