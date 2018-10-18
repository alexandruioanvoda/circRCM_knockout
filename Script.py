


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
