import plotly.express as px
import csv
import numpy as np


def plotFigure(dataPath):
    with open(dataPath) as csvFile:
        df = csv.DictReader(csvFile)
        fig = px.scatter(df, x="Coffee in ml", y="Sleep in hours")
        fig.show()


def getDataSource(dataPath):
    cofeeInMl = []
    sleepInHours = []
    with open(dataPath) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            cofeeInMl.append(float(row["Coffee in ml"]))
            sleepInHours.append(float(row["Sleep in hours"]))

    return {"x": cofeeInMl, "y": sleepInHours}


def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print(
        "Correlation between Coffee in ml and Sleep in Hours:",
        correlation[0, 1],
    )


def setup():
    dataPath = "./data2.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)
    plotFigure(dataPath)


setup()
