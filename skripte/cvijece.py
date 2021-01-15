import csv

f = open("iris.data", "r")

reader = csv.reader(f, delimiter = ",")

cvijece =[]

for e in reader:
    e = str(e)
    e = e.strip()
    if len(e) == 0:
        continue
    parts = e.split(",")
    cvijece.append(
                               (
                            float(parts[0]) ,
                            float(parts[1]) ,
                            float(parts[2]) ,
                            float(parts[3]) ,
                            parts[4]
                            )
                        )
    
    
f.close()

print(cvijece)
print(cvijece[12])

print(cvijece[12][1])

