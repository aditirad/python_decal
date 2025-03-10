{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMUBZF+e5kBVBNEkqRfhr3A",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/aditirad/python_decal/blob/main/HW4_Python_Decal_Aditi_Radhakrishnan.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2.1 Making a List Variable\n",
        "\n",
        "Create a variable (name it anything you want, but make it descriptive!) that\n",
        "is assigned to a list with numbers 0 through 20. You should not write each\n",
        "number manually.\n",
        "\n",
        ">>> whateverNameYouWant = # Your code here\n",
        "\n",
        ">>> print(whateverNameYouWant)\n",
        "\n",
        "[0, 1, 2, ..., 20] # It should print all numbers 1-20 in a list"
      ],
      "metadata": {
        "id": "NxL4upqPvWxq"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hXNO_9RKuudc",
        "outputId": "b48dc568-b2ab-481e-9e99-40fea53e8a62"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]\n"
          ]
        }
      ],
      "source": [
        "# 2.1 Making a List Variable\n",
        "numbers_list = list(range(21))\n",
        "print(numbers_list)  # [0, 1, 2, ..., 20]"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2.2 Working with List Elements\n",
        "\n",
        "Write a function that will take in your list from Part 2.1 and square each element in the list. Assign the result to a new variable.\n",
        "\n",
        ">>> whateverNameYouWant = # Your code from Part 2.1\n",
        "\n",
        ">>> def squareList():\n",
        "\n",
        ">>> # Your code here\n",
        "\n",
        ">>> anotherNameYouWant = squareList(list)\n",
        "\n",
        ">>> print(anotherNameYouWant)\n",
        "\n",
        "[0, 1, 4, ..., 400]"
      ],
      "metadata": {
        "id": "SAkJnlJavmaJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# 2.2 Squaring List Elements\n",
        "def square_list(lst):\n",
        "    \"\"\"Takes a list and returns a new list with each element squared.\"\"\"\n",
        "    return [x ** 2 for x in lst]\n",
        "\n",
        "squared_list = square_list(numbers_list)\n",
        "print(squared_list)  # [0, 1, 4, ..., 400]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ila7IAfKu8ro",
        "outputId": "da422312-866c-480a-9f2a-d7adde35ec30"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2.3 Slicing\n",
        "\n",
        "Write a function that takes in your new list from Part 2.2 and returns the first\n",
        "15 elements of the list using slicing.\n",
        ">>> anotherNameYouWant = squareList(list)\n",
        ">>> first_fifteen_elements(anotherNameYouWant)\n",
        "[0, 1, 4, ..., 196]"
      ],
      "metadata": {
        "id": "uTU1hEZWv4Y4"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# 2.3 Slicing First 15 Elements\n",
        "def first_fifteen_elements(lst):\n",
        "    \"\"\"Returns the first 15 elements of a list.\"\"\"\n",
        "    return lst[:15]\n",
        "\n",
        "print(first_fifteen_elements(squared_list))  # [0, 1, 4, ..., 196]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3t-Z9wuOu_gl",
        "outputId": "d59d3500-6332-4c73-b351-2f60c56d79d0"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2.4 Striding\n",
        "\n",
        "Write a function that takes in your list from Part 2.2 and returns every 5th\n",
        "element from the list using striding.\n",
        ">>> anotherNameYouWant = squareList(list)\n",
        ">>> every_fifth_element(anotherNameYouWant)\n",
        "[16, 81, 196, 361]"
      ],
      "metadata": {
        "id": "a74yHtUmwBJ6"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# 2.4 Striding Every 5th Element\n",
        "def every_fifth_element(lst):\n",
        "    \"\"\"Returns every 5th element from a list.\"\"\"\n",
        "    return lst[4::5]  # Starts at index 4 (5th element), strides by 5\n",
        "\n",
        "print(every_fifth_element(squared_list))  # [16, 81, 196, 361]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6aZU_q7CvCvg",
        "outputId": "358436c9-210b-482a-8207-b25c96efbc3e"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[16, 81, 196, 361]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2.5 Slicing & Striding\n",
        "\n",
        "Write a function that takes your list from Part 2.2, slices the last 3 elements of\n",
        "the list, and then returns every 3rd element from that list in reverse order.\n",
        ">>> anotherNameYouWant = squareList(list)\n",
        ">>> fancy_function(anotherNameYouWant)\n",
        "[400, 289, 196, 121, 64, 25, 4]"
      ],
      "metadata": {
        "id": "_BszB5nLwMwn"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# 2.5 Slicing & Striding in Reverse\n",
        "def fancy_function(lst):\n",
        "    \"\"\"Slices the last 3 elements, then returns every 3rd element in reverse order.\"\"\"\n",
        "    return lst[-21:: -3]  # Takes last 21 elements and strides backwards by 3\n",
        "\n",
        "print(fancy_function(squared_list))  # [400, 289, 196, ..., 4]\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ojwun0f1vE0b",
        "outputId": "ab15b62a-c747-42b6-cc93-4ee3c6c2f178"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "3.1 Creating a 5x5 2D List\n",
        "\n",
        "Write a function that uses nested for loops to create a 5x5 2D list where the\n",
        "numbers 1 through 25 are stored sequentially. Assign the result to a new variable.\n",
        ">>> matrix = create_2d_list()\n",
        ">>> print(matrix)\n",
        "[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],\n",
        "[16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]"
      ],
      "metadata": {
        "id": "cIzx_0glwSnB"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# 3.1 Creating a 5x5 2D List\n",
        "def create_2d_list():\n",
        "    \"\"\"Creates a 5x5 2D list with numbers 1 through 25 sequentially.\"\"\"\n",
        "    return [[i + j * 5 + 1 for i in range(5)] for j in range(5)]\n",
        "\n",
        "matrix = create_2d_list()\n",
        "print(matrix)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "S9B9Py5HvGti",
        "outputId": "333c5a92-8cfc-4eb6-9a7c-7eb2042c591a"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "3.2 Replacing 2D List with Multiples of 3\n",
        "\n",
        "With the 2D list you created in Part 3.1, write a function that will replace all\n",
        "multiples of 3 with the character “?”.\n",
        ">>> matrix = create_2d_list()\n",
        ">>> modified_2d_list(matrix)\n",
        "[[1, 2, ‘?’, 4, 5],\n",
        "[‘?’, 7, 8, ‘?’, 10],\n",
        "[11, ‘?’, 13, 14, ‘?’],\n",
        "[16, 17, ‘?’, 19, 20],\n",
        "[‘?’, 22, 23, ‘?’, 25]]"
      ],
      "metadata": {
        "id": "xHb_cpXEwbjI"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# 3.2 Replacing Multiples of 3 with '?'\n",
        "def modified_2d_list(matrix):\n",
        "    \"\"\"Replaces multiples of 3 in a 2D list with '?'.\"\"\"\n",
        "    return [['?' if num % 3 == 0 else num for num in row] for row in matrix]\n",
        "\n",
        "new_matrix = modified_2d_list(matrix)\n",
        "print(new_matrix)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "w4AS7Qc8vIrN",
        "outputId": "ac52938b-28bc-4b7e-9cef-7ba8c144ffb0"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[1, 2, '?', 4, 5], ['?', 7, 8, '?', 10], [11, '?', 13, 14, '?'], [16, 17, '?', 19, 20], ['?', 22, 23, '?', 25]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "3.3 Summing None-’ ?’ Elements\n",
        "\n",
        "Assign the result of your function from Part 3.2 to a variable. Write a function\n",
        "that will iterate through the new 2D list variable and return the sum of all the\n",
        "elements that are not “?”. Hint: Try using “!=”.\n",
        ">>> matrix = create_2d_list()\n",
        ">>> new_matrix = modified_2d_list(matrix)\n",
        ">>> sum_non_question_elements(new_matrix)\n",
        "217"
      ],
      "metadata": {
        "id": "0V47outMwfNH"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# 3.3 Summing Non-'?' Elements\n",
        "def sum_non_question_elements(matrix):\n",
        "    \"\"\"Sums all numeric elements in a 2D list, ignoring '?'.\"\"\"\n",
        "    return sum(num if num != '?' else 0 for row in matrix for num in row)\n",
        "\n",
        "print(sum_non_question_elements(new_matrix))  # Expected: 217"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4I4Mx7IZvKP3",
        "outputId": "1484b891-800d-4339-8934-3eb001d1da07"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "217\n"
          ]
        }
      ]
    }
  ]
}