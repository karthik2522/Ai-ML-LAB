{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "1.ipynb",
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
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RprBLnOGhpqS",
        "outputId": "4228278d-0d47-47ce-f7a1-a9a2d4642cd5"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Path found: ['A', 'F', 'G', 'I', 'J']\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['A', 'F', 'G', 'I', 'J']"
            ]
          },
          "metadata": {},
          "execution_count": 2
        }
      ],
      "source": [
        "def aStarAlgo(start_node, stop_node):\n",
        "         \n",
        "        open_set = set(start_node) \n",
        "        closed_set = set()\n",
        "        g = {} \n",
        "        parents = {}\n",
        "        g[start_node] = 0\n",
        "        parents[start_node] = start_node\n",
        "        while len(open_set) > 0:\n",
        "            n = None\n",
        "            for v in open_set:\n",
        "                if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):\n",
        "                    n = v \n",
        "            if n == stop_node or Graph_nodes[n] == None:\n",
        "                pass\n",
        "            else:\n",
        "                for (m, weight) in get_neighbors(n):\n",
        "                    if m not in open_set and m not in closed_set:\n",
        "                        open_set.add(m)\n",
        "                        parents[m] = n\n",
        "                        g[m] = g[n] + weight\n",
        "                    else:\n",
        "                        if g[m] > g[n] + weight:\n",
        "                            g[m] = g[n] + weight\n",
        "                            parents[m] = n\n",
        "                            if m in closed_set:\n",
        "                                closed_set.remove(m)\n",
        "                                open_set.add(m)\n",
        "            if n == None:\n",
        "                print('Path does not exist!')\n",
        "                return None\n",
        "            if n == stop_node:\n",
        "                path = []\n",
        "                while parents[n] != n:\n",
        "                    path.append(n)\n",
        "                    n = parents[n]\n",
        "                path.append(start_node)\n",
        "                path.reverse()\n",
        "                print('Path found: {}'.format(path))\n",
        "                return path\n",
        "            open_set.remove(n)\n",
        "            closed_set.add(n)\n",
        "        print('Path does not exist!')\n",
        "        return None\n",
        "def get_neighbors(v):\n",
        "    if v in Graph_nodes:\n",
        "        return Graph_nodes[v]\n",
        "    else:\n",
        "        return None\n",
        "def heuristic(n):\n",
        "        H_dist = {\n",
        "            'A': 10,\n",
        "            'B': 8,\n",
        "            'C': 5,\n",
        "            'D': 7,\n",
        "            'E': 3,\n",
        "            'F': 6,\n",
        "            'G': 5,\n",
        "            'H': 3,\n",
        "            'I': 1,\n",
        "            'J': 0             \n",
        "        }\n",
        "        return H_dist[n]\n",
        "Graph_nodes = {\n",
        "    'A': [('B', 6), ('F', 3)],\n",
        "    'B': [('C', 3), ('D', 2)],\n",
        "    'C': [('D', 1), ('E', 5)],\n",
        "    'D': [('C', 1), ('E', 8)],\n",
        "    'E': [('I', 5), ('J', 5)],\n",
        "    'F': [('G', 1),('H', 7)] ,\n",
        "    'G': [('I', 3)],\n",
        "    'H': [('I', 2)],\n",
        "    'I': [('E', 5), ('J', 3)],\n",
        "     \n",
        "}\n",
        "aStarAlgo('A', 'J')\n",
        "\n",
        "\n"
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