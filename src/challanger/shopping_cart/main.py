def validate_number(value: object, field_name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(
            f"{field_name} deve ser um número inteiro ou decimal."
        )


def validate_discount(discount: int | float) -> None:
    if not 0 <= discount <= 100:
        raise ValueError("O desconto deve estar entre 0 e 100.")


def validate_price(price: int | float) -> None:
    if price < 0:
        raise ValueError("O preço não pode ser negativo.")


def calculate_discounted_price(
    price: int | float,
    discount: int | float,
) -> float:
    """Calcula o preço final após aplicar um desconto percentual."""

    validate_number(price, "O preço")
    validate_number(discount, "O desconto")
    validate_price(price)
    validate_discount(discount)

    return price - (price * discount / 100)


print(calculate_discounted_price(100, 10))