import sys
from ui import main

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n*** Quitting the program. Bye! ***")
        sys.exit()
    except Exception as e:
        print("There was an error: {e}")
        sys.exit(1)
