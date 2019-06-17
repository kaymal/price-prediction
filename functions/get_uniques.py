def get_uniques(data, column_name):
    '''
    Get the unique elements from a column
    which consists of list of items. Return unique elements.
    '''
    unique_vals = set()
    
    for row in data[column_name]:
        # Add list of items to a set
        unique_vals.update(row)

    return unique_vals