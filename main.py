import sys
from game import Game


def main():
    file_name = check_args(sys.argv)
    Game().game_flow(file_name)
    
                           
def check_args(args):
    if len(args) != 2:
        print("Usage: python main.py <file_name>")
        exit(1)

    return args[1]


if __name__ == "__main__":
    main()