import getpass
import msvcrt
def hide_password():
    def get_hidden_input(prompt="Enter your password: "):
        print(prompt, end='', flush=True)
        password = b''
        while True:
            char = msvcrt.getch()
            if char in {b'\n', b'\r'}:
                print('')
                return password.decode('utf-8')
            elif char == b'\003':  # Ctrl+C
                raise KeyboardInterrupt
            elif char == b'\b':  # Backspace
                password = password[:-1]
                print('\b \b', end='', flush=True)
            else:
                password += char
                print('*', end='', flush=True)

    password = get_hidden_input()
    return password
