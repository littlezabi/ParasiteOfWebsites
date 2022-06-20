import variables as vars
from subprocess import check_output


def run_browser():
    command = f"C:\Program Files\Google\Chrome\Application\chrome.exe https://web.whatsapp.com/ --remote-debugging-port=9222 --user-data-dir=C:/whatsapp/"
    print(f"""
Opening Browser:
    host: 127.0.0.1
    port: 9222
    profile: C:/whatsapp/
    """)
    print("if browser is opened you can close this program")
    command = check_output(command)
    exit()


run_browser()
