#!/usr/bin/env python

"""
track hp through combat

don't let HP go above max

out of scope:
    - identifying insta-death
    - temp hp

saving/reading player character (pc) data:

    file name format: <playername>.<pcname>

    data format is a single string of the form:

    <playername>:<charname>:<maxhp>:<lasthp>

    e.g.

        frank:zoltan the magnificent:100:75
"""
import lib

print('Hello. This program will track HP changes during your game.  '
      'First we\'ll see if you have existing data, if not we\'ll create it.  \n'
      'Then we\'ll enter \'combat\' mode.  \n'
      'When entering HP changes, the tracker assumes HP loss.  '
      'Enter a plus (+) to increase, e.g. +10 will add '
      '10 HP\n')

player_info = lib.get_info()

lib.combat(player_info)

lib.post_combat(player_info)