import unittest2 as unittest
import os
import robotsuite
from plone.testing import layered
from plonetheme.bootstrap.testing import BOOTSTRAPTHEME_ROBOT


def test_suite():
    suite = unittest.TestSuite()
    current_dir = os.path.abspath(os.path.dirname(__file__))
    robot_dir = os.path.join(current_dir, 'robot')
    robot_tests = [
        os.path.join('robot', doc) for doc in
        os.listdir(robot_dir) if doc.endswith('.robot') and
        doc.startswith('test_')
    ]
    for test in robot_tests:
        suite.addTests([
            layered(robotsuite.RobotTestSuite(test),
                    layer=BOOTSTRAPTHEME_ROBOT),
        ])
    return suite
