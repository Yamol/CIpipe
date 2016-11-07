web version is in: https://zlab.umassmed.edu/CIpipe/ or http://www.calyx.biz/cipipe.html 

CIpipe- CRISPR indel pipe
Apr22, 2016
Yingxiang Li

Content:
	Introduction
	Installation
	Synopsis
	Commands and Options
	Workflow Charts
	Annotation of example.input.tab
	Test Cases
	Thanks

Introduction:
CRISPR-Cas9 is a powerful tool for sequence-specific genome editing. The Cas protein cuts genomic DNA at locations complementary to a single guide RNA. Insertions and deletions (indels) often result when the cuts are repaired. Currently, there is no easy-to-use computational pipeline to determine the locations, identities, and frequencies of the indels. We have developed a pipeline, named CIpipe (CRISPR Indel pipeline), to identify indels in high-throughput DNA sequencing data and provide the statistical characterization of these indels.

Installation:
CIpipe can only run on Mac OS or Linux OS.
You need python 2.7.10, R 3.2.2, bwa 0.7.5a; fastqc v0.11.2; samtools 1.3; java 1.7.0_95 first.
After installation of pip, type in your terminal:
(sudo) pip install CIpipe (--upgrade)

Commands and Options:

For a single sample analysis.
​
Synopsis
CIpipe -R reference -D data -O output
CIpipe -R ref.fa -D data/ -O output/ -N test1
CIpipe -R ref.fa -D data/ -O output/ -N test1 -R
CIpipe -R ref.fa -D data/ -O output/ -N test1 -P 0.01 -B 15 -A 0.001
CIpipe -R ref.fa -D data/ -O output/ -N test1 -VI -VR -VS -VC
CIpipe -R ref.fa -D data/ -O output/ -N test1 -T chr1:100 -US 20 -DS 20
CIpipe -R ref.fa -D data/ -O output/ -N test1 -Q 0.1
CIpipe -R ref.fa -D data/ -O output/ -N test1 -G

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit
  -R REFERENCE, --reference REFERENCE	sample reference file, fasta format. (eg: my_ref.fa)
  -D DATA, --data DATA	sample data directory, fastq-ONLY. one file for single end, two files for paired end. (eg: my_data/)
  -O OUTPUT, --output OUTPUT	output directory, will be created if not exists. (eg: my_output/)
  -F, --refresh         whether to refresh all processes. default: OFF, -RE will turn ON.
  -N NAME, --name NAME  sample name, default is name of output directory. (eg: my_sample)
  -RK RANK, --rank RANK	sample rank. (eg: 1)
  -CA CUTADAPTA, --cutadapta CUTADAPTA	cut 3' adapter with cutadapt, default: none.
  -CG CUTADAPTG, --cutadaptg CUTADAPTG	cut 5' adapter with cutadapt, default: none.
  -S SEED, --seed SEED	the minimum seed length in BWA, default: 19.
  -M, --markdup         whether to mark and remove duplicate by Picard. default: OFF, -M will turn ON.
  -U, --unlimited       whether to set no read depth limit in mpileup by SAMtools. default: ON, -U will turn OFF.
  -G, --gatk            whether to search for indel by GATK. default: OFF, -G will turn ON.
  -P PVALUE, --pvalue PVALUE	minimal p value, default: 0.05.
  -B BASEQUALITY, --basequality BASEQUALITY	minimal base quality, default: 30.
  -A VARFREQ, --varfreq VARFREQ	minimal variant frequency, default: 0.0001.
  -VO, --vcf            whether to output VarScan in VCF format. default: OFF, -VI will turn ON.
  -VI, --indel          whether to search for indel by VarScan. default: ON, -VI will turn OFF.
  -VR, --readcount      whether to search for read counts by VarScan. default: ON, -VR will turn OFF.
  -VS, --snp            whether to search for SNP by VarScan. default: OFF, -VS will turn ON.
  -VC, --consensus      whether to search for consensus call by VarScan. default: OFF, -VC will turn ON.
  -T TARGET, --target TARGET	CRISPR target position. indel in target range will be picked out, mutiple targets separated by ',', default: 'none'. (eg: gene1:100,gene2:200)
  -US UPSTREAM, --upstream UPSTREAM	up stream distance from CRISPR target position, default: 20.
  -DS DOWNSTREAM, --downstream DOWNSTREAM	down stream distance from CRISPR target position, default: 10.
  -Q RESULTFREQ, --resultfreq RESULTFREQ	to select the results above appointed frequency, default: 0.05.

For multiple samples ​and advanced analysis.

Synopsis
CIpipe -E
CIpipe -I test.input.tab

optional arguments:
​
  -E, --example         whether to create example input data. modify the example.input.tab to fit your data. default: OFF, -E will turn ON.
  -I INPUT, --input INPUT	information table of all input data. all settings should be in it. (eg. example.input.tab)


