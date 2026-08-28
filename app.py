def calculate_discount(price, discount):
    if discount < 0 or discount > 100:
        raise ValueError("Invalid discount percentage")
    return price * (1 - discount / 100)
if __name__ == "__main__":
    print(f"Final Price: {calculate_discount(100, 20)}")