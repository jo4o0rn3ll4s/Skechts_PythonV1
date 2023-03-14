

def categories_dict_to_string(categories: dict) -> str:
    """Transforma um dicionário de categorias em uma string
    Args:
        categories (dict): Dicionário de categorias
    Returns:
        str: String com as categorias
    """
    return ''.join([key for key, value in categories.items() if value])
