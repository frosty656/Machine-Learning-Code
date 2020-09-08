#!/usr/bin/env python
# coding: utf-8

# ## MyStats-lib
# **My library for statistical functions.**

# In[2]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import math

def mean(x):
    return round((sum(x) / len(x)), 2)

def mean_of_means(x):
    list_of_mean = [round((mean(x_i)), 2) for x_i in x]
    return mean(list_of_mean)

def data_range(x):
    return max(x) - min(x)

def diff_from_mean(x):
    x_bar = mean(x)
    return [round((x_i - x_bar), 2) for x_i in x]

def sum_of_squares(x):
    return(sum(x_i**2 for x_i in x))

def variance(x):
    l = len(x)
    deviations = diff_from_mean(x)
    return (sum_of_squares(deviations)/(l - 1))

def standard_deviation(x):
    v = variance(x)
    return math.sqrt(v)

def diff_from_mean(x):
    x_bar = mean(x)
    return [round((x_i - x_bar), 2) for x_i in x]

def sum_of_squares(x):
    return round((sum(x_i**2 for x_i in x)), 2)

def variance(x):
    l = len(x) 
    deviations = diff_from_mean(x)
    return round((sum_of_squares(deviations)/(l - 1)), 2)

