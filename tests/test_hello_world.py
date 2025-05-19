import unittest
import subprocess

class TestHelloWorld(unittest.TestCase):

    def test_hello_world_output(self):
        process = subprocess.run(['python', '../hello_world.py'], capture_output=True, text=True)
        self.assertEqual(process.stdout, "Hello, World!\n")

if __name__ == '__main__':
    unittest.main()
