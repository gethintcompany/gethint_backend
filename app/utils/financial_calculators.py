def calculate_cagr(start_value: float, end_value: float, years: int):
    return (end_value / start_value) ** (1/years) - 1