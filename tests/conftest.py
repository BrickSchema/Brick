"""
Generates tests automatically
"""
import pytest
import glob


def pytest_generate_tests(metafunc):
    """
    Generates Brick tests for a variety of contexts
    """

    # validates that example files pass validation
    if "filename" in metafunc.fixturenames:
        # example_files_1 = glob.glob("examples/*.ttl")
        example_files = glob.glob("examples/*/*.ttl")
        # example_files = set(example_files_1 + example_files_2)
        metafunc.parametrize("filename", example_files)
