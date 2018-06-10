import argparse
import facebook

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-f', '--facebook', action="store_true", dest="facebook",
                        help='Post on facebook')

    parser.add_argument('-i', '--instagram', action="store_true", dest="instagram",
                        help='Post on instagram')

    parser.add_argument('-t', '--twitter', action="store_true", dest="twitter",
                        help='Post on twitter')
