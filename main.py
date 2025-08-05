import subprocess
import os
import importlib.util
import sys
import urllib.request
from bs4 import BeautifulSoup
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.styles import Style
from prompt_toolkit.key_binding import KeyBindings

UseCurrentCustomCommand = False  # Set to True to use local commands, False to fetch from remote
LOCAL_COMMANDS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Commands")
REMOTE_COMMANDS_URL = "https://github.com/shan-commits2/Shell-App/tree/main/Commands"

def get_custom_commands():
    if UseCurrentCustomCommand:
        if not os.path.isdir(LOCAL_COMMANDS_DIR):
            return []
        return [f[:-3] for f in os.listdir(LOCAL_COMMANDS_DIR)
                if f.endswith(".py") and os.path.isfile(os.path.join(LOCAL_COMMANDS_DIR, f))]
    else:
        try:
            with urllib.request.urlopen(REMOTE_COMMANDS_URL) as response:
                html = response.read()
            soup = BeautifulSoup(html, "html.parser")
            commands = []
            print("Using Remote Commands Directory From Github")
            for a in soup.find_all("a", class_="js-navigation-open Link--primary"):
                name = a.text.strip()
                if name.endswith(".py"):
                    commands.append(name[:-3])
            return commands
        except Exception as e:
            print(f"[!] Failed to fetch remote commands: {e}")
            return []

def run_real_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, check=True, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"\n[!] Command failed:\n{e.output}")

def run_custom_command(command_name, args):
    command_path = os.path.join(LOCAL_COMMANDS_DIR, f"{command_name}.py")
    if not os.path.isfile(command_path):
        print(f"[!] No such local custom command: {command_name}")
        return
    spec = importlib.util.spec_from_file_location(command_name, command_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[command_name] = module
    spec.loader.exec_module(module)
    if hasattr(module, "main"):
        try:
            module.main(args)
        except Exception as e:
            print(f"[!] Error running {command_name}.py: {e}")
    else:
        print(f"[!] {command_name}.py has no main() function")

def print_header():
    os.system("cls" if os.name == "nt" else "clear")
    print(
        "╔═════════════════════════════════════════════════════╗\n"
        "║                  $ Sudo Shell                       ║\n"
        "╠═════════════════════════════════════════════════════╣\n"
        "║ Type <command> or 'exit'. Use TAB to auto-complete. ║\n"
        "╚═════════════════════════════════════════════════════╝\n"
    )

def change_directory(args):
    if not args:
        print(f"Current Directory: {os.getcwd()}")
        return
    raw_input = ' '.join(args)
    expanded = os.path.expanduser(os.path.expandvars(raw_input))
    if not os.path.isabs(expanded):
        expanded = os.path.join(os.path.expanduser("~"), raw_input)
    try:
        os.chdir(expanded)
        print(f"[✓] Changed directory to: {os.getcwd()}")
    except Exception as e:
        print(f"[!] Failed to change directory: {e}")

def main():
    print_header()
    history = InMemoryHistory()
    style = Style.from_dict({'prompt': 'ansicyan bold'})

    bindings = KeyBindings()

    @bindings.add('enter')
    def _(event):
        buffer = event.current_buffer
        if buffer.validate():
            buffer.validate_and_handle()

    @bindings.add('s-enter')
    def _(event):
        event.current_buffer.insert_text('\n')

    session = PromptSession(history=history, key_bindings=bindings)

    custom_commands = get_custom_commands()
    all_commands = sorted(set(custom_commands + ['cd', 'exit']))
    completer = WordCompleter(all_commands, ignore_case=True, sentence=True)

    while True:
        try:
            user_input = session.prompt(
                HTML('<prompt>$ Sudo: </prompt>'),
                completer=completer,
                style=style,
                multiline=True,
                prompt_continuation="... "
            ).strip()
        except (EOFError, KeyboardInterrupt):
            print("\n[Exiting...]")
            break

        if not user_input:
            continue

        if user_input.lower() == "exit":
            print("[Exited]")
            break

        parts = user_input.split()
        command = parts[0]
        args = parts[1:]

        if command == "cd":
            change_directory(args)
        elif command in custom_commands:
            run_custom_command(command, args)
        else:
            print(f"[!] '{command}' is not a recognized custom command.")

if __name__ == "__main__":
    main()
