import datetime

def print_timestamp():
    """Prints the current formatted timestamp."""
    now = datetime.datetime.now()
    timestamp_str = now.strftime("\n %d/%m/%Y \n %H:%M:%S\n")
    print(f" TimeStamp {timestamp_str}")

# This ensures the script still runs if you execute 'python tstamp.py' directly,
# but doesn't auto-run if someone imports it as a library.
if __name__ == "__main__":
    print_timestamp()