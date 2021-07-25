import numpy as np,csv,math

def getDataSource(data_path):
    Days_Present = []
    Marks_in_percentage = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Marks_in_percentage.append(float(row["Marks In Percentage"]))
            Days_Present.append(float(row["Days Present"]))
    return {"x" : Days_Present, "y": Marks_in_percentage}
def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Marks Scored by each student according to there roll no are :- \n--->",correlation[0,1])
def setup():
    data_path  = "Marks.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
setup()

math = math.sqrt(11)
print (math)