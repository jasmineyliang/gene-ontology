from Bio.UniProt.GOA import gafbyproteiniterator
path = "G:\My Drive\pythonProject\COMS570HW5\goa_worm.gaf"
Evidence = ['EXP', 'IDA', 'IPI', 'IMP', 'IGI', 'IEP'
  #  , 'HTP', 'HDA', 'HMP', 'HGI', 'HEP'   ## uncomment for high throughout
            ]
total_proteins = 0
exp = 0
with open(path, 'r') as handle:
    for line in gafbyproteiniterator(handle):
        total_proteins = total_proteins+1
        print ("total", total_proteins)
        res = [sub['Evidence'] for sub in line]
        for key in Evidence:
            if key in res:
                print(str(res))
                exp = exp + 1
                print("EXP", exp)
                break
    NoExp = total_proteins - exp
    Normalized = exp/total_proteins

    print("not by exp", NoExp)
    print("Normalized by no", Normalized)