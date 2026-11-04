"""Prices for the checkout."""


def apply_discount(price: float) -> float:
    """Return the price with the launch discount."""
    return round(price * 0.9, 2)
