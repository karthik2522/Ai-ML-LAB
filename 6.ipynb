{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "6.ipynb",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RprBLnOGhpqS",
        "outputId": "8a253f45-8fcc-4512-e01c-91472320b2a4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Split 768 rows into train=514 and test=254 rows\n",
            "Accuracy: 0.39370078740157477%\n"
          ]
        }
      ],
      "source": [
        "import csv\n",
        "import random\n",
        "import math\n",
        "def safe_div(x,y):\n",
        "    if y == 0:\n",
        "        return 0\n",
        "    return x / y\n",
        "def loadCsv(filename):\n",
        "\tlines = csv.reader(open(filename, \"r\"))\n",
        "\tdataset = list(lines)\n",
        "\tfor i in range(len(dataset)):\n",
        "\t\tdataset[i] = [float(x) for x in dataset[i]]\n",
        "\treturn dataset\n",
        "def splitDataset(dataset, splitRatio):\n",
        "\ttrainSize = int(len(dataset) * splitRatio)\n",
        "\ttrainSet = []\n",
        "\tcopy = list(dataset)\n",
        "\twhile len(trainSet) < trainSize:\n",
        "\t\tindex = random.randrange(len(copy))\n",
        "\t\ttrainSet.append(copy.pop(index))\n",
        "\treturn [trainSet, copy]\n",
        "def separateByClass(dataset):\n",
        "\tseparated = {}\n",
        "\tfor i in range(len(dataset)):\n",
        "\t\tvector = dataset[i]\n",
        "\t\tif (vector[-1] not in separated):\n",
        "\t\t\tseparated[vector[-1]] = []\n",
        "\t\tseparated[vector[-1]].append(vector)\n",
        "\treturn separated\n",
        "def mean(numbers):\n",
        "\treturn sum(numbers)/float(len(numbers))\n",
        "def stdev(numbers):\n",
        "\tavg = mean(numbers)\n",
        "\tvariance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)\n",
        "\treturn math.sqrt(variance)\n",
        "def summarize(dataset):\n",
        "\tsummaries = [(mean(attribute), stdev(attribute))\n",
        "                   for attribute in zip(*dataset)]\n",
        "\tdel summaries[-1]\n",
        "\treturn summaries\n",
        "def summarizeByClass(dataset):\n",
        "\tseparated = separateByClass(dataset)\n",
        "\tsummaries = {}\n",
        "\tfor classValue, instances in separated.items():\n",
        "\t\tsummaries[classValue] = summarize(instances)\n",
        "\treturn summaries\n",
        "def calculateProbability(x, mean, stdev):\n",
        "\texponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))\n",
        "\treturn (1 / (math.sqrt(2*math.pi) * stdev)) * exponent\n",
        "def calculateClassProbabilities(summaries, inputVector):\n",
        "\tprobabilities = {}\n",
        "\tfor classValue, classSummaries in summaries.items():\n",
        "\t\tprobabilities[classValue] = 1\n",
        "\t\tfor i in range(len(classSummaries)):\n",
        "\t\t\tmean, stdev = classSummaries[i]\n",
        "\t\t\tx = inputVector[i]\n",
        "\t\t\tprobabilities[classValue] *= calculateProbability(x, mean, stdev)\n",
        "\treturn probabilities\n",
        "def predict(summaries, inputVector):\n",
        "\tprobabilities = calculateClassProbabilities(summaries, inputVector)\n",
        "\tbestLabel, bestProb = None, -1\n",
        "\tfor classValue, probability in probabilities.items():\n",
        "\t\tif bestLabel is None or probability > bestProb:\n",
        "\t\t\tbestProb = probability\n",
        "\t\t\tbestLabel = classValue\n",
        "\treturn bestLabel\n",
        "def getPredictions(summaries, testSet):\n",
        "\tpredictions = []\n",
        "\tfor i in range(len(testSet)):\n",
        "\t\tresult = predict(summaries, testSet[i])\n",
        "\t\tpredictions.append(result)\n",
        "\treturn predictions\n",
        "def getAccuracy(testSet, predictions):\n",
        "    correct = 0\n",
        "    for i in range(len(testSet)):\n",
        "        if testSet[i][-1] == predictions[i]:\n",
        "            correct += 1\n",
        "        return (correct/float(len(testSet))) * 100.0\n",
        "def main():\n",
        "\tfilename = 'pima-indians-diabetes.csv'\n",
        "\tsplitRatio = 0.67\n",
        "\tdataset = loadCsv(filename)\n",
        "\ttrainingSet,testSet=splitDataset(dataset, splitRatio) \n",
        "\tprint('Split {0} rows into train={1} and test={2} rows'\n",
        "  .format(len(dataset), len(trainingSet), len(testSet)))\n",
        "\tsummaries = summarizeByClass(trainingSet)\n",
        "\tpredictions = getPredictions(summaries, testSet)\n",
        "\taccuracy = getAccuracy(testSet, predictions)\n",
        "\tprint('Accuracy: {0}%'.format(accuracy))\n",
        "\n",
        "main()\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "f6lHwBWvi8TI"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}