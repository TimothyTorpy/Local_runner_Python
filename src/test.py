import unittest as ut
import script as script
from unittest.mock import patch
from io import StringIO


##Please note that the obessive comments are just for my own understanding of the code. 
##From reseach and what i am attempting to do.


class TestScript(ut.TestCase):
    def setUp(self): ##Pulls the list from the script file. To ensure it is always up to date.
        self.list_w = script.w
        print("Setup Completed")
        
    def test_a(self): ##Tests the function a to make sure it returns a word from the list.
        self.assertIn(script.a(), self.list_w)
        
        
class stringValidations(ut.TestCase):
    @patch(('builtins.input'), side_effect=['a'])##Patch mocks the input function, Side Effect is the inputs on each call.
    def test_single_letter(self, mock_input):##Mock_input is inculed in the patch function.
        self.assertEqual(script.f(), "a")
        
    
    @patch(('builtins.input'), side_effect=['1', 'a'])
    def test_number_then_letter(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as fake_out:##with patch(sys.stdout) mocks and grabs the output of the function.
            self.assertEqual(script.f(), "a")
            self.assertIn("Please enter a single letter.",fake_out.getvalue())
            
            
            
    @patch(('builtins.input'), side_effect=['aa', 'b'])
    def test_multiple_letters(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as fake_out:
            self.assertEqual(script.f(), "b")
            self.assertIn("Please enter a single letter.",fake_out.getvalue())
            
            
    @patch(('builtins.input'), side_effect=['B'])
    def test_uppercase(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as fake_out:
            self.assertEqual(script.f(), "b")
            
            
class test_hangman(ut.TestCase):
    @patch('random.choice', return_value='dog')
    @patch('builtins.input', side_effect=['d','o','z','z','g'])
    def test_repeated_input(self, mock_input, mock_choice):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            script.h()
            ##check for correct handling of repeated input
            self.assertIn("You've already guessed that letter.", fake_out.getvalue())
            ##check for game state after repeated input
            self.assertIn("Congratulations! You guessed the word: dog", fake_out.getvalue())
            
            output = fake_out.getvalue()
            attempts = [int(line.split(':')[1]) for line in output.split('\n') if "Attempts left:" in line]
            self.assertEqual(attempts, [6, 6, 6, 5, 5])
            

if __name__ == "__main__":
    ut.main()

