def main_test(*, package=None, verbose=False):
    print("Starting VIDAR test...")
    print()

    print("Checking for all necessary packages for VIDAR ...")
    missing_list = []
    try:
        import numpy 
        import scipy
        import sklearn
        import matplotlib
    except ImportError as e:
        missing_list.append("{0}".format(e))
    
    if len(missing_list) == 0:
        print("All required dependencies are installed.")
    else:
        print("You do not have all the required dependencies for VIDAR:")
        #print()
        for dep in missing_list:
            print(dep)
        print()
        print("You can install the above missing packages by pip or conda.")
        print()
        return 1
    
    print()
    print("Starting the VIDAR test suite:")

    test_args = ["-W", "ignore"]
    import importlib
    if package:
        try:
            importlib.import_module(f"{package}")
        except ModuleNotFoundError:
            raise ModuleNotFoundError(f"{package} was not found.")
        test_args.extend(["--pyargs", f"{package}"])
    # else:
    #     test_args.extend(["--pyargs", "VIDAR"])
        
    if verbose:
        test_args.append("-vvv")
    
    import pytest

    if verbose:
        print(f"Running pytest with arguments: {test_args}")

    return pytest.main(test_args)


if __name__ == "__main__":
    import sys
    import argparse

    parser = argparse.ArgumentParser(description="Run the VIDAR test suite")
    parser.add_argument("--package", default="vidar", help="Run the main tests of VIDAR")
    parser.add_argument('--verbose', action='store_true', help="Run the tests in verbose mode")
    test_args = parser.parse_args()
    sys.exit(
        main_test(
            package=test_args.package,
            verbose=test_args.verbose
            )
        )