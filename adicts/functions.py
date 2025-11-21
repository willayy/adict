import numpy as np

def sub(
    d1: dict,
    d2: dict,
) -> dict:
    """
    Subtracts values of two dictionaries for common keys.
    :param d1: First dictionary
    :type d1: dict
    :param d2: Second dictionary
    :type d2: dict
    :return: Dictionary with subtracted values for common keys
    :rtype: dict
    """
    common_keys = d1.keys() & d2.keys()
    return {k: d1[k] - d2[k] for k in common_keys}


def add(
    d1: dict,
    d2: dict,
) -> dict:
    """
    Adds values of two dictionaries for common keys.

    :param d1: First dictionary
    :type d1: dict
    :param d2: Second dictionary
    :type d2: dict
    :return: Dictionary with summed values for common keys
    :rtype: dict
    """
    common_keys = d1.keys() & d2.keys()
    return {k: d1[k] + d2[k] for k in common_keys}


def crem(d: dict, how: str, cond: callable) -> dict:
    """
    Removes items from dictionary based on condition applied to keys or values.

    :param d: Input dictionary
    :type d: dict
    :param how: "k" to apply condition to keys, "v" to values
    :type how: str
    :param cond: Condition function that returns True for items to remove
    :type cond: callable
    :return: Filtered dictionary
    :rtype: dict
    """
    if how == "v":
        return {k: v for k, v in d.items() if not cond(v)}
    if how == "k":
        return {k: v for k, v in d.items() if not cond(k)}
    if how not in ["k", "v"]:
        raise ValueError(f"How has illegal argument: {how}")


def rem(d: dict, keys: list[str]) -> dict:
    """
    Removes specified keys from the dictionary.
    
    :param d: Input dictionary
    :type d: dict
    :param keys: List of keys to remove
    :type keys: list[str]
    :return: Filtered dictionary
    :rtype: dict
    """
    return {k: v for k, v in d.items() if k not in keys}


def to_np(d: dict, how: str = "v") -> np.ndarray:
    """
    Converts dictionary keys or values to a NumPy array.
    
    :param d: Input dictionary
    :type d: dict
    :param how: "k" to convert keys, "v" to convert values
    :type how: str
    :return: NumPy array of keys or values
    :rtype: ndarray[_AnyShape, dtype[Any]]
    """
    if how == "v":
        return np.array(list(d.values()))
    if how == "k":
        return np.array(list(d.keys()))
    if how not in ["k", "v"]:
        raise ValueError(f"How has illegal argument: {how}")


def mul(d: dict, factor: dict | int | float) -> dict:
    """
    Multiplies dictionary values by a factor, which can be a scalar or another dictionary.
    
    :param d: Input dictionary
    :type d: dict
    :param factor: Scalar factor or dictionary of factors
    :type factor: dict | int | float
    :return: Scaled dictionary
    :rtype: dict
    """
    if isinstance(factor, (float, int)):
        return {k: d[k] * factor for k in d.keys()}
    if isinstance(factor, dict):
        return {k: d[k] * factor.get(k, 1) for k in d.keys()}
    else:
        raise ValueError(f"Factor has illegal type: {type(factor)}")


def pow(d: dict, exponent: dict | int | float) -> dict:
    """
    Raises dictionary values to a power, which can be a scalar or another dictionary.

    :param d: Input dictionary
    :type d: dict
    :param exponent: Scalar exponent or dictionary of exponents
    :type exponent: dict | int | float
    :return: Dictionary with values raised to the specified powers
    :rtype: dict
    """
    if isinstance(exponent, (float, int)):
        return {k: d[k] ** exponent for k in d.keys()}
    if isinstance(exponent, dict):
        return {k: d[k] ** exponent.get(k, 1) for k in d.keys()}
    else:
        raise ValueError(f"Exponent has illegal type: {type(exponent)}")


def apply(func: callable, d: dict, how: str = "v") -> dict:
    """
    Applies a function to either the keys or values of a dictionary.
    
    :param func: Function to apply
    :type func: callable
    :param d: Input dictionary
    :type d: dict
    :param how: "k" to apply to keys, "v" to values
    :type how: str
    :return: Dictionary with function applied to keys or values
    :rtype: dict
    """
    if how == "v":
        return {k: func(v) for k, v in d.items()}
    if how == "k":
        return {func(k): v for k, v in d.items()}
    if how not in ["k", "v"]:
        raise ValueError(f"How has illegal argument: {how}")
