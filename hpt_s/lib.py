
#!/usr/bin/env python

"""
*** THIS IS THE OLD VERSION OF MY HITPOINT TRACKER FUNCTIONS***

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
import os

def gen_char_file_name(player_name, character_name, character_data_directory=None):
    """
        return the file name used to hold character data from 

        returns a relative path of the form:

            <character_data_directory>/<player_name>.<character_name>
    """

    file_name = player_name + '.' + character_name

    if character_data_directory:

        file_name = os.path.join(character_data_directory, file_name)


    return file_name



def get_info():
    """
    get basic player data, then attempt to read HP data from file 
    with name based on basic info.  If fail, then create the file 
    and gather the HP data too.

    return all the info gathered in a dict

    {'player_name': <player name>, 
     'pc_name'
     'maximum_hp': <maxhp>, 
     'current_hp': <currenthp>, 
     'file': <datafile>}
    """

    player = input('What is your name (player): ')
    pc = input('What is your character\'s name: ')  # todo change pc to character or similar - player and pc might be confused for one another
    pc_data_file_name = gen_char_file_name(player, pc, 'chars')  # todo make chars dir a param

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


    char_data = {'player_name': player, 
                 'pc_name': pc, 
                 'maximum_hp':maxhp, 
                 'current_hp': currhp, 
                 'file': pc_data_file_name}

    return char_data


def combat(pdata):
    """
    run combat loop using player data (in pdata)

    return (None)
    """

    maxhp = pdata['maximum_hp']
    currhp = pdata['current_hp']

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

    pdata['current_hp'] = currhp


def post_combat(pdata):
    """
    Clean up tasks run after user ends combat loop.

    e.g. display final stats, save to file for use next time
    """

    maxhp = pdata['maximum_hp']
    currhp = pdata['current_hp']
    player = pdata['player_name']
    pc = pdata['pc_name']
    fname = pdata['file']

    print('Final HP is {}/{}'.format(currhp, maxhp))

    with open(fname, 'w') as pc_data:

        data = ':'.join([player, pc, str(maxhp), str(currhp)])  # prep data for storage

        pc_data.write(data + '\n')  # store the data