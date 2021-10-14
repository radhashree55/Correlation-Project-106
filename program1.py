import plotly.express as px
import csv
import numpy as np


def plotFigure(dataPath):
    with open(dataPath) as csvFile:
        df = csv.DictReader(csvFile)
        fig = px.scatter(df, x="Days Present", y="Marks In Percentage")
        fig.show()


def getDataSource(dataPath):
    marksInPercentage = []
    daysPresent = []
    with open(dataPath) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            marksInPercentage.append(float(row["Marks In Percentage"]))
            daysPresent.append(float(row["Days Present"]))

    return {"x": marksInPercentage, "y": daysPresent}


def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print(
        "Correlation between Marks in percentage and Days present:",
        correlation[0, 1],
    )


def setup():
    dataPath = "./data1.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)
    plotFigure(dataPath)


setup()
