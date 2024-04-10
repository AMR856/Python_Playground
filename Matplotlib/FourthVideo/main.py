#!/usr/bin/python3

from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

lables = ['player1', 'player2', 'player3']
colors = ['#6d904f', '#008fd5', '#e5ae37']


"""
    player1.reverse()
    player2.reverse()
    player3.reveres()

    Here are all of the locations for legend (according to documentation):
    'best'
    'upper right'
    'upper left'
    'lower left'
    'lower right'
    'right'
    'center left'
    'center right'
    'lower center'
    'upper center'
    'center'
"""


plt.stackplot(minutes, player1, player2, player3, labels=lables, colors=colors)

# plt.legend(loc='lower left')
plt.legend(loc=(0.07, 0.05))
plt.title("My StackPlot")
plt.tight_layout()
plt.show()