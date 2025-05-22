import subprocess
import sys
import unittest

class TestHello(unittest.TestCase):

    def test_hello_world_output(self):
        """Tests if the hello.py script prints 'Hello, World!'."""
        try:
            # Run the hello.py script using the same Python interpreter
            result = subprocess.run(
                [sys.executable, "-m", "src.hello"], 
                capture_output=True, 
                text=True, 
                check=True
            )
            # Check if the output is "Hello, World!"
            self.assertEqual(result.stdout.strip(), "Hello, World!")
        except subprocess.CalledProcessError as e:
            self.fail(f"Running hello.py failed: {e}\nOutput:\n{e.stdout}\nError:\n{e.stderr}")
        except FileNotFoundError:
            self.fail("Could not find src/hello.py or python interpreter.")

if __name__ == "__main__":
    unittest.main()
