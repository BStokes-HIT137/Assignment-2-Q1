#call up csv library
import csv
#Use in built python python library to count word occurrences and most_common() for top 30
from collections import Counter

#set directory of .txt file aquired in Q1_Task1
output_txt ="E:/chuditchwerkroom/2024_Werkroom/0000_CDU/2024_CDU/2024 SEM 2/HIT137/Working_Python Files/Assignment 2_HIT137_CAS_080/Q1_file_output/HIT137_A2_Q1.1.txt"

#Count word occurances split lines into word blocks
word_total_count = Counter()
with open(output_txt) as file:
    for line in file:
        word_total_count.update(line.split())

#Find the most common words 30 words from word_count_total
top30 = word_total_count.most_common(30)

#save to a new csv document
output_top30_csv ="E:/chuditchwerkroom/2024_Werkroom/0000_CDU/2024_CDU/2024 SEM 2/HIT137/Working_Python Files/Assignment 2_HIT137_CAS_080/Q1_file_output/HIT137_A2_Q3.1.csv"

with open(output_top30_csv, 'w', newline ='') as csv_file:
    writer = csv.writer(csv_file)
    #add in a header to the csv file for the columns and to compare later
    writer.writerow (['First Python In Built Library Pass of TOP30'])
    writer.writerow(['Word','Frequency'])
    #Write the counts to the file
    for word, count in top30:
        writer.writerow ([word,count])

#print the resulting dictionary
print('Here is a quick look at the list.')
for word, count in top30:
    print(f'{word}: {count}')
#show task is complete and location    
print(f'Your top 30 occurrences have been saved to {output_top30_csv}')

#Just need to address file handling