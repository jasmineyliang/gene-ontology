# gene-ontology
proteins annotated
Go to http://www.ebi.ac.uk/GOA/downloads
Download the uniprot-goa  files goa_<species>_gaf.gz for
Human
Mouse
Rat
S. cerevisiae (Yeast)
C. elegans (Worm)

File format guide is available in the README, and in the file header (the lines starting with a “!”). These are tab-delimited files. A field with a null value is an empty string.
Use your favorite scripting language to answer the following questions. If using Python, I recommend installing biopython and availing yourself of the Bio.Uniprot module, or using PANDAS
For each species:

How many proteins are experimentally annotated (including high throughput evidence codes)?
How many proteins are not experimentally annotated?
Which species “leads” in being experimentally annotated? That is, has the most proteins that are experimentally annotated? Answer in absolute numbers and normalized by the number of annotated proteins size
Answer the previous three question twice. Once including high throughput evidence codes and "regular" experimental evidence codes, and once excluding high throughput evidence codes. 


Experimental evidence codes are: EXP, IDA, IPI, IMP, IGI, IEP
High throughput experimental evidence codes are: HTP, HDA, HMP, HGI, HEP
See: http://geneontology.org/page/guide-go-evidence-codes  
for details

1. Results as tables, with a brief explanation.

2. A conclusions from this data  

3. The code 
