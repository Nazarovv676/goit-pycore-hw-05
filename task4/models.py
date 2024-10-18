import json

def parse_user(data):
    """
    Parse user data from a JSON string and validate its structure.

    Args:
        data (str): JSON string representing user data.

    Returns:
        dict: Dictionary containing user data if valid.

    Raises:
        ValueError: If JSON data does not represent a valid user dictionary or if there's an error parsing JSON.
    """
    try:
        user_dict = json.loads(data)  # Attempt to parse JSON data
        if isinstance(user_dict, dict) and "name" in user_dict and "phone" in user_dict:
            return user_dict  # Return user dictionary if it has 'name' and 'phone' keys
        else:
            raise ValueError("Parsed data is not a valid user dictionary.")
    except json.JSONDecodeError as e:
        raise ValueError(f"Error parsing JSON data: {e}")

def serialize_user(user_dict):
    """
    Serialize user data dictionary into a JSON string.

    Args:
        user_dict (dict): Dictionary containing user data.

    Returns:
        str: JSON string representing the serialized user data.

    Raises:
        ValueError: If there's an error serializing user data.
    """
    try:
        user_json = json.dumps(user_dict)  # Convert user dictionary to JSON string
        return user_json
    except (TypeError, ValueError) as e:
        raise ValueError(f"Error serializing user data: {e}")
