# ALL_PIPELINES

This repository gathers pipeline-like repositories published under the `AGENslab` and `digenoma-lab` GitHub organizations.

## Automatic Update

This file is generated automatically by `scripts/update_readme.py` using the GitHub API. If `GH_ORG_READ_TOKEN` is configured, private repositories from the tracked organizations are included as well.
The GitHub Actions workflow `.github/workflows/update-readme.yml` refreshes it on a schedule and can also be triggered manually.

## Criteria Used In This Table

- **Version**: extracted from GitHub releases, tags, `nextflow.config`, `pyproject.toml`, `setup.py`, or the `README` when available.
- **Status**: inferred from repository structure and explicit notes in the `README`. `Active` indicates an executable pipeline with workflow and documentation; `In development`, a pipeline under construction; `Documented`, a repository with documentation or associated analysis; `Experimental`, auxiliary material, a demo, or a template.
- **Tools**: summarized from the `README`, manifests, and the main project files detected at the repository root.

## AGENslab Pipelines

| Pipeline Name | Latest Version | Status | Description | Tools Used |
|---|---|---|---|---|
| [**Basecalling**](https://github.com/AGENslab/Basecalling) | 0.0.1 | Active | This Nextflow pipeline performs Nanopore basecalling using Dorado and downstream sequence statistics with SeqKit. It supports both FAST5 and POD5... | Nextflow, Dorado, Pod5 Tools, SeqKit, Slurm |
| [**BrumiR-Fungi**](https://github.com/AGENslab/BrumiR-Fungi) | v1 | Active | Pipeline para la identificación de miRNAs candidatos en hongos a partir de datos FASTQ. | Nextflow, fastp, BrumiR, Slurm |
| [**mask2braker**](https://github.com/AGENslab/mask2braker) | 0.1.0 | Active | Este repositorio contiene un pipeline desarrollado en Nextflow para el análisis, anotación y evaluación de genes en genomas de novo. El flujo de... | Nextflow, windowmasker, BRAKER3, BUSCO, UniProt |
| [**miR-DE-cancer**](https://github.com/AGENslab/miR-DE-cancer) | No declared version | Documented | Este repositorio contiene un flujo de trabajo desarrollado en RStudio para el análisis de expresión diferencial de microRNAs (miRNAs) en proyectos... | RStudio, R, edgeR, multiMiR |
| [**MiRScout**](https://github.com/AGENslab/MiRScout) | 0.1.1 | Active | MiRScout is a Nextflow DSL2 pipeline for miRNA candidate discovery using dual trimming strategies and BrumiR-based prediction. | Nextflow, fastp, cutadapt, BrumiR, Random Forest |
| [**nextflow-template**](https://github.com/AGENslab/nextflow-template) | 0.1.0 | Experimental | Este pipeline es un template mínimo de Nextflow DSL2 con módulos, workflows y un archivo principal. Solo utiliza echo para mostrar cómo fluyen los... | Nextflow, Slurm |
| [**nf-assembly**](https://github.com/AGENslab/nf-assembly) | v1.0.0 | Active | nf-assembly is a modular pipeline built with Nextflow DSL2, designed for genome assembly, scaffolding, and annotation — particularly suited for... | Nextflow, Slurm, Hifiasm, RagTag, GFAtools |
| [**nf_rna_align**](https://github.com/AGENslab/nf_rna_align) | 1.0.0 | Active | Este pipeline automatiza las etapas de preprocesamiento, alineamiento y cuantificación de lecturas largas de RNA-seq. Está desarrollado en... | Nextflow, fastp, Slurm, BWA, FastQC |
| [**Prediccion-de-interacciones-miRNA-mRNA**](https://github.com/AGENslab/Prediccion-de-interacciones-miRNA-mRNA) | No declared version | Documented | Este repositorio contiene el código desarrollado para una tesis que implementa y evalúa modelos de Deep Learning orientados a predecir... | Keras, Transformer |
| [**Python_learning-Sesion_1**](https://github.com/AGENslab/Python_learning-Sesion_1) | No declared version | Experimental | Fecha: 22/08/2025 Docentes: Dra. Carol Moraga e Ing. Felipe Gómez | Python |
| [**QualityTranscriptome**](https://github.com/AGENslab/QualityTranscriptome) | No declared version | Documented | Evaluation of quality of the assembly using RNA-Seq read representation | Not specified |
| [**sarcopipe**](https://github.com/AGENslab/sarcopipe) | 0.1.1 | Active | Sarcopipe is a Nextflow pipeline designed for the identification and linkage of miRNAs and mRNAs, specifically tailored for analyzing Sarcopenia... | Nextflow, fastp, BrumiR, Slurm, miRDeep2 |
| [**StressPathways**](https://github.com/AGENslab/StressPathways) | No declared version | Documented | identification of participant genes in different stress pathways | Not specified |

## digenoma-lab Pipelines

| Pipeline Name | Latest Version | Status | Description | Tools Used |
|---|---|---|---|---|
| [**aigen2026**](https://github.com/digenoma-lab/aigen2026) | No declared version | Documented | Sitio oficial de la conferencia AIGEN 2026: IA y Genómica para la Salud Pública, construido con Hugo y preparado para despliegue en Netlify. | Not specified |
| [**alndv**](https://github.com/digenoma-lab/alndv) | v1.0 | Active | A nextflow (DSL 2) Whole‑Genome Short‑Read Pipeline (BWA‑MEM2 → DeepVariant → GLnexus) for small‑variant discovery from paired‑end FASTQ files. | Nextflow, Slurm, BWA, FastQC, Samtools |
| [**alndvs**](https://github.com/digenoma-lab/alndvs) | No declared version | Documented | Somatic point mutation calling for matched and tumor-only samples | Not specified |
| [**alnsl**](https://github.com/digenoma-lab/alnsl) | V0.1 | Active | A nextflow pipeline for alignment of short WGS reads. | Nextflow, Slurm, BWA, FastQC, Samtools |
| [**analisis-paper-cancer**](https://github.com/digenoma-lab/analisis-paper-cancer) | No declared version | Documented | R code | Not specified |
| [**AncestryInference**](https://github.com/digenoma-lab/AncestryInference) | 0.0.1 | Active | Nextflow pipeline for global and local ancestry inference, with QC and visualisation of the correlation between local (LAI) and global (GAI)... | Nextflow, Slurm, bcftools |
| [**AncestryPCA**](https://github.com/digenoma-lab/AncestryPCA) | 1.0 | Active | Ancestry PCA pipeline for genomic data, with a focus on Chilean cohorts and population-structure work alongside a reference panel (for example... | Nextflow, Slurm, bcftools |
| [**annotsv**](https://github.com/digenoma-lab/annotsv) | 1.0 | Active | Sotfware to annotate human structural variants | Nextflow, Slurm |
| [**assemblies**](https://github.com/digenoma-lab/assemblies) | No declared version | Documented | Repository with documentation in Rmarkdown for genome assemlies | R |
| [**bhap**](https://github.com/digenoma-lab/bhap) | 0.1.0 | Documented | bhap is a Bayesian classifier designed to assign haplotype labels (A, B, or U) to genomic reads based on k-mer count data. It models k-mer... | Python |
| [**biomining_mags**](https://github.com/digenoma-lab/biomining_mags) | No declared version | Documented | Analysis of eight metagenomic samples sequenced via Illumina (short reads), obtained from the Cauquenes copper tailing (located in central Chile),... | Nextflow, fastp, BWA, Bakta |
| [**biomining_metagenomes**](https://github.com/digenoma-lab/biomining_metagenomes) | No declared version | Documented | Repository that holds data, scripts and figures regarding to the mining MAGs (Cauquenes tailing) article: "Genome-resolved metagenomics and... | Nextflow, BWA, CheckM, Samtools |
| [**BRCA**](https://github.com/digenoma-lab/BRCA) | v1.0 | Active | A Nextflow pipeline for processing target NGS BRCA data | Nextflow, BWA, FastQC, Samtools, Qualimap |
| [**BRCA12_ms**](https://github.com/digenoma-lab/BRCA12_ms) | v1.0 | Documented | Code for figure and analysis of BRCA12 ms | Nextflow |
| [**breast_cancer**](https://github.com/digenoma-lab/breast_cancer) | No declared version | Documented | repo holding files for the analysis of 120 WGS of breast cancer patients | Not specified |
| [**call_snv**](https://github.com/digenoma-lab/call_snv) | 1.0 | Active | Nextflow pipeline for the identification of Single Nucleotide Variants (SNVs) from short-read sequences. | Nextflow, Python, Slurm, Manta, Samtools |
| [**cancer_histology**](https://github.com/digenoma-lab/cancer_histology) | No declared version | Experimental | Unlike genomic information, histological images of cancer patients are a simpler method of obtaining information. In particular, H&E method images... | Not specified |
| [**CHI-DT**](https://github.com/digenoma-lab/CHI-DT) | No declared version | Documented | Data Note paper of Chilean genomes | Not specified |
| [**CHI-T2T**](https://github.com/digenoma-lab/CHI-T2T) | No declared version | Documented | Repo with analysis and data for the human genome paper. | Not specified |
| [**covid_genomics**](https://github.com/digenoma-lab/covid_genomics) | v1.0 | Documented | Repository holding analysis of 100 covid chilean genomes | Not specified |
| [**CRAB-MIL**](https://github.com/digenoma-lab/CRAB-MIL) | v1.0 | Experimental | This repository reproduces the results in the paper. | Python |
| [**data-TARA**](https://github.com/digenoma-lab/data-TARA) | No declared version | Documented | Repositorio de análisis integrados MetaTranscriptómica (MetaT), MetaGenómica (MetaG) y Taxonomía del proyecto TARA Chile. Contiene los objetos... | RStudio |
| [**DGL_TAT**](https://github.com/digenoma-lab/DGL_TAT) | No declared version | Documented | Repositorio con diversa documentación de procesos ejecutados por el digenoma lab en distintos cluster de computo | Not specified |
| [**dgl_workflows**](https://github.com/digenoma-lab/dgl_workflows) | No declared version | Documented | Repo with documentation about the different workflows of digenomalab | Bakta |
| [**DifferentialMethylationRegions**](https://github.com/digenoma-lab/DifferentialMethylationRegions) | 0.0.1 | Active | Nextflow pipeline to preprocess modkit-style BEDs, build common CpG sets per chromosome, run differential methylation (DSS, multi-factor) and... | Nextflow, R, Slurm, bcftools, bedtools |
| [**dipdiff-nf**](https://github.com/digenoma-lab/dipdiff-nf) | 1.0 | Active | Nextflow for running dipdiff | Nextflow, STAR, Wengan, minimap2, Samtools |
| [**DT_Gallbladder**](https://github.com/digenoma-lab/DT_Gallbladder) | No declared version | Documented | Figures for data description of Gallbladder Cancer samples | Not specified |
| [**EpiTractor**](https://github.com/digenoma-lab/EpiTractor) | 0.1.0 | Documented | EpiTractor, a library for ancestry-based methylation DMLs. | Python |
| [**Eval-RF-hap**](https://github.com/digenoma-lab/Eval-RF-hap) | v1.0.0 | Active | Eval-RF-hap is a Nextflow pipeline designed to evaluate the haplotyping performance of RFhap (or whatever other model to separate haplotypes),... | Nextflow, Slurm, Hifiasm, Nanopore |
| [**EWAS**](https://github.com/digenoma-lab/EWAS) | No declared version | Documented | Epigenetic wide association study | Not specified |
| [**fast_hybrid_polising**](https://github.com/digenoma-lab/fast_hybrid_polising) | 0.1 | Active | nextflow run main.nf --long_reads ./test/long-reads --short_reads ./test/short-reads --outdir results --debug true | Nextflow, Slurm, Racon, minimap2 |
| [**FastKM**](https://github.com/digenoma-lab/FastKM) | v1.0 | Documented | FastKM is a lightweight C++ tool for fast k-mer marker lookup in long reads using a minimal perfect hash function (MPHF) and a compact... | Not specified |
| [**fchims**](https://github.com/digenoma-lab/fchims) | No declared version | Documented | Github with code for aseembly, annotation, methylation and variants. | Not specified |
| [**functional_enrichment**](https://github.com/digenoma-lab/functional_enrichment) | 0.0.1 | Active | This pipeline performs functional enrichment analysis using GWAS data and local references. | Slurm, bcftools |
| [**Gallbladder_WGS**](https://github.com/digenoma-lab/Gallbladder_WGS) | No declared version | Documented | Figures and analysis for Gallbladder manuscript | PURPLE |
| [**gannot**](https://github.com/digenoma-lab/gannot) | 0.0.1 | Active | Clinical grade annotation of WGS variants. | Nextflow, Slurm, bcftools |
| [**genome_assembly_tools**](https://github.com/digenoma-lab/genome_assembly_tools) | No declared version | Documented | Scripts to manipulate files associated to genome assembly | Not specified |
| [**GWAS**](https://github.com/digenoma-lab/GWAS) | 1.6 | Active | Nextflow pipeline for genome-wide association analysis and ancestry-stratified GWAS with Tractor. Global and local ancestry (ADMIXTURE + RFMix)... | Nextflow, Slurm, Samtools, bcftools |
| [**hapdup-nf**](https://github.com/digenoma-lab/hapdup-nf) | v1.0 | Active | Nextflow pipeline for running HapDup for haplotype assembly. | Nextflow, STAR, Wengan, minimap2, Samtools |
| [**HBW**](https://github.com/digenoma-lab/HBW) | No declared version | Documented | HBW is a repository hold code for implementing trio-based binning and bubble graph approaches to diploid assembly but for hybrid genomic datasets... | Wengan |
| [**HistologyFeatureExtraction**](https://github.com/digenoma-lab/HistologyFeatureExtraction) | 1.1 | Active | A Nextflow pipeline for extracting features from histology whole slide images (WSI) using multiple patch and slide encoders via TRIDENT. | Nextflow, Python, Slurm, OpenCV, PyTorch |
| [**HistologyLinearProbing**](https://github.com/digenoma-lab/HistologyLinearProbing) | 1.4 | Active | Linear probing pipeline for histopathology to evaluate different feature extractors (foundation models) using Elastic Net classification on genes... | Nextflow, Python, R, Slurm, scikit-learn |
| [**HistologyMultiInstanceLearning**](https://github.com/digenoma-lab/HistologyMultiInstanceLearning) | 1.1 | Experimental | Multi-Instance Learning (MIL) pipeline for histopathology to evaluate different MIL architectures (ABMIL, CLAM, DSMIL, etc.) using pre-extracted... | Nextflow, Python, Slurm, Transformer |
| [**HistoMILTrainer**](https://github.com/digenoma-lab/HistoMILTrainer) | 1.2 | Experimental | A library for training Multi-Instance Learning (MIL) architectures from MIL-Lab on histology datasets. HistoMILTrainer provides a unified... | Python, Slurm, PyTorch, scikit-learn, Transformer |
| [**hrr_analisis_er**](https://github.com/digenoma-lab/hrr_analisis_er) | No declared version | Documented | Description er | Not specified |
| [**HRR_histology**](https://github.com/digenoma-lab/HRR_histology) | v1.0.0 | Documented | This project contains a descriptive analysis of breast biopsy data from the Hospital Regional de Rancagua. The workflow includes data cleaning,... | R |
| [**ImputeVariants**](https://github.com/digenoma-lab/ImputeVariants) | v1.1 | Active | ImputeVariants is a comprehensive Nextflow pipeline for genotype phasing and imputation using state-of-the-art methods. The pipeline supports two... | Nextflow, Slurm, bcftools |
| [**just_align_sr**](https://github.com/digenoma-lab/just_align_sr) | 1.0 | Active | Just Align SR is a lightweight Nextflow pipeline designed for aligning short-read sequencing data (e.g., Illumina or MGI) using BWA-MEM. The... | Nextflow, Slurm, BWA, FastQC, Samtools |
| [**k-count-nf**](https://github.com/digenoma-lab/k-count-nf) | 1.0 | Active | A nextflow pipeline to count k-mers and estimate genome size from WGS data | Nextflow, STAR |
| [**liftover**](https://github.com/digenoma-lab/liftover) | v1.2 | Active | A Nextflow pipeline for lifting over genomic coordinates from one reference genome to another (e.g., hg19 to hg38 or vice versa). Supports both... | Nextflow, Slurm, Samtools, bcftools |
| [**LLM-RAG-Demo**](https://github.com/digenoma-lab/LLM-RAG-Demo) | v1.1 | Experimental | Chat system for genetic variants using RAG with Milvus Lite and DeepSeek. | Python |
| [**longcall**](https://github.com/digenoma-lab/longcall) | 0.0.1 | Active | Longcall is a Nextflow DSL2 pipeline for Oxford Nanopore (ONT) whole-genome data that | Nextflow, Slurm, minimap2, Samtools, bcftools |
| [**longcall_somatic**](https://github.com/digenoma-lab/longcall_somatic) | 0.0.1 | Active | Somatic ONT variant calling and methylation analysis for mixed tumor-only and tumor-normal cohorts. | Nextflow, Slurm, minimap2, Samtools |
| [**longreadstats**](https://github.com/digenoma-lab/longreadstats) | v1.1 | Active | digenoma-lab/longreadstats is a bioinformatics best-practice analysis pipeline for computing long-read statistics with Nanoplot. | Nextflow, Python, Slurm |
| [**LRnaseq_Rat**](https://github.com/digenoma-lab/LRnaseq_Rat) | No declared version | Documented | Repository with analysis of trascriptome data generated with Oxford Nanopore | Python, RStudio, R, Nanopore |
| [**MAG_ONT**](https://github.com/digenoma-lab/MAG_ONT) | No declared version | Documented | Chron metagenomic analysis of ONT data | Not specified |
| [**mesomic_data_note**](https://github.com/digenoma-lab/mesomic_data_note) | No declared version | Documented | Repository with code and datasets used in the mesomics data note manuscript. | Not specified |
| [**methont**](https://github.com/digenoma-lab/methont) | 0.1 | Active | The methont pipeline is designed to process long-read sequencing data for DNA methylation analysis. It includes alignment, variant calling,... | Nextflow, Slurm, minimap2, Samtools |
| [**MethylationPCA**](https://github.com/digenoma-lab/MethylationPCA) | 0.0.1 | Active | Pipeline Nextflow para preprocesar archivos BED de metilación de CpG y ejecutar un análisis de componentes principales (PCA) sobre la matriz de... | Nextflow, R, Slurm |
| [**minibusco-nf**](https://github.com/digenoma-lab/minibusco-nf) | V0.1 | Active | A simple and scalable Nextflow pipeline to compute genome or transcriptome quality metrics using minibusco. This pipeline is designed for... | Nextflow, BUSCO, Slurm |
| [**mitoH**](https://github.com/digenoma-lab/mitoH) | 7.505 | Documented | Mitocondrial genome analysis | Samtools |
| [**mocancer**](https://github.com/digenoma-lab/mocancer) | No declared version | Documented | Multi-omic analysis of cancer data | Not specified |
| [**nf-bakta**](https://github.com/digenoma-lab/nf-bakta) | v1.1 | Active | A Nextflow pipeline for the annotation of bacterial genomes or MAGs running Bakta. | Nextflow, Python, UniProt, Slurm, Bakta |
| [**nf-groot**](https://github.com/digenoma-lab/nf-groot) | No declared version | Active | A Nextflow pipeline for running Groot, which is a tool to type Antibiotic Resistance Genes (ARGs) in metagenomic samples. | Nextflow, Slurm |
| [**nf-mag-depths**](https://github.com/digenoma-lab/nf-mag-depths) | No declared version | Active | A nextflow pipeline to calculate depth of coverage from a metagenomic set of bins. | Nextflow, BWA, MetaBAT, Samtools |
| [**nf-mutect2**](https://github.com/digenoma-lab/nf-mutect2) | v1.0 | Active | Somatic SNV/indel calling with GATK Mutect2 for WGS (hg38), including optional Panel of Normals (PON), scatter/gather sharding, and filtering.... | Nextflow, Slurm, BWA, FastQC, GATK |
| [**nf-ssvsr**](https://github.com/digenoma-lab/nf-ssvsr) | v1.1 | Active | Simplified local Nextflow DSL2 workflow for | Nextflow, Python, Slurm, BWA, GATK |
| [**nf-wengan**](https://github.com/digenoma-lab/nf-wengan) | No declared version | Documented | A nexflow workflow for wengan | Wengan |
| [**oncovirus**](https://github.com/digenoma-lab/oncovirus) | No declared version | Documented | prediction of somatic virus integration from WGS using hmftools | Not specified |
| [**ontmeth-nf**](https://github.com/digenoma-lab/ontmeth-nf) | No declared version | Active | Nextflow pipeline to compute methylation from Nanopore data | Nextflow, Python, BWA, Samtools, Nanopore |
| [**ontpolish**](https://github.com/digenoma-lab/ontpolish) | No declared version | Documented | Polishing long-read assemblies | Not specified |
| [**Phasing**](https://github.com/digenoma-lab/Phasing) | 1.1 | Active | A Nextflow pipeline for phasing unphased genotype data using Beagle with reference panels from the 1000 Genomes Project. | Nextflow, Slurm, Samtools, bcftools |
| [**qualimap-nf**](https://github.com/digenoma-lab/qualimap-nf) | 1.0 | Active | The Qualimap pipeline processes sequencing data in a fast and efficient manner using Nextflow, a workflow management system. It takes aligned... | Nextflow, Python, Slurm, Samtools, Qualimap |
| [**quant_mags**](https://github.com/digenoma-lab/quant_mags) | No declared version | Active | Quantify MAGs abundance (metaG) and gene expression (metaT) | Nextflow, Python, R |
| [**quantmetaT**](https://github.com/digenoma-lab/quantmetaT) | No declared version | Active | Quantifies paired-end metatranscriptome reads using Salmon and outputs merged TPM and raw count matrices for all samples. | Nextflow, Slurm |
| [**RF-mut-tumor-only**](https://github.com/digenoma-lab/RF-mut-tumor-only) | No declared version | Documented | El llamado de variantes con muestras pareadas de tejido tumoral y normal es más confiable que el llamado de variantes con muestras de tumor... | RStudio, R, bcftools |
| [**rfhap**](https://github.com/digenoma-lab/rfhap) | V2.0 | Active | A Nextflow pipeline for long-read phasing in trio datasets, leveraging multiple k-mers and a random forest classifier. | Nextflow, Random Forest, Slurm, Hifiasm |
| [**rfhap_ms**](https://github.com/digenoma-lab/rfhap_ms) | v1.0 | Documented | Figures and analysis for RFHAP manuscript | Not specified |
| [**SMAGdb**](https://github.com/digenoma-lab/SMAGdb) | No declared version | Documented | The soid metagenome data base and analysis toolkit | Not specified |
| [**snps_mags**](https://github.com/digenoma-lab/snps_mags) | V1.0 | Active | snps_mags is a Nextflow pipeline designed for calling point mutations in Metagenome-Assembled Genomes (MAGs) using InStrain. The pipeline... | Nextflow, Slurm, BWA, FastQC, Samtools |
| [**somalier-nf**](https://github.com/digenoma-lab/somalier-nf) | v1.0 | Active | Minimal Nextflow DSL2 pipeline for somalier, the pipeline include | Nextflow, Slurm, somalier |
| [**somatic_point_mutations**](https://github.com/digenoma-lab/somatic_point_mutations) | v1.1 | Active | This repository provides a Nextflow pipeline for calling somatic point mutations from tumor/normal pairs using Whole Genome Sequencing (WGS) or... | Nextflow, Python, Slurm, Manta, bcftools |
| [**SomaticVariantCalling**](https://github.com/digenoma-lab/SomaticVariantCalling) | 0.0.1 | Active | A Nextflow (DSL 2) pipeline that takes pre‑aligned whole‑genome CRAM files and runs DeepVariant (autosomes only) followed by GLnexus cohort merging. | Nextflow, Slurm, Qualimap |
| [**spg**](https://github.com/digenoma-lab/spg) | 1.0 | Active | Simple Pan-Genome workflow for MAGs. | Nextflow, Python, Slurm, MetaBAT, Prokka |
| [**Summer_Course_ML**](https://github.com/digenoma-lab/Summer_Course_ML) | No declared version | Experimental | Material for the CMM summer course | Not specified |
| [**SV_Delly_Germline**](https://github.com/digenoma-lab/SV_Delly_Germline) | v1.0 | Active | This pipeline identifies germline structural variants (SVs) — deletions, duplications, inversions, insertions, and translocations — from... | Nextflow, Slurm, Delly, bcftools |
| [**svlr**](https://github.com/digenoma-lab/svlr) | 1.0 | Active | A nextflow Structural variant calling workflow for long-reads | Nextflow, Slurm, minimap2, Samtools |
| [**svlr_somatic**](https://github.com/digenoma-lab/svlr_somatic) | 1.0 | Active | A Nextflow pipeline for somatic structural variant (SV) calling using long-read sequencing data. | Nextflow, Slurm, minimap2, Samtools |
| [**systemix_mag_analysis**](https://github.com/digenoma-lab/systemix_mag_analysis) | No declared version | Documented | Repository holding analysis and figures to understand MAG (Metagenome-Assembled Genome) data. | Nextflow, RStudio, CheckM, Bakta, Prokka |
| [**TARA-Chile**](https://github.com/digenoma-lab/TARA-Chile) | No declared version | Documented | Genomics of TARA Ocean Chile expedition | Not specified |

> Note: this table is heuristic. Some repositories do not declare versions or toolchains explicitly, so the best possible inference is shown from the metadata available on GitHub.
