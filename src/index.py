import sys
from ui import main

if __name__ == "__main__":
    try:
        main()
        sys.exit()
    except KeyboardInterrupt:
        print("\n*** Quitting the program. Bye! ***")
        sys.exit()
    except Exception as e:
        print(f"There was an error: {e}")
        sys.exit(1)
