README
===========================
you can also check: https://zlab.umassmed.edu/CIpipe/ or http://www.calyx.biz/cipipe.html 

#CIpipe - CRISPR Indel pipe
###Apr22, 2016 (Nov07, 2016), Yingxiang Li

Content
------
* [Introduction](#Introduction)
* [Installation](#Installation)
* [Usage](#Usage)
* [Workflow Charts](#Workflow Charts)
* [Annotation of example.input.tab](#Annotation of example.input.tab)
* [Test Cases](#Test Cases)
* [Thanks](#Thanks)

 <a name="Introduction"/> 
Introduction
------

CRISPR-Cas9 is a powerful tool for sequence-specific genome editing. The Cas protein cuts genomic DNA at locations complementary to a single guide RNA. Insertions and deletions (indels) often result when the cuts are repaired. Currently, there is no easy-to-use computational pipeline to determine the locations, identities, and frequencies of the indels. We have developed a pipeline, named CIpipe (CRISPR Indel pipeline), to identify indels in high-throughput DNA sequencing data and provide the statistical characterization of these indels.

 <a name="Installation"/>
Installation
------

CIpipe can only run on Mac OS or Linux OS.
You need `python 2.7.10`, `R 3.2.2`, `bwa 0.7.5a`, `fastqc v0.11.2`, `samtools 1.3`, `java 1.7.0_95` first.
After installation of pip, type in your terminal:
```Bash
(sudo) pip install CIpipe (--upgrade)
```

<a name="Usage"/>
Usage 
------
###For a single sample analysis.
Synopsis
```Bash
CIpipe -R reference -D data -O output
CIpipe -R ref.fa -D data/ -O output/ -N test1
CIpipe -R ref.fa -D data/ -O output/ -N test1 -R
CIpipe -R ref.fa -D data/ -O output/ -N test1 -P 0.01 -B 15 -A 0.001
CIpipe -R ref.fa -D data/ -O output/ -N test1 -VI -VR -VS -VC
CIpipe -R ref.fa -D data/ -O output/ -N test1 -T chr1:100 -US 20 -DS 20
CIpipe -R ref.fa -D data/ -O output/ -N test1 -Q 0.1
CIpipe -R ref.fa -D data/ -O output/ -N test1 -G
```
###optional arguments:

|parameter|introduction|
|:---------- |:-----------|
|-h, --help  | show this help message and exit|
|-V, --version|show program's version number and exit|
|-R REFERENCE, --reference REFERENCE|sample reference file, fasta format. (eg: my_ref.fa)|
|-D DATA, --data DATA|sample data directory, fastq-ONLY. one file for single end, two files for paired end. (eg: my_data/)|
|-O OUTPUT, --output|OUTPUT	output directory, will be created if not exists. (eg: my_output/)|
|-F, --refresh|whether to refresh all processes. default: OFF, -RE will turn ON.|
|-N NAME, --name NAME|sample name, default is name of output directory. (eg: my_sample)|
|-RK RANK, --rank RANK|sample rank. (eg: 1)|
|-CA CUTADAPTA, --cutadapta CUTADAPTA|cut 3' adapter with cutadapt, default: none.|
|-CG CUTADAPTG, --cutadaptg CUTADAPTG|cut 5' adapter with cutadapt, default: none.|
|-S SEED, --seed SEED|the minimum seed length in BWA, default: 19.|
|-M, --markdup|whether to mark and remove duplicate by Picard. default: OFF, -M will turn ON.|
|-U, --unlimited|whether to set no read depth limit in mpileup by SAMtools. default: ON, -U will turn OFF.|
|-G, --gatk|whether to search for indel by GATK. default: OFF, -G will turn ON.|
|-P PVALUE, --pvalue|PVALUE	minimal p value, default: 0.05.|
|-B BASEQUALITY, --basequality BASEQUALITY|minimal base quality, default: 30.|
|-A VARFREQ, --varfreq VARFREQ|minimal variant frequency, default: 0.0001.|
|-VO, --vcf|whether to output VarScan in VCF format. default: OFF, -VI will turn ON.|
|-VI, --indel|whether to search for indel by VarScan. default: ON, -VI will turn OFF.|
|-VR, --readcount|whether to search for read counts by VarScan. default: ON, -VR will turn OFF.|
|-VS, --snp|whether to search for SNP by VarScan. default: OFF, -VS will turn ON.|
|-VC, --consensus|whether to search for consensus call by VarScan. default: OFF, -VC will turn ON.|
|-T TARGET, --target TARGET|CRISPR target position. indel in target range will be picked out, mutiple targets separated by ',', default: 'none'. (eg: gene1:100,gene2:200)|
|-US UPSTREAM, --upstream UPSTREAM|up stream distance from CRISPR target position, default: 20.|
|-DS DOWNSTREAM, --downstream DOWNSTREAM|down stream distance from CRISPR target position, default: 10.|
|-Q RESULTFREQ, --resultfreq RESULTFREQ|to select the results above appointed frequency, default: 0.05.|

###For multiple samples ​and advanced analysis.
Synopsis
```Bash
CIpipe -E
CIpipe -I test.input.tab
```

optional arguments:

|parameter|introduction|
|:---------|:--------|
|-E, --example|whether to create example input data. modify the example.input.tab to fit your data. default: OFF, -E will turn ON.|
|-I INPUT, --input INPUT|information table of all input data. all settings should be in it. (eg. example.input.tab)|

<a name="Workflow Charts"/>
Workflow Charts
------

###For a single samples analysis (basic).
![](http://www.calyx.biz/uploads/2/1/9/2/21925892/2706147_orig.png "")
***
###For a single samples analysis (complete).
![](http://www.calyx.biz/uploads/2/1/9/2/21925892/4017768_orig.png "")
***
###For multiple samples and advanced analysis. (basic).
![](http://www.calyx.biz/uploads/2/1/9/2/21925892/2706147_orig.png "")
***
###For multiple samples and advanced analysis. (complete).
![](http://www.calyx.biz/uploads/2/1/9/2/21925892/2706147_orig.png "")
***
***

##Annotation of example.input.tab
Type: ```Bash CIpipe -E``` to create an `example.input.tab​`.
Then modify it to fit your real data.

![](http://www.calyx.biz/uploads/2/1/9/2/21925892/4173713_orig.png "")

<a name="Test Cases"/>
Test Cases
------
Test data is a part from 
>**Li,Y. et al. (2015) A versatile reporter system for CRISPR-mediated chromosomal rearrangements. Genome Biol., 16, 111.**

The full data is: [PRJNA283020](https://www.ncbi.nlm.nih.gov/sra?linkname=bioproject_sra_all&from_uid=283020). Here I only get the top 20,000 lines of each fastq file.

1. Download the data: `SRR2007490`, `SRR2007491`, `SRR207493`. (12.5MB, 12.4MB, 11.8MB)
2. Download the reference:  `refer.zip` (LSL_1008bp.fa, iGFP_448bp.fa). (2KB)
3. For a single sample analysis (name: test1):
	1. Extract `refer.zip` to `refer/`.
	2. Extract `SRR2007490` to `data/SRR2007490/`.
	3. After the installation of CIpipe, in the terminal, type: ```Bash CIpipe -R refer/LSL_1008bp.fa -D data/SRR2007490/ -O output/ -N test1 ```
	4. CIpipe will show the progress on your terminal screen like this:
	![](https://zlab.umassmed.edu/CIpipe/files/322149.png "")
	5. The files in output/test1/result folder include:
		* `test1.data.infor.txt`  (the map and data information)
		* ​`test1.indel.brief.tab`  (the brief indel result from `VarScan/test1.indel.tab`)
		* `test1.indel.potential.LSL_1008bp:88.tab` (the indel target position range result. if user didn't point out the cut position, CIpipe will assume that the position with the max varfreq was the cut position and add a 'potential' in the file name.)
		* `test1.indel.potential.LSL_1008bp:88.pdf` (the indel target position region detail plot. it's ordered by positions and from small to large and indel types from deletion to insertion)
		* `test1.indel.potential.LSL_1008bp:88.sort.pdf` (the indel target position detail plot. it's ordered by variant frequency from high to low.)

4. For multiple samples and advanced analysis:
	1. Extract `refer.zip` to `refer/`.
	2. Extract `SRR2007490`, `SRR2007491`, `SRR207493` to `data/SRR2007490/`, `data/SRR2007491/`, `data/SRR2007493/`.
	3. In the terminal, type: ```Bash CIpipe more -E ``` `exmaple.input.tab` will be generated in the current working directory like this:

	4. Open `example.input.tab` and modify it to `test2.input.tab` as follows:

	5. In the terminal, type: ```Bash CIpipe -I input/test2.input.tab```

	6. CIpipe will show the progress on your terminal screen like this:

	7. In result folder of each sample, there are such files (example: `LSL2`):
		* `LSL2.data.infor.txt` (the map and data information)
		* `LSL2.indel.brief.tab` (the brief indel result)
		* `LSL2.indel.LSL_1008bp:88.tab` (the indels only in target region, if user pointed out the cut position, there will be no 'potential' in the file name.)
		* `LSL2.indel.LSL_1008bp:88.pdf` (the indel target position region detail plot)
		* `LSL2.indel.LSL_1008bp:88.sort.pdf` (the indel target position region detail plot)

	8. In the result folder of batch (test2.result/), there are such files:
		* `test2.indel.iGFP_448bp.mat` (indels across all iGFP samples)
		* `test2.indel.LSL_1008bp.mat` (indels across all LSL samples)

5. You can change all kinds of parameters to filter the results. For example, you can change the p value to 0.01 to get a stricter indels result table; change base quality to 15 to get more potential indels.	
<a name="Thanks"/>
Thanks
------
We thank the members of the `Weng` and `Xue` laboratories for helpful discussions, in particular `Chunqing Song, Pengpeng Liu, Yu Fu, Tyler Borrman, Michael Purcaro, Arjan van der Velde` for their insightful suggestions. 