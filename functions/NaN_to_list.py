def NaN_to_list(data, column_name):
    '''
    When dealing with a column which consist of lists, we need to change
    the type of NaNs from 'float' to 'list' in order to perform iterative 
    operations. This function detects NaNs and creates an empty list for
    missing rows.
    '''
    # Create a boolean vector for indexing
    NaN_rows = data[column_name].isnull()
    
    # Change the type of NaNs from 'float' to (empty) 'list'
    data[NaN_rows][column_name] = data[NaN_rows][column_name].apply(lambda x: [])