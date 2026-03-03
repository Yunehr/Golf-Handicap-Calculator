def check_credentials(username, password):
    """
    Check if the provided credentials are valid.
    Currently hardcoded for testing. Update this function for proper authentication.
    
    Args:
        username: The username to verify
        password: The password to verify
        
    Returns:
        True if credentials are valid, False otherwise
    """
    valid_username = "admin"
    valid_password = "password"
    
    return username == valid_username and password == valid_password
