import ast
from distutils.core import setup
from setuptools import setup, find_packages

def get_version(fname):
    with open(fname) as f:
        source = f.read()
    module = ast.parse(source)
    for e in module.body:
        if isinstance(e, ast.Assign) and \
                len(e.targets) == 1 and \
                e.targets[0].id == '__version__' and \
                isinstance(e.value, ast.Str):
            return e.value.s
    raise RuntimeError('__version__ not found')

setup(name = 'CIpipe',  
      version = get_version('CIpipe/CIpipe'),
      keywords = 'CRISPR Indel pipe',
      description = 'CRISPR Indel pipe', 
      long_description = 'CRISPR has been a prevalent and powerful tool for gene editing in recent years. With the appliance of CRISPR, researchers could change DNA structures by inducing indel (insertion/deletion) at specific locus conveniently. In order to examine the efficiency of CRISPR experiment, high-through sequencing on target region will be performed, which brings the computational question. To address this issue, we developed a pipeline, \'CIpipe (CRISPR Indel pipe)\', to analyze the target sequencing data for indel after CRISPR experiment. CIpipe is easy to use and can produce understandable results for paper writing quickly.',
      license = 'GPLv3',
      classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Build Tools',
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      'Programming Language :: Python :: 2.7',
      ],
      author = 'Yingxiang Li',  
      author_email = 'xlccalyx@gmail.com', 
      maintainer = 'Yingxiang Li',
      url = 'https://zlab.umassmed.edu/CIpipe/',
      download_url = 'https://pypi.python.org/pypi/CIpipe',
      install_requires = ['numpy>=1.11.0'],
      packages = ['CIpipe'],
      package_dir = {'CIpipe': 'CIpipe'},
      scripts = ['CIpipe/CIpipe'],
      package_data = {'CIpipe': ['VarScan.v2.3.9.jar', 'CreateSequenceDictionary.jar', 'example.input.tab', 'GenomeAnalysisTK.jar', 'picard.jar']}
) 

