import os
import unittest

import hpt_s.lib as lib

class HptTest(unittest.TestCase):

    def test_gen_char_file_name(self):

        char_dir = 'chars'
        
        player_names = [
                   'Larry Player', 
                   'Über Larry', 
                   'Larry Larry Fo Farry Fe Fi Fo Ferry Larry', 
                   ]

        char_names = [
                      'Warry Char', 
                      'Über Warry',
                     ]

        for pname in player_names:

            for cname in char_names:

                fname = lib.gen_char_file_name(pname, cname, char_dir)

                self.assertEqual(fname, os.path.join(char_dir, pname + '.' + cname))




    def test_open_existing_char(self):
         

    def test_char_data_collection(self):
        pass


if __name__ == '__main__':

    unittest.main()
