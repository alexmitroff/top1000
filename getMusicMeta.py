import argparse

from core.top import Top


def get_arguments():
    parser = argparse.ArgumentParser(description='get additional data from Spotify')
    parser.add_argument('-f', '--file',
                        dest='csvfile',
                        required=True, help='path to CSV file')
    return parser.parse_args()


def run():
    args = get_arguments()
    csv_file_path = getattr(args, 'csvfile')
    top = Top()
    top.import_CSV(csv_file_path)
    print(top.top)


if __name__ == '__main__':
    run()
