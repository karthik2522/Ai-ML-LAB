{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "3.ipynb",
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
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RprBLnOGhpqS",
        "outputId": "b649fd73-6f8a-4af4-a864-5639a7762577"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Final S:\n",
            "['Sunny' 'Warm' '?' 'Strong' '?' '?']\n",
            "Final G:\n",
            "[['Sunny', '?', '?', '?', '?', '?'], ['?', 'Warm', '?', '?', '?', '?']]\n"
          ]
        }
      ],
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "data = pd.DataFrame(data=pd.read_csv('1finds.csv'))\n",
        "concepts = np.array(data.iloc[:,0:-1])\n",
        "target = np.array(data.iloc[:,-1])\n",
        "def learn(concepts, target):\n",
        "    specific_h = concepts[0].copy()\n",
        "    general_h = [[\"?\" for i in range(len(specific_h))] for i in range(len(specific_h))]\n",
        "    for i, h in enumerate(concepts):\n",
        "        if target[i] == \"Yes\":\n",
        "            for x in range(len(specific_h)):\n",
        "                if h[x] != specific_h[x]:\n",
        "                    specific_h[x] = '?'\n",
        "                    general_h[x][x] = '?'\n",
        "        if target[i] == \"No\":\n",
        "            for x in range(len(specific_h)):\n",
        "                if h[x] != specific_h[x]:\n",
        "                    general_h[x][x] = specific_h[x]\n",
        "                else:\n",
        "                    general_h[x][x] = '?'\n",
        "    indices = [i for i,val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]\n",
        "    for i in indices:\n",
        "        general_h.remove(['?', '?', '?', '?', '?', '?'])\n",
        "    return specific_h, general_h\n",
        "s_final, g_final = learn(concepts, target)\n",
        "print(\"Final S:\", s_final, sep=\"\\n\")\n",
        "print(\"Final G:\", g_final, sep=\"\\n\")\n"
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