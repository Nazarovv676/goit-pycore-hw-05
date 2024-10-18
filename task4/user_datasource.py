from functools import wraps
import os
import tempfile
import models

# Path to the database file and its encoding
_db_path = "database.txt"
_file_encoding = "UTF-8"
_eol = "\n"  # End of line character


class DatabaseNotFoundError(Exception):
    """Custom exception raised when the database file is not found."""

    pass


class UserNotFoundError(Exception):
    """Custom exception raised when the user is not found."""

    def __init__(self, name: str):
        self.name = name
        super().__init__(f"User '{self.name}' not found.")


def database_required(func):
    """Decorator that checks for the existence of the database file.

    Raises:
        DatabaseNotFoundError: If the database file is not found.
    """

    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            raise DatabaseNotFoundError("Database file not found.")

    return inner


@database_required
def add(user):
    """Adds a new user to the database.

    Args:
        user (dict): A dictionary representing the user to add.

    Raises:
        ValueError: If user info is not provided.
    """
    if not user:
        raise ValueError("Provide user info.")
    with open(_db_path, "a", encoding=_file_encoding) as file:
        file.write(models.serialize_user(user) + _eol)


@database_required
def update(user):
    """Updates an existing user in the database.

    Args:
        user (dict): A dictionary representing the user to update.

    Raises:
        ValueError: If user info is not provided or user is not found.
        UserNotFoundError: If the user with the given name is not found.
    """
    if not user:
        raise ValueError("Provide user info.")

    updated = False
    # Use a temporary file to update user info
    with open(
        _db_path, "r", encoding=_file_encoding
    ) as file, tempfile.NamedTemporaryFile(
        "w", delete=False, encoding=_file_encoding
    ) as temp_file:
        for line in file:
            record = models.parse_user(line)
            if record["name"] == user["name"]:
                updated_record = models.serialize_user(user)
                temp_file.write(updated_record + _eol)
                updated = True
            else:
                temp_file.write(line)

    if updated:
        os.replace(temp_file.name, _db_path)
        return user
    else:
        os.remove(temp_file.name)
        raise UserNotFoundError(user["name"])


@database_required
def get_by_name(name):
    """Retrieves a user by their name from the database.

    Args:
        name (str): The name of the user to retrieve.

    Raises:
        ValueError: If user name is not provided.
        UserNotFoundError: If the user with the given name is not found.

    Returns:
        dict: The user record if found.
    """
    if not name:
        raise ValueError("Provide user name.")
    with open(_db_path, "r", encoding=_file_encoding) as file:
        for line in file:
            record = models.parse_user(line)
            if record["name"] == name:
                return record
    raise UserNotFoundError(name)


@database_required
def get_all():
    """Retrieves all users from the database.

    Returns:
        list: A list of user records.
    """
    with open(_db_path, "r", encoding=_file_encoding) as file:
        return [models.parse_user(line) for line in file]
