#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 8.0
#  in conjunction with Tcl version 8.6
#    Jan 15, 2024 06:39:56 PM +03  platform: Windows NT


import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import deneme6

    
_debug = True # False to eliminate debug printing from callback functions.

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = deneme6.AnaEkran(_top1)
    # Creates a toplevel widget.
    global _top2, _w2
    _top2 = tk.Toplevel(root)
    _w2 = deneme6.KutuKesim(_top2)
    # Creates a toplevel widget.
    global _top3, _w3
    _top3 = tk.Toplevel(root)
    _w3 = deneme6.LamelKesim(_top3)
    # Creates a toplevel widget.
    global _top4, _w4
    _top4 = tk.Toplevel(root)
    _w4 = deneme6.LamelKesim_1(_top4)
    root.mainloop()

def KutuKesim(*args):
    if _debug:
        print('deneme6_support.KutuKesim')
        for arg in args:
            print ('    another arg:', arg)
        sys.stdout.flush()

def anaekran(*args):
    if _debug:
        print('deneme6_support.anaekran')
        for arg in args:
            print ('    another arg:', arg)
        sys.stdout.flush()

def numara(*args):
    if _debug:
        print('deneme6_support.numara')
        for arg in args:
            print ('    another arg:', arg)
        sys.stdout.flush()

if __name__ == '__main__':
    deneme6.start_up()




