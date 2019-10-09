import argparse

parser = argparse.ArgumentParser(description='Update Brick models.')
parser.add_argument('models', metavar='model', type=str, nargs='+',
                    help='a turtle file with a brick model')
parser.add_argument('--source',
                    help='source version')
parser.add_argument('--target',
                    help='target version')

args = parser.parse_args()

for model in args.models:
    print('Updating {}...'.format(model))