from api import fetcher


def main_wrapper():
    print("This is the start of my Python project. This function's name is {main_wrapper.__name__}")

    # Code here
    fetcher.states_accessor()


if __name__ == "__main__":
    main_wrapper()
