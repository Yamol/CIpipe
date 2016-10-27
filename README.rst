more details are in: http://www.calyx.biz/cipipe.html 

	|~~~~~~~~~~~~~www.calyx.biz~~~~~~~~~~~~|
	|                 __.                  |
	|  ___.  ____.   |  |  __. __.__.   __.|
	|_/ ___\ \__  \  |  | <   y  |\  \ /  /|
	|\  c___  /  a \_|  l__\___  | >  x  < |
	| \_____>(______/|____//_____|/__/ \__\|
	|~~~~~~~~~~~~~www.calyx.biz~~~~~~~~~~~~|


CIpipe: CRISPR indel pipe
Apr22, 2016
Yingxiang Li

Introduction
CRISPR has been a prevalent and powerful tool for gene editing in recent years. With the appliance of CRISPR, researchers could change DNA structures by inducing indel (insertion/deletion) at specific locus conveniently. In order to examine the efficiency of CRISPR experiment, high-through sequencing on target region will be performed, which brings the computational question. To address this issue, we developed a pipeline, ‘CIpipe (CRISPR Indel pipe)’, to analyze the target sequencing data for indel after CRISPR experiment. CIpipe is easy to use and can produce understandable results for paper writing quickly.

Installation
CIpipe can only run on Mac OS or Linux OS.
You need python 2.7, bwa: 0.7.5a; fastqc: v0.11.2; samtools: 1.3; java: 1.7.0_95 first.
After installation of 'pip', type in your terminal:
pip install CIpipe

Synopsis
CIpipe one -R ref.fa -D data/ -O output/
CIpipe one -R ref.fa -D data/ -O output/ -N test -P 0.01 -B 15 -A 0.001
CIpipe one -R ref.fa -D data/ -O output/ -N test -F -X -VI
CIpipe one -R ref.fa -D data/ -O output/ -N test -VS -VC -VR
CIpipe one -R ref.fa -D data/ -O output/ -N test -T 100 -US 20 -DS 20

CIpipe more -E
CIpipe more -I test.input.tab

Commands and Options
one	CIpipe one -R reference -D data -O output 
	#mode one, for one sample analysis.

	optional arguments:
	-h, --help		show this help message and exit

	-R, --reference		sample reference file, fasta format. (eg: my_ref.fa)

	-D, --data		sample data directory, fastq-ONLY. one file for single end, two files for paired end. (eg: my_data/)
	 
	​-O, --output		output directory, will be created if not exists. (eg: my_output/)  

	​-N, --name		sample name, default is name of output directory. (eg: my_sample)

	-RK, --rank		sample rank. (eg: 1)

	-P, --pvalue		minimal p value, default: 0.05.

	-B, --basequality		minimal base quality, default: 30.

	-A, --varfreq		minimal variant frequency, default: 0.0001.

	-T, --target		CRISPR target position. indel in target range will be picked out, mutiple targets separated by ';', default: NoTarget. (eg: gene1:100;gene2:200)

	​-US, --upstream		up stream distance from CRISPR target position, default: 20.

	-DS, --downstream		down stream distance from CRISPR target position, default: 10.

	-F, --fastqc		fastq quality control by FastQC, default: ON. -F will turn OFF.   

	-X, --index		build reference index by BWA, default: ON. -X will turn OFF.

	-U, --unlimited		no read depth limit in mpileup by SAMtools, default: OFF.

	-VI, --Indel		search for indel by VarScan, default: ON. -I will turn OFF.

	-VS, --snp		search for SNP by VarScan, default: OFF.

	-VC, --consensus		search for consensus call by VarScan, default: OFF.

	-VR, --readcount		search for read counts by VarScan, default: OFF.


more	CIpipe more [-E | -I input] 
		#mode more, for mutiple samples and advanced analysis.

	optional arguments:
	-h, --help		show this help message and exit

​	-E, --example		create example input data. modify the example.input.tab to fit your data.

​	-I, --input		information table of all input data. all settings should be in it. (eg. example.input.tab)​

 


​

​