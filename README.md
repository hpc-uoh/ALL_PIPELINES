# ALL_PIPELINES

This repository gathers the pipelines available in the `AGENslab` and `digenoma-lab` directories.

## Automatic Update

This file can now be regenerated automatically with `scripts/update_readme.py`. The workflow `.github/workflows/update-readme.yml` is configured to refresh it daily and also supports manual execution from GitHub Actions.

## Criteria Used In This Table

- **Version**: extracted from `nextflow.config`, `pyproject.toml`, `setup.py`, or the `README` when available.
- **Status**: inferred from the repository structure and explicit notes in the `README`. `Active` indicates an executable pipeline with workflow and documentation; `In development`, a pipeline under construction; `Documented`, a repository with documentation or associated analysis; `Experimental`, auxiliary material, a demo, or a template.
- **Tools**: summarized from the `README`, manifests, and the main project files.

## AGENslab Pipelines

| Pipeline Name | Latest Version | Status | Description | Tools Used |
|---|---|---|---|---|
| [**Basecalling**](https://github.com/AGENslab/Basecalling) | 0.0.1 | Active | This Nextflow pipeline performs Nanopore basecalling using Dorado and downstream sequence statistics with SeqKit. It supports both FAST5 and POD5... | Nextflow, Dorado, Pod5 Tools, SeqKit, Slurm |
| [**BrumiR-Fungi**](https://github.com/AGENslab/BrumiR-Fungi) | 0.1.1 | Active | Pipeline for identifying candidate miRNAs in fungi from FASTQ data. | Nextflow, fastp, BrumiR, Slurm |
| [**mask2braker**](https://github.com/AGENslab/mask2braker) | 0.1.0 | Active | This repository contains a Nextflow pipeline for the analysis, annotation, and evaluation of genes in de novo genomes. The workflow... | Nextflow, windowmasker, BRAKER3, BUSCO, UniProt |
| [**miR-DE-cancer**](https://github.com/AGENslab/miR-DE-cancer) | No declared version | Documented | This repository contains an RStudio workflow for differential expression analysis of microRNAs (miRNAs) in cancer projects... | RStudio, R, edgeR, multiMiR |
| [**MiRScout**](https://github.com/AGENslab/MiRScout) | 0.1.1 | Active | MiRScout is a Nextflow DSL2 pipeline for miRNA candidate discovery using dual trimming strategies and BrumiR-based prediction. | Nextflow, fastp, cutadapt, BrumiR, Random Forest |
| [**nextflow-template**](https://github.com/AGENslab/nextflow-template) | 0.1.0 | Experimental | This pipeline is a minimal Nextflow DSL2 template with modules, workflows, and a main file. It only uses echo to show how data flows... | Nextflow, Slurm |
| [**nf-assembly**](https://github.com/AGENslab/nf-assembly) | 0.1.0 | Active | nf-assembly is a modular pipeline built with Nextflow DSL2, designed for genome assembly, scaffolding, and annotation — particularly suited for... | Nextflow, Slurm, Hifiasm, RagTag, GFAtools |
| [**nf_rna_align**](https://github.com/AGENslab/nf_rna_align) | 1.0.0 | Active | This pipeline automates the preprocessing, alignment, and quantification stages for long-read RNA-seq data. It is implemented in... | Nextflow, fastp, Slurm, BWA, FastQC |
| [**Prediccion-de-interacciones-miRNA-mRNA**](https://github.com/AGENslab/Prediccion-de-interacciones-miRNA-mRNA) | 1.0 | Documented | This repository contains code developed for a thesis that implements and evaluates deep learning models aimed at predicting... | Keras, Transformer |
| [**Python_learning-Sesion_1**](https://github.com/AGENslab/Python_learning-Sesion_1) | No declared version | Experimental | Date: 2025-08-22. Instructors: Dr. Carol Moraga and Eng. Felipe Gomez | Python |
| [**sarcopipe**](https://github.com/AGENslab/sarcopipe) | 0.1.1 | Active | Sarcopipe is a Nextflow pipeline designed for the identification and linkage of miRNAs and mRNAs, specifically tailored for analyzing Sarcopenia... | Nextflow, fastp, BrumiR, Slurm, miRDeep2 |
| [**StressPathways**](https://github.com/AGENslab/StressPathways) | No declared version | Documented | Identification of genes involved in different stress pathways | Not specified |

## digenoma-lab Pipelines

| Pipeline Name | Latest Version | Status | Description | Tools Used |
|---|---|---|---|---|
| [**alignment-nf**](https://github.com/digenoma-lab/alignment-nf) | 1.0 | Active | [](https://singularity-hub.org/collections/4522) | Nextflow, R, BWA, GATK, Samtools |
| [**alndv**](https://github.com/digenoma-lab/alndv) | 0.0.1 | Active | A nextflow (DSL 2) Whole‑Genome Short‑Read Pipeline (BWA‑MEM2 → DeepVariant → GLnexus) for small‑variant discovery from paired‑end FASTQ files. | Nextflow, Slurm, BWA, FastQC, Samtools |
| [**alndvs**](https://github.com/digenoma-lab/alndvs) | No declared version | Documented | Somatic point mutation calling for matched and tumor-only samples | Not specified |
| [**alnsl**](https://github.com/digenoma-lab/alnsl) | 0.0.1 | Active | A nextflow pipeline for alignment of short WGS reads. | Nextflow, Slurm, BWA, FastQC, Samtools |
| [**ampliconarchitect-nf**](https://github.com/digenoma-lab/ampliconarchitect-nf) | 1.0 | Active | Nextflow pipeline to discover ecDNA in cancer genomes. | Nextflow, PURPLE, AmpliconArchitect |
| [**analisis-paper-cancer**](https://github.com/digenoma-lab/analisis-paper-cancer) | No declared version | Experimental | R code | Not specified |
| [**AncestryInference**](https://github.com/digenoma-lab/AncestryInference) | 0.0.1 | Active | Nextflow pipeline for global and local ancestry inference, with QC and visualisation of the correlation between local (LAI) and global (GAI)... | Nextflow, Slurm, bcftools |
| [**annotsv**](https://github.com/digenoma-lab/annotsv) | 1.0 | Active | Software to annotate human structural variants | Nextflow, Slurm |
| [**assemblies**](https://github.com/digenoma-lab/assemblies) | No declared version | Documented | Repository with documentation in Rmarkdown for genome assemlies | R |
| [**assemblyStats**](https://github.com/digenoma-lab/assemblyStats) | 1.0.0 | Active | Genome Informatics Facility \| [](https://www.nextflow.io/) | Nextflow, BUSCO, Slurm |
| [**bacannot**](https://github.com/digenoma-lab/bacannot) | 3.2 | Active | [](https://github.com/fmalmeida/bacannot/releases) | Nextflow, Python, RStudio, R, Bakta |
| [**bam2cram**](https://github.com/digenoma-lab/bam2cram) | 2.0 | Active | A repository to convert BAM->CRAM files | Nextflow, Slurm, STAR, Samtools |
| [**bhap**](https://github.com/digenoma-lab/bhap) | 0.1.0 | Active | bhap is a Bayesian classifier designed to assign haplotype labels (A, B, or U) to genomic reads based on k-mer count data. It models k-mer... | Python |
| [**biomining_mags**](https://github.com/digenoma-lab/biomining_mags) | No declared version | Documented | Analysis of eight metagenomic samples sequenced via Illumina (short reads), obtained from the Cauquenes copper tailing (located in central Chile),... | Nextflow, fastp, BWA, Bakta |
| [**biomining_metagenomes**](https://github.com/digenoma-lab/biomining_metagenomes) | No declared version | Documented | Repository that holds data, scripts and figures regarding to the mining MAGs (Cauquenes tailing) article: "Genome-resolved metagenomics and... | Nextflow, BWA, CheckM, Samtools |
| [**BRCA**](https://github.com/digenoma-lab/BRCA) | No declared version | Active | A Nextflow pipeline for processing target NGS BRCA data | Nextflow, BWA, FastQC, Samtools, Qualimap |
| [**BRCA12_ms**](https://github.com/digenoma-lab/BRCA12_ms) | No declared version | Documented | Code for figure and analysis of BRCA12 ms | Nextflow |
| [**breast_cancer**](https://github.com/digenoma-lab/breast_cancer) | No declared version | Documented | repo holding files for the analysis of 120 WGS of breast cancer patients | Not specified |
| [**call_snv**](https://github.com/digenoma-lab/call_snv) | 1.0 | Active | Nextflow pipeline for the identification of Single Nucleotide Variants (SNVs) from short-read sequences. | Nextflow, Python, Slurm, Manta, Samtools |
| [**cancer_histology**](https://github.com/digenoma-lab/cancer_histology) | No declared version | Documented | Unlike genomic information, histological images of cancer patients are a simpler method of obtaining information. In particular, H&E method images... | Not specified |
| [**CHI-DT**](https://github.com/digenoma-lab/CHI-DT) | No declared version | Documented | Data Note paper of Chilean genomes | Not specified |
| [**CHI-T2T**](https://github.com/digenoma-lab/CHI-T2T) | No declared version | Documented | Repo with analysis and data for the human genome paper. | Not specified |
| [**covid_genomics**](https://github.com/digenoma-lab/covid_genomics) | No declared version | Documented | Repository holding analysis of 100 covid chilean genomes | Not specified |
| [**CRAB-MIL**](https://github.com/digenoma-lab/CRAB-MIL) | No declared version | Documented | This repository reproduces the results in the paper. | Python |
| [**crc_omics**](https://github.com/digenoma-lab/crc_omics) | No declared version | Documented | No clear description in README. | Not specified |
| [**data-TARA**](https://github.com/digenoma-lab/data-TARA) | No declared version | Experimental | Repository for integrated MetaTranscriptomics (MetaT), Metagenomics (MetaG), and Taxonomy analyses from the TARA Chile project. It contains the objects... | RStudio |
| [**DGL_TAT**](https://github.com/digenoma-lab/DGL_TAT) | No declared version | Documented | Repository with assorted documentation of processes run by the digenoma lab on different computing clusters | Not specified |
| [**dgl_workflows**](https://github.com/digenoma-lab/dgl_workflows) | No declared version | Experimental | Repo with documentation about the different workflows of digenomalab | Bakta |
| [**DifferentialMethylationRegions**](https://github.com/digenoma-lab/DifferentialMethylationRegions) | 0.0.1 | Active | Nextflow pipeline to preprocess modkit-style BEDs, build common CpG sets per chromosome, run differential methylation (DSS, multi-factor) and... | Nextflow, R, Slurm, bcftools, bedtools |
| [**dipdiff-nf**](https://github.com/digenoma-lab/dipdiff-nf) | 1.0 | Active | Nextflow for running dipdiff | Nextflow, STAR, Wengan, minimap2, Samtools |
| [**discovarexp-51885**](https://github.com/digenoma-lab/discovarexp-51885) | No declared version | Documented | This repo contains a copy of the DiscovarDenovo short-read assembler developed by Broad Institute. The repo is a mirror of discovarexp-51885 | Not specified |
| [**Eval-RF-hap**](https://github.com/digenoma-lab/Eval-RF-hap) | 0.0.1 | Active | Eval-RF-hap is a Nextflow pipeline designed to evaluate the haplotyping performance of RFhap (or whatever other model to separate haplotypes),... | Nextflow, Slurm, Hifiasm, Nanopore |
| [**EWAS**](https://github.com/digenoma-lab/EWAS) | No declared version | Documented | Epigenetic wide association study | Not specified |
| [**facets-nf**](https://github.com/digenoma-lab/facets-nf) | 2.0 | Active | Table of Contents ================= Description Usage Dependencies Input (mandatory) + Example of Tumor/Normal pairs file (--tn_file) * Parameters | Nextflow, Slurm, somalier |
| [**fast-sg**](https://github.com/digenoma-lab/fast-sg) | 5.3 | Documented | Fast-SG is an alignment-free algorithm for ultrafast scaffolding graph construction from short or long reads. | Not specified |
| [**fast_hybrid_polising**](https://github.com/digenoma-lab/fast_hybrid_polising) | 0.1 | Active | nextflow run main.nf --long_reads ./test/long-reads --short_reads ./test/short-reads --outdir results --debug true | Nextflow, Slurm, Racon, minimap2 |
| [**FastKM**](https://github.com/digenoma-lab/FastKM) | No declared version | Documented | FastKM is a lightweight C++ tool for fast k-mer marker lookup in long reads using a minimal perfect hash function (MPHF) and a compact... | Not specified |
| [**fastmin-sg**](https://github.com/digenoma-lab/fastmin-sg) | No declared version | Documented | [](http://hits.dwyl.io/adigenova/fastmin-sg) | Wengan, minimap2 |
| [**fastqc-nf**](https://github.com/digenoma-lab/fastqc-nf) | No declared version | Active | [](https://singularity-hub.org/collections/4559) | Nextflow, FastQC, Samtools |
| [**fchims**](https://github.com/digenoma-lab/fchims) | No declared version | Documented | Github with code for aseembly, annotation, methylation and variants. | Not specified |
| [**fragaria_poster_figures**](https://github.com/digenoma-lab/fragaria_poster_figures) | No declared version | Experimental | No clear description in README. | Not specified |
| [**functional_enrichment**](https://github.com/digenoma-lab/functional_enrichment) | 0.0.1 | Active | This pipeline performs functional enrichment analysis using GWAS data and local references. | Slurm, bcftools |
| [**Gallbladder_WGS**](https://github.com/digenoma-lab/Gallbladder_WGS) | No declared version | Documented | Figures and analysis for Gallbladder manuscript | PURPLE |
| [**genome_assembly_tools**](https://github.com/digenoma-lab/genome_assembly_tools) | No declared version | Documented | Scripts to manipulate files associated to genome assembly | Not specified |
| [**Germline-StructuralV-nf**](https://github.com/digenoma-lab/Germline-StructuralV-nf) | 1.0 | In development | wrench: This pipeline is currently under development :wrench | Nextflow, BWA, Manta, Samtools, bcftools |
| [**GWAS**](https://github.com/digenoma-lab/GWAS) | 0.0.1 | Active | A comprehensive Nextflow pipeline for Genome-Wide Association Studies (GWAS) including quality control, association analysis, and visualization. | Nextflow, Python, Slurm, Samtools, bcftools |
| [**hapdup-nf**](https://github.com/digenoma-lab/hapdup-nf) | 1.0 | Active | Nextflow pipeline for running HapDup for haplotype assembly. | Nextflow, STAR, Wengan, minimap2, Samtools |
| [**HBW**](https://github.com/digenoma-lab/HBW) | No declared version | Documented | HBW is a repository hold code for implementing trio-based binning and bubble graph approaches to diploid assembly but for hybrid genomic datasets... | Wengan |
| [**hic-scaffolding-nf**](https://github.com/digenoma-lab/hic-scaffolding-nf) | 1.0 | Active | A Nextflow pipeline for scaffolding genome assemblies using Hi-C reads with [CHROMAP][chromap], [YAHS][yahs], and [Juicer Tools][juicer_tools]. | Nextflow, Slurm, Samtools |
| [**HistologyFeatureExtraction**](https://github.com/digenoma-lab/HistologyFeatureExtraction) | 0.0.1 | Active | A Nextflow pipeline for extracting features from histology whole slide images (WSI) using multiple patch and slide encoders via TRIDENT. | Nextflow, Python, Slurm, OpenCV, PyTorch |
| [**HistologyLinearProbing**](https://github.com/digenoma-lab/HistologyLinearProbing) | 0.0.1 | Active | Linear probing pipeline for histopathology to evaluate different feature extractors (foundation models) using Elastic Net classification on genes... | Nextflow, Python, R, Slurm, scikit-learn |
| [**HistologyMultiInstanceLearning**](https://github.com/digenoma-lab/HistologyMultiInstanceLearning) | 0.0.1 | Experimental | Multi-Instance Learning (MIL) pipeline for histopathology to evaluate different MIL architectures (ABMIL, CLAM, DSMIL, etc.) using pre-extracted... | Nextflow, Python, Slurm, Transformer |
| [**HistoMILTrainer**](https://github.com/digenoma-lab/HistoMILTrainer) | 1.1 | Active | A library for training Multi-Instance Learning (MIL) architectures from MIL-Lab on histology datasets. HistoMILTrainer provides a unified... | Python, Slurm, PyTorch, scikit-learn, Transformer |
| [**hrr_analisis_er**](https://github.com/digenoma-lab/hrr_analisis_er) | No declared version | Documented | ER analysis description | Not specified |
| [**HRR_histology**](https://github.com/digenoma-lab/HRR_histology) | No declared version | Documented | This project contains a descriptive analysis of breast biopsy data from the Hospital Regional de Rancagua. The workflow includes data cleaning,... | R |
| [**ImputeVariants**](https://github.com/digenoma-lab/ImputeVariants) | 0.0.1 | Active | ImputeVariants is a comprehensive Nextflow pipeline for genotype phasing and imputation using state-of-the-art methods. The pipeline supports two... | Nextflow, Slurm, bcftools |
| [**intervalmiss**](https://github.com/digenoma-lab/intervalmiss) | No declared version | Documented | [](http://hits.dwyl.io/adigenova/intervalmiss) | Wengan |
| [**just_align_sr**](https://github.com/digenoma-lab/just_align_sr) | 0.0.1 | Active | Just Align SR is a lightweight Nextflow pipeline designed for aligning short-read sequencing data (e.g., Illumina or MGI) using BWA-MEM. The... | Nextflow, Slurm, BWA, FastQC, Samtools |
| [**k-count-nf**](https://github.com/digenoma-lab/k-count-nf) | 1.0 | Active | A nextflow pipeline to count k-mers and estimate genome size from WGS data | Nextflow, STAR |
| [**liftover**](https://github.com/digenoma-lab/liftover) | 0.0.1 | Active | A Nextflow pipeline for lifting over genomic coordinates from one reference genome to another (e.g., hg19 to hg38 or vice versa). Supports both... | Nextflow, Slurm, Samtools, bcftools |
| [**liger**](https://github.com/digenoma-lab/liger) | No declared version | Documented | Synthetic Scaffolding Graph construction, Overlaps, Scaffolding, Validation, Gap filling and Polishing. Liger is a Wengan component. | LIGER, Wengan |
| [**LLM-RAG-Demo**](https://github.com/digenoma-lab/LLM-RAG-Demo) | No declared version | Experimental | Chat system for genetic variants using RAG with Milvus Lite and DeepSeek. | Python |
| [**longcall**](https://github.com/digenoma-lab/longcall) | 0.0.1 | Active | Longcall is a Nextflow DSL2 pipeline for Oxford Nanopore (ONT) whole-genome data that | Nextflow, Slurm, minimap2, Samtools, bcftools |
| [**longreadstats**](https://github.com/digenoma-lab/longreadstats) | 1.0dev | Active | digenoma-lab/longreadstats is a bioinformatics best-practice analysis pipeline for computing long-read statistics with Nanoplot. | Nextflow, Python, Slurm |
| [**LRnaseq_Rat**](https://github.com/digenoma-lab/LRnaseq_Rat) | No declared version | Documented | Repository with analysis of trascriptome data generated with Oxford Nanopore | Python, RStudio, Nanopore |
| [**mag**](https://github.com/digenoma-lab/mag) | 2.3.0 | Active | nf-core/mag is a bioinformatics best-practise analysis pipeline for assembly, binning and annotation of metagenomes. | Nextflow, fastp, Python, BUSCO, FastQC |
| [**MAG_ONT**](https://github.com/digenoma-lab/MAG_ONT) | No declared version | Documented | Chron metagenomic analysis of ONT data | Not specified |
| [**mesomic_data_note**](https://github.com/digenoma-lab/mesomic_data_note) | No declared version | Experimental | Repository with code and datasets used in the mesomics data note manuscript. | Not specified |
| [**methont**](https://github.com/digenoma-lab/methont) | 0.1 | Active | The methont pipeline is designed to process long-read sequencing data for DNA methylation analysis. It includes alignment, variant calling,... | Nextflow, Slurm, minimap2, Samtools |
| [**MethylationPCA**](https://github.com/digenoma-lab/MethylationPCA) | 0.0.1 | Active | Pipeline Nextflow para preprocesar archivos BED de metilación de CpG y ejecutar un análisis de componentes principales (PCA) sobre la matriz de... | Nextflow, Slurm |
| [**minibusco-nf**](https://github.com/digenoma-lab/minibusco-nf) | 0.0.1 | Active | A simple and scalable Nextflow pipeline to compute genome or transcriptome quality metrics using minibusco. This pipeline is designed for... | Nextflow, BUSCO, Slurm |
| [**mitoH**](https://github.com/digenoma-lab/mitoH) | 7.505 | Documented | Mitocondrial genome analysis | Samtools |
| [**mocancer**](https://github.com/digenoma-lab/mocancer) | No declared version | Documented | Multi-omic analysis of cancer data | Not specified |
| [**mutect-nf**](https://github.com/digenoma-lab/mutect-nf) | 3 | Active | [](https://singularity-hub.org/collections/4357) | Nextflow, Python, GATK, Mutect2, bedtools |
| [**MutSig**](https://github.com/digenoma-lab/MutSig) | No declared version | Active | Mutational signature analysis of WGS data. This repo constains simple scripts to perform mutational signatures analysis using SigProfilerExtractor | Python, PURPLE |
| [**nextflow**](https://github.com/digenoma-lab/nextflow) | No declared version | Documented | "Dataflow variables are spectacularly expressive in concurrent programming" Henri E. Bal , Jennifer G. Steiner , Andrew S. Tanenbaum | Nextflow, Slurm, Samtools |
| [**nf-bakta**](https://github.com/digenoma-lab/nf-bakta) | 1.0 | Active | A Nextflow pipeline for the annotation of bacterial genomes or MAGs running Bakta. | Nextflow, Python, UniProt, Slurm, Bakta |
| [**nf-gene-fusions**](https://github.com/digenoma-lab/nf-gene-fusions) | 1.1 | Active | A nextflow pipeline to call somatic rna fusions from RNA-seq data using arriba | Nextflow, STAR, Samtools |
| [**nf-groot**](https://github.com/digenoma-lab/nf-groot) | No declared version | Active | A Nextflow pipeline for running Groot, which is a tool to type Antibiotic Resistance Genes (ARGs) in metagenomic samples. | Nextflow, Slurm |
| [**nf-hla-neo**](https://github.com/digenoma-lab/nf-hla-neo) | 1.0 | Active | Pipeline to predict neoantigens from WGS of T/N pairs | Nextflow, BWA, PURPLE, bcftools |
| [**nf-mag-depths**](https://github.com/digenoma-lab/nf-mag-depths) | No declared version | Active | A nextflow pipeline to calculate depth of coverage from a metagenomic set of bins. | Nextflow, BWA, MetaBAT, Samtools |
| [**nf-mutect2**](https://github.com/digenoma-lab/nf-mutect2) | 0.0.1 | Active | Somatic SNV/indel calling with GATK Mutect2 for WGS (hg38), including optional Panel of Normals (PON), scatter/gather sharding, and filtering.... | Nextflow, Slurm, BWA, FastQC, GATK |
| [**nf-ngscheckmate**](https://github.com/digenoma-lab/nf-ngscheckmate) | No declared version | Active | Nextflow workflow running NGSCheckMate | Nextflow, Slurm, NGSCheckMate |
| [**nf-ssvsr**](https://github.com/digenoma-lab/nf-ssvsr) | 0.3.0 | Active | Simplified local Nextflow DSL2 workflow for | Nextflow, Python, Slurm, BWA, GATK |
| [**nf-wengan**](https://github.com/digenoma-lab/nf-wengan) | No declared version | Documented | A nexflow workflow for wengan | Wengan |
| [**oncovirus**](https://github.com/digenoma-lab/oncovirus) | No declared version | Documented | prediction of somatic virus integration from WGS using hmftools | Not specified |
| [**ontmeth-nf**](https://github.com/digenoma-lab/ontmeth-nf) | No declared version | Active | Nextflow pipeline to compute methylation from Nanopore data | Nextflow, Python, BWA, Samtools, Nanopore |
| [**ontpolish**](https://github.com/digenoma-lab/ontpolish) | No declared version | Documented | Polishing long-read assemblies | Not specified |
| [**Phasing**](https://github.com/digenoma-lab/Phasing) | 0.0.1 | Active | A Nextflow pipeline for phasing unphased genotype data using Beagle with reference panels from the 1000 Genomes Project. | Nextflow, Slurm, Samtools, bcftools |
| [**ppilon**](https://github.com/digenoma-lab/ppilon) | 1.0 | Active | No clear description in README. | Nextflow, Slurm, BWA, STAR, Pilon |
| [**PrincipalComponentAnalysis**](https://github.com/digenoma-lab/PrincipalComponentAnalysis) | 0.0.1 | Active | Principal Component Analysis pipeline for genomic data, specifically designed for Chilean datasets or population-specific studies. The workflow... | Nextflow, Slurm, bcftools |
| [**prok-annotate**](https://github.com/digenoma-lab/prok-annotate) | 3.0.0 | Active | A Nextflow pipeline for the functional annotation of prokaryotic genomes and metagenomes. | Nextflow, Python, Prokka |
| [**prok-classify**](https://github.com/digenoma-lab/prok-classify) | 1.3.0 | Active | metashot/prok-classify is a workflow for assigning objective taxonomic classifications to bacterial and archaeal genomes using GTDB-Tk and the... | Nextflow |
| [**purple-nf**](https://github.com/digenoma-lab/purple-nf) | 1.0 | Active | Nextflow pipeline for CNV calling with PURPLE | Nextflow, PURPLE, bcftools |
| [**qualimap-nf**](https://github.com/digenoma-lab/qualimap-nf) | 1.0 | Active | The Qualimap pipeline processes sequencing data in a fast and efficient manner using Nextflow, a workflow management system. It takes aligned... | Nextflow, Python, Slurm, Samtools, Qualimap |
| [**quant_mags**](https://github.com/digenoma-lab/quant_mags) | No declared version | Active | Quantify MAGs abundance (metaG) and gene expression (metaT) | Nextflow, Python |
| [**quantmetaT**](https://github.com/digenoma-lab/quantmetaT) | No declared version | Active | Quantifies paired-end metatranscriptome reads using Salmon and outputs merged TPM and raw count matrices for all samples. | Nextflow, Slurm |
| [**racon**](https://github.com/digenoma-lab/racon) | No declared version | Documented | [](https://github.com/lbcb-sci/racon/releases/latest) [](https://travis-ci.com/lbcb-sci/racon) | Python, STAR, Racon, Nanopore |
| [**RF-mut-tumor-only**](https://github.com/digenoma-lab/RF-mut-tumor-only) | 1.0 | Documented | El llamado de variantes con muestras pareadas de tejido tumoral y normal es más confiable que el llamado de variantes con muestras de tumor... | RStudio, R, bcftools |
| [**rfhap**](https://github.com/digenoma-lab/rfhap) | 0.0.2 | Active | A Nextflow pipeline for long-read phasing in trio datasets, leveraging multiple k-mers and a random forest classifier. | Nextflow, Random Forest, Slurm, Hifiasm |
| [**rfhap_ms**](https://github.com/digenoma-lab/rfhap_ms) | No declared version | Documented | Figures and analysis for RFHAP manuscript | Not specified |
| [**seqtk**](https://github.com/digenoma-lab/seqtk) | No declared version | Documented | Introduction | Not specified |
| [**SMAGdb**](https://github.com/digenoma-lab/SMAGdb) | No declared version | Documented | The soid metagenome data base and analysis toolkit | Not specified |
| [**snps_mags**](https://github.com/digenoma-lab/snps_mags) | 0.0.1 | Active | snps_mags is a Nextflow pipeline designed for calling point mutations in Metagenome-Assembled Genomes (MAGs) using InStrain. The pipeline... | Nextflow, Slurm, BWA, FastQC, Samtools |
| [**somalier-nf**](https://github.com/digenoma-lab/somalier-nf) | No declared version | Active | Minimal Nextflow DSL2 pipeline for somalier, the pipeline include | Nextflow, Slurm, somalier |
| [**somatic_point_mutations**](https://github.com/digenoma-lab/somatic_point_mutations) | 1.0 | Active | This repository provides a Nextflow pipeline for calling somatic point mutations from tumor/normal pairs using Whole Genome Sequencing (WGS) or... | Nextflow, Python, Slurm, Manta, bcftools |
| [**SomaticVariantCalling**](https://github.com/digenoma-lab/SomaticVariantCalling) | 0.0.1 | Active | A Nextflow (DSL 2) pipeline that takes pre‑aligned whole‑genome CRAM files and runs DeepVariant (autosomes only) followed by GLnexus cohort merging. | Nextflow, Slurm, Qualimap |
| [**spg**](https://github.com/digenoma-lab/spg) | 1.0 | Active | Simple Pan-Genome workflow for MAGs. | Nextflow, Python, Slurm, MetaBAT, Prokka |
| [**strelka2-nf**](https://github.com/digenoma-lab/strelka2-nf) | No declared version | Active | [](https://singularity-hub.org/collections/4622) | Nextflow, Strelka2, bcftools |
| [**Summer_Course_ML**](https://github.com/digenoma-lab/Summer_Course_ML) | No declared version | Experimental | Material for the CMM summer course | Not specified |
| [**SV_Delly_Germline**](https://github.com/digenoma-lab/SV_Delly_Germline) | 1.0 | Active | This pipeline identifies germline structural variants (SVs) — deletions, duplications, inversions, insertions, and translocations — from... | Nextflow, Slurm, Delly, bcftools |
| [**sv_somatic_cns**](https://github.com/digenoma-lab/sv_somatic_cns) | 1.0 | Active | Consensus calling of Somatic Structural variants from Paired WGS | Nextflow, Python, BWA, Manta, Delly |
| [**svlr**](https://github.com/digenoma-lab/svlr) | 1.0 | Active | A nextflow Structural variant calling workflow for long-reads | Nextflow, Slurm, minimap2, Samtools |
| [**svlr_somatic**](https://github.com/digenoma-lab/svlr_somatic) | 1.0 | Active | A Nextflow pipeline for somatic structural variant (SV) calling using long-read sequencing data. | Nextflow, Slurm, minimap2, Samtools |
| [**systemix_mag_analysis**](https://github.com/digenoma-lab/systemix_mag_analysis) | No declared version | Documented | Repository holding analysis and figures to understand MAG (Metagenome-Assembled Genome) data. | Nextflow, RStudio, CheckM, Bakta, Prokka |
| [**TARA-Chile**](https://github.com/digenoma-lab/TARA-Chile) | No declared version | Documented | Genomics of TARA Ocean Chile expedition | Not specified |
| [**viralrecon**](https://github.com/digenoma-lab/viralrecon) | 2.5 | Active | nf-core/viralrecon is a bioinformatics analysis pipeline used to perform assembly and intra-host/low-frequency variant calling for viral samples.... | Nextflow, fastp, cutadapt, Python, FastQC |
| [**wengan**](https://github.com/digenoma-lab/wengan) | No declared version | Documented | [](http://hits.dwyl.io/adigenova/wengan) | LIGER, Wengan, Nanopore |
| [**wengan_demo**](https://github.com/digenoma-lab/wengan_demo) | 0.2 | Experimental | This repository contains a test dataset and the instructions to run Wengan (version 0.2). | Wengan, Nanopore |

> Note: some projects do not explicitly declare a version or tools; in those cases, the best possible inference is shown based on the content available in the repository.
# ALL_PIPELINES
