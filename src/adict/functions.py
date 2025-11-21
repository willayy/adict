import numpy as np


def sub(
    d1: dict,
    d2: dict,
) -> dict:
    common_keys = d1.keys() & d2.keys()
    return {k: d1[k] - d2[k] for k in common_keys}


def add(
    d1: dict,
    d2: dict,
) -> dict:
    common_keys = d1.keys() & d2.keys()
    return {k: d1[k] + d2[k] for k in common_keys}


def crem(d: dict, how: str, cond: callable) -> dict:
    if how == "v":
        return {k: v for k, v in d.items() if not cond(v)}
    if how == "k":
        return {k: v for k, v in d.items() if not cond(k)}
    if how not in ["k", "v"]:
        raise ValueError(f"How has illegal argument: {how}")


def rem(d: dict, keys: list[str]) -> dict:
    return {k: v for k, v in d.items() if k not in keys}


def to_np(d: dict, how: str = "v") -> np.ndarray:
    if how == "v":
        return np.array(list(d.values()))
    if how == "k":
        return np.array(list(d.keys()))
    if how not in ["k", "v"]:
        raise ValueError(f"How has illegal argument: {how}")


def mul(d: dict, factor: dict | int | float) -> dict:
    if isinstance(factor, (float, int)):
        return {k: d[k] * factor for k in d.keys()}
    if isinstance(factor, dict):
        return {k: d[k] * factor.get(k, 1) for k in d.keys()}
    else:
        raise ValueError(f"Factor has illegal type: {type(factor)}")


def pow(d: dict, exponent: dict | int | float) -> dict:
    if isinstance(exponent, (float, int)):
        return {k: d[k] ** exponent for k in d.keys()}
    if isinstance(exponent, dict):
        return {k: d[k] ** exponent.get(k, 1) for k in d.keys()}
    else:
        raise ValueError(f"Exponent has illegal type: {type(exponent)}")


def apply(func: callable, d: dict, how: str = "v") -> dict:
    if how == "v":
        return {k: func(v) for k, v in d.items()}
    if how == "k":
        return {func(k): v for k, v in d.items()}
    if how not in ["k", "v"]:
        raise ValueError(f"How has illegal argument: {how}")
