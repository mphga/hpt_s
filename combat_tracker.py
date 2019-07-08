
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

print('Hello. This program will track HP changes during your game.  '
      'First we\'ll see if you have existing data, if not we\'ll create it.  \n'
      'Then we\'ll enter \'combat\' mode.  \n'
      'When entering HP changes, the tracker assumes HP loss.  '
      'Enter a plus (+) to increase, e.g. +10 will add '
      '10 HP\n')


player = input('What is your name (player): ')
pc = input('What is your character\'s name: ')
pc_data_file_name = '.'.join([player, pc])

try:

    with open(pc_data_file_name, 'r') as pc_data: # open data file, get stats

        data = pc_data.readline()
        data = data.split(':')
        player = data[0]
        pc = data[1]
        maxhp = int(data[2])
        currhp = int(data[3])

except:

    print('No existing character, so let\'s create one.')
    
    maxhp = input('Enter max HP: ')
    currhp = input('Enter current HP (enter for max): ')

    maxhp = int(maxhp)

    if currhp:  # user entered a value other than max
        currhp = int(currhp)  # todo check validity
    else:
        currhp = maxhp  # user indicated they're at max HP now

    data = ':'.join([player, pc, str(maxhp), str(currhp)])  # prep data for storage

    with open(pc_data_file_name, 'w') as pc_data:

        pc_data.write(data + '\n')  # store the data

cont = True
while cont:

    # get input from user, which is an integer for hp adjustment
    # or nothing -- meaning end combat (end the loop)
    delta = input('\nYour current HP is: {}\nEnter HP change '
                  'or enter to quit combat: '.format(currhp))

    # if input is empty string - end loop
    if not delta:
        break

    # otherwise assume it was an integer, indicating hp adjustment
    # determine if newhp would be > max hp, if so
    # warn user value out of bounds, set currt hp to max
    # for convenience, assume default is HP loss, e.g. number w/o
    # sign = loss, must prepend '+' to indicate gain
    if not delta.startswith('+'):  # assume it's a number w/o a +/-
        delta = -int(delta)
    else:
        delta = int(delta)

    newhp = currhp + delta

    if newhp > maxhp:

        print('Your new total is greater than your max HP, '
              'setting your current HP to max HP')

        currhp = maxhp

    # else update current HP using the user entered value
    else:

        currhp = newhp

print('Final HP is {}/{}'.format(currhp, maxhp))

with open(pc_data_file_name, 'w') as pc_data:

    data = ':'.join([player, pc, str(maxhp), str(currhp)])  # prep data for storage

    pc_data.write(data + '\n')  # store the data


