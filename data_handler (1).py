## data_dict={
## "enst100110" : {"gene_strand":"+",
##                 "region":"exon",
##                 "length":"87",
##                 "repair_raw":"89",
##                 "repair_rpkm":"2.42",
##                 "strain":"wT",
##                 "replicate":"A",
##                 "damage":"CPD",
##                 "repair_strand":"" }
##........
##          }

data_name = input("Please enter the sample name: ")
out_name = input("Please enter the output file name: ")
total_read = float(input("Please enter the total line: "))

data = open(data_name, "r")

data_dict={ }
data_line = data.readlines()

data_name_2 = data_name.split("_")

strain = data_name_2[0]


damage = data_name_2[1]
if damage == "64":
    damage ="64PP"
replicate = data_name_2[2]

repair_strand = data_name_2[5]
if repair_strand == "minus":
    repair_strand = "-"
elif repair_strand == "plus":
    repair_strand="+"

for x in data_line:
    x = x.split()
    data_list=[]
    for i in x:
        data_list.append(i)
        
    chro = data_list[0]
    spoint =float(data_list[1])
    epoint = float(data_list[2])
    length = float(epoint-spoint)
    gene_name = data_list[3][:15]
    gene_long = data_list[3].split("_")
    intron_exon = gene_long[1]
    zero = data_list[4]
    pm = data_list[5]
    rep_value = float(data_list[6])
    rep_rpkm = 0
    
    if gene_name in data_dict:
        data_dict[gene_name]["repair_raw"] += rep_value
        data_dict[gene_name]["length"] += length
    else:
        dict_in={"gene_strand":pm,"region":intron_exon,"length":length,"repair_raw":rep_value,"repair_rpkm":rep_rpkm,"strain":strain,"replicate":replicate,"damage":damage,"repair_strand":repair_strand}
        data_dict[gene_name] = dict_in
        

for gname, namelist in data_dict.items():
    namelist["repair_rpkm"] = ((((namelist["repair_raw"])/total_read)*1000000)/namelist["length"])*1000




f = open(out_name, 'a')

for dict_gene, dict_gene_list in data_dict.items():
    a = []
    a.append(dict_gene)
    for key in dict_gene_list:
        a.append(dict_gene_list[key])
    for item in a:
       f.write(("%s" % item)+" ")
    f.write("\n")
    
f.close()
