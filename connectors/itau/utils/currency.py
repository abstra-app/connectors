def str_to_cents(value: str) -> int:
    """
    Converts a string representation of a monetary value to cents.
    
    Args:
        value (str): The monetary value as a string, e.g., "123.45".
        
    Returns:
        int: The value in cents, e.g., 12345 for "123.45".
    """
    if not value:
        return 0
    return int(float(value) * 100)