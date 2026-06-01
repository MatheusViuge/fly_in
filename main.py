

from Parser.Extract import Parser


if __name__ == "__main__":
    try:
        Parser()
    except Exception as e:
        print(f"Error: {e}")
