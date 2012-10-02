#!/bin/bash
cd /home/joram/code/realEstate2/
date >> log.txt
python ./scrape.py

rm /var/www/heatmap/priceData.csv
python ./updateCSV.py
