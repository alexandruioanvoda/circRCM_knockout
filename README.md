# circRCM_knockout
Script that produces BED files of RCMs

## Installation
To install run this in the terminal:
```
git clone https://github.com/alexandruioanvoda/circRCM_knockout
cd ./circRCM_knockout
chmod +x ./*
```
The installation and runs were tested on Ubuntu 18

The following dependencies need to be installed: `Python 3, biopython, bedtools`

For any issues running scripts in this repository, please email at `avoda@nevada.unr.edu`


## Run

Navigate with the terminal to the circRCM_knockout folder and run:

`python Script.py`


## Input

Just insert the coordinates of the introns flanking the circRNA.
Example: for Circ_0000333, `chrIII, +, 1927947, 1929102, 1918723, 1927649`
(chromosome in ce11 genome, strand, intron 1 start, intron 1 end, intron 2 start, intron 2 end)
