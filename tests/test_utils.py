import io
import sys
import unittest

from lib import utils


class TestUtils(unittest.TestCase):
    def test_log_outputs_prefix_and_message(self):
        buf = io.StringIO()
        old_stdout = sys.stdout
        try:
            sys.stdout = buf
            utils.log("hello")
        finally:
            sys.stdout = old_stdout

        output = buf.getvalue().strip()
        self.assertTrue(output.startswith("[osint-utils] "))
        self.assertIn("hello", output)


if __name__ == "__main__":
    unittest.main()
