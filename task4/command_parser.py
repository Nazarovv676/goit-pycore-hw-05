import re
import command_handler

def parse(command: str) -> int:
    """
    Parses a command string and executes the corresponding action.

    Args:
        command (str): The command string input by the user.

    Returns:
        int: 
            - 1 if the command is "close" or "exit".
            - 0 if the command is unknown.
            - No return value for other commands (prints output directly).
    """

    # Check for exit commands
    if re.search(r"^close$|^exit$", command, re.IGNORECASE):
        print("🤖\tGoodbye!")
        return 1

    # Check for greeting command
    elif re.search(r"^hello$", command, re.IGNORECASE):
        print("🤖\tHow can I help you?")

    # Check for "add" command to add a user
    elif match := re.search(r"^add\s*(?P<name>\w+)?\s*(?P<phone>[\d\+\-\(\)\s]+)?$", command, re.IGNORECASE):
        name = match.group("name")
        phone_number = match.group("phone")
        res = command_handler.add_user(name, phone_number)
        print(res)

    # Check for "change" command to modify user details
    elif match := re.search(r"^change\s*(?P<name>\w+)?\s*(?P<phone>[\d\+\-\(\)\s]+)?$", command, re.IGNORECASE):
        name = match.group("name")
        phone_number = match.group("phone")
        res = command_handler.change_user(name, phone_number)
        print(res)

    # Check for "phone" command to retrieve user's phone number
    elif match := re.search(r"^phone\s*(?P<name>\w+)?$", command, re.IGNORECASE):
        name = match.group("name")
        res = command_handler.get_user_phone(name)
        print(res)

    # Check for "all" command to list all users
    elif re.search(r"^all\s*$", command, re.IGNORECASE):
        res = command_handler.get_all()
        print(res)

    # Check for "help" command to show available commands
    elif re.search(r"^help\s*$", command, re.IGNORECASE):
        res = command_handler.show_help()
        print(res)

    # Handle unknown commands
    else:
        print("🤖\tUnknown command. Please try one more time.")
        return 0
