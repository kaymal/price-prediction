def name_columns(data):
    '''
    Name columns with underscore(_) convention.
    '''
    # Clean "\n"s from the column names
    data.columns = data.columns.str.strip("\n")

    # Make lowercase
    data.columns = data.columns.str.lower()
    
    # Replace space with underscore(_)
    data.columns = data.columns.str.replace(" ", "_")
    
    # Replace . with ""
    data.columns = data.columns.str.replace(".", "")
    
    # Replace "_&_" with "&"
    data.columns = data.columns.str.replace("_&_", "_")
    
    # Replace "-" with "_"
    data.columns = data.columns.str.replace("-", "_")
    
    return data.columns