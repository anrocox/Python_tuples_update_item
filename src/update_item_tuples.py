#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 7, 2014

@author: anroco

How to modify items of a tuple in python?

¿Como modificar elementos de una tupla en python?
'''

#create a tuple
tupla = ('s', 1, [], False)
print (tupla)

#tuples are immutable, so you can not modify items which are also immutable,
#as str, boolean, numbers etc.
tupla[2].append(500)
print(tupla)
