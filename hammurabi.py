#!/usr/bin/python3

""" The game of Hammurabi to practice while taking a python course """

__author__ = 'Jason Consiglio'
__date__ = '09/17/2023'

import trade
import event
import calculate
import report
import time

def main():
    """ Start the game, and call various functions from appropriate modules.
        Args:
            none
        Return:
            none
    """
    info_dict = {
        'turns':'10',
        'population':'100',
        'grain':'2800',
        'acres':'1000',
        'rat_mod': '2.3',
        'plague_mod': '2.3',
        'pop_mod': '2.3'
        }
    while True:
        report.turn_info(info_dict)
        time.sleep(2)
        

if __name__ == '__main__':
    main()
