import csv

#Isolate Liberia and Nigeria first
csvfile_read = open("ebola_2014_2016_clean.csv",mode='r',newline='') # make the file object to be read by csvreader. isolate Liberia and Nigeria
csvfile_write_Liberia = open("Liberia_2014_2016.csv","w")
csvfile_write_Nigeria = open("Nigeria_2014_2016.csv","w")

csvreader = csv.reader(csvfile_read,delimiter=',')
next(csvreader,None) # skip through heading

csvwriter_Liberia = csv.writer(csvfile_write_Liberia,delimiter=',')
csvwriter_Nigeria = csv.writer(csvfile_write_Nigeria,delimiter=',')

csvwriter_Liberia.writerow(["Country","Date","Cumulative no. of confirmed, probable and suspected cases","Cumulative no. of confirmed, probable and suspected deaths"])
csvwriter_Nigeria.writerow(["Country","Date","Cumulative no. of confirmed, probable and suspected cases","Cumulative no. of confirmed, probable and suspected deaths"])

for row in csvreader:
    if row[0] == "Nigeria":
        csvwriter_Nigeria.writerow(row)
    elif row[0] == "Liberia":
        csvwriter_Liberia.writerow(row)


csvfile_read.close()
csvfile_write_Liberia.close()
csvfile_write_Nigeria.close()
    


