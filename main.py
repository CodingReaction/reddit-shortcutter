import webbrowser
import sys
import time

print("Tip 1: you could also call the script with 'python-version main.py file_with_subreddits' instead of the default filename")

filename = sys.argv[1] if len(sys.argv) > 1 else "subreddits.txt"
try:
    with open(filename, mode='r') as file:
        counter_to_sleep = 0
        for subreddit_name in file:
            webbrowser.open_new_tab(f"https://www.reddit.com/r/{subreddit_name}/new")
            counter_to_sleep += 1
            if counter_to_sleep % 5 == 0:
                time.sleep(10)
except FileNotFoundError(err):
    print("The file that contains the subreddits lists doesn't exists.")
    print("Create a file with name subreddits.txt containing one subreddit per line (only the subreddit name)")