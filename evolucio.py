"""evolucio"""
from audioop import reverse
import pandas as pd
import numpy as np


def top_average_column(data: dict, identifier: str, col: str, threshold: int) -> list:
    tuple_list = []
    for key, columns_dict in data.items():
        if len(columns_dict['year']) >= threshold and not np.isnan(columns_dict[col]).any():
            mean_value = sum(columns_dict[col]) / len(columns_dict[col])
            tuple_element = (columns_dict[identifier], 
                             mean_value, 
                             {'value': columns_dict[col], 'year': columns_dict['year']})
            tuple_list.append(tuple_element)
    tuple_list.sort(key=lambda tup: tup[1], reverse=True)
    return tuple_list
