def sort(width: float, height: float, length: float, mass: float) -> str:
    """
     Sort packages according to their size and mass

    Args: 
        width (float): Package width in centimeters
        length (float): Package length in centimeters
        height (float): Package height in centimeters
        mass (float): Package weight in kilograms

    Returns:
        str: "STANDARD", "SPECIAL", or "REJECTED"

    Raises:
        TypeError: If any input is not a number
        ValueError: If any dimension or mass is negative
    """
    # Input validation (positive numbers only)
    try:
        width, height, length, mass = map(float, (width, height, length, mass))
    except (TypeError, ValueError) as e:
        raise TypeError("All inputs must be numeric") from e

    if any(x < 0 for x in (width, height, length, mass)):
        raise ValueError("Dimensions and weight must be non-negative")

    # Calculate volume
    volume = width * height * length

    is_big = (volume >= 1_000_000 or max(width, height, length) >= 150)
    is_heavy = (mass >= 20)

    if is_big and is_heavy:
        return "REJECTED"
    
    if is_big or is_heavy:
        return "SPECIAL"
    
    return "STANDARD"

        