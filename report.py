#!/usr/bin/python3

""" The report module will output formatted text to the command line. """

__author__ = 'Jason Consiglio'
__date__ = '09/17/2023'

def turn_info(info_dict):
    """ Print the formatted text for each turn.
        Args:
            info_dict
        Return:
            success, failure
    """
    print('*' * 38)
    print('* TURNS * POPULATION * GRAIN * ACRES *')
    print('* ' + info_dict['turns'] +
          '    * ' + info_dict['population'] +
          '        * ' + info_dict['grain'] +
          '  * ' + info_dict['acres'] +
          '  *')


def trade_info(_grain, _acres, _trade_value):
    """ Print the formatted text based on trade details.
        Args:
            _grain, _acres, _trade_value
        Returns:
            success, failure
    """
    
