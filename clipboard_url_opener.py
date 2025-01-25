# pip install pyperclip
# clipboard_url_opener listens to the clipboard and automatically opens any newly copied URL in default web browser.

import pyperclip
import webbrowser
import time
import re

def is_valid_url(url):
    regex = re.compile(
        r'^(https?:\/\/)?'
        r'([\w\-]+\.)+[\w\-]{2,}'
        r'(\/[\w\-./?%&=]*)?$',
        re.IGNORECASE
    )
    return re.match(regex, url) is not None

def main():
    last_clipboard_content = ""
    while True:
        try:
            current_clipboard_content = pyperclip.paste()
            if current_clipboard_content != last_clipboard_content and is_valid_url(current_clipboard_content):
                last_clipboard_content = current_clipboard_content
                webbrowser.open(current_clipboard_content)
            time.sleep(1)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
