from tabulate import tabulate
import user_datasource
from input_error_handler import input_error


@input_error(
    "🤖\tGive me a name and phone number please.\n\tUsage: `add <name> <phone>`\n\tExample: `add John 1234567890`."
)
def add_user(name, phone):
    user_datasource.add(
        {
            "name": name,
            "phone": phone,
        }
    )

    return f"🤖\tUser '{name}' has been added."


@input_error(
    "🤖\tGive me a name and phone number please.\n\tUsage: `change <name> <phone>`\n\tExample: `change John 0987654321`."
)
def change_user(name, phone):
    user_datasource.update(
        {
            "name": name,
            "phone": phone,
        }
    )

    return f"🤖\tUser '{name}' has been changed."


@input_error(
    "🤖\tPlease provide the name.\n\tUsage: `phone <name>`\n\tExample: `phone John`."
)
def get_user_phone(name):
    user = user_datasource.get_by_name(name)
    phone = user["phone"]

    return f"🤖\tUser phone: '{phone}'."


@input_error("🤖\tSorry... Some error occurred when retrieving users.")
def get_all():
    users = user_datasource.get_all()
    table_data = [(user["name"], user["phone"]) for user in users]

    return tabulate(table_data, headers=["Name", "Phone"], tablefmt="fancy_grid")


def show_help():
    help_text = """
🤖 Command Line Tool

Usage:
    command [options]

Available Commands:
    add <name> <phone>        Adds a new user with the specified name and phone number.
                              Example: `add John 1234567890`

    change <name> <phone>     Updates the phone number of an existing user.
                              Example: `change John 0987654321`

    phone <name>              Retrieves the phone number of the specified user.
                              Example: `phone John`

    all                       Displays all users and their phone numbers.

    hello                     Greets the user and offers assistance.

    help                      Displays this help message.

    close / exit              Exits the application.
"""
    return help_text
