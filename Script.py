# Dependencies:
# biopython & bedtools

# RUN THE COMMAND BELOW IN THE TERMINAL FROM THE LOCATION OF THE PYTHON SCRIPT
# IN ORDER TO HAVE THE CE11.FA GENOME FILE ACCESSIBLE
# wget -c http://hgdownload.cse.ucsc.edu/goldenPath/ce11/bigZips/chromFa.tar.gz -O - | gzip -dc | tar -xO > ce11.fa

coordinates=[]
coordinates.append(input("Chromosome of gene (typed like this -> 'chrIII'):"))
coordinates.append(input("Gene strand (+ or -):"))
coordinates.append(int(input("Intron 1 start coordinate:")))
coordinates.append(int(input("Intron 1 end coordinate:")))
coordinates.append(int(input("Intron 2 start coordinate:")))
coordinates.append(int(input("Intron 2 end coordinate:")))


#coordinates=["chrIII","+",11688327,11689777,11685351,11688107]


# This creates temporary BED files from said intron coordinates

left = open("left.bed", "w")
left.write(coordinates[0]+"\t"+str(coordinates[2])+"\t"+str(coordinates[3])+"\tName\t0\t"+coordinates[1])
left.close()
right = open("right.bed", "w")
right.write(coordinates[0]+"\t"+str(coordinates[4])+"\t"+str(coordinates[5])+"\tName\t0\t"+coordinates[1])
right.close()

# This extracts the FASTA sequence from the BED files
import os
os.system('bedtools getfasta -fi ce11.fa -bed left.bed -s -name > left_intron.fa')
os.system('bedtools getfasta -fi ce11.fa -bed right.bed -s -name > right_intron.fa')

# This BLASTs the introns against eachother
exec(open('blast_function.py').read())

# This retrieves all the RCM sequences
os.system('cat results_RCM.txt | grep query | tr -d "-" | tr " " "\n" | grep -ve query | grep -ve blast | grep . > leftRCMs.txt')
os.system('cat results_RCM.txt | grep reverse | tr " " "\n" | grep -ve Subject | grep -ve reverse | grep . > rightRCMs.txt')
lines_left = [line.rstrip('\n') for line in open('leftRCMs.txt')]
lines_right = [line.rstrip('\n') for line in open('rightRCMs.txt')]
left_seq = [line.rstrip('\n') for line in open('left_intron.fa')]
right_seq = [line.rstrip('\n') for line in open('right_intron.fa')]
left_seq=left_seq[1].upper()
right_seq=right_seq[1].upper()

# This finds WHERE the RCMs are in the introns (coordinates)
BEDs_left = [[left_seq.find(line)+coordinates[2], left_seq.find(line)+coordinates[2]+len(line)] for line in lines_left]
BEDs_right = [[right_seq.find(line)+coordinates[4], right_seq.find(line)+coordinates[4]+len(line)] for line in lines_right]

final = open("output.bed", "w")
for line in BEDs_left:
    final.write(coordinates[0]+"\t"+str(line[0])+"\t"+str(line[1])+"\tRCM\t0\t"+coordinates[1]+"\n")
for line in BEDs_right:
    final.write(coordinates[0]+"\t"+str(line[0])+"\t"+str(line[1])+"\tRCM\t0\t"+coordinates[1]+"\n")
final.close()

for i in range(5):
    print("")

print("All the RCMs are shown in the OUTPUT.BED file.")
os.system('')
os.system('rm left.bed right.bed left_intron.fa right_intron.fa seq1.fasta seq2.fasta stats_RCM.csv results_RCM.txt leftRCMs.txt rightRCMs.txt')
