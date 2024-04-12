#!/usr/bin/python3

from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.15, 0]
plt.pie(slices, explode=explode, labels=labels, shadow=True,
        startangle= 45,
        autopct='%1.1f%%')

plt.title("Pie Chart Here")
plt.tight_layout()
plt.show()

"""
    some properites:

    shadow = True
    startangle = 90
    autopct= %1.1f%%
    
"""


# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f


# Language Popularity
# slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 
# 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
# labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 
# 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']