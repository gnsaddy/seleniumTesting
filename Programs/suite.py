import unittest as ut
from Programs import ChromeLaunch
from Programs import FirefoxLaunch


class Test_Suite(ut.TestCase):
    def test_main(self):
        self.suite = ut.TestSuite()
        self.suite.addTests([
            ut.defaultTestLoader.loadTestsFromTestCase(ChromeLaunch.ChromeLaunch),
            ut.defaultTestLoader.loadTestsFromTestCase(FirefoxLaunch.FirefoxLaunch),
        ])

        runner = ut.TextTestRunner()
        runner.run(self.suite)


if __name__ == "__main__":
    ut.main()
