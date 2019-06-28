def string_to_list(data, column_name):
     # Create a boolean vector for indexing
    not_NaN_rows = data[column_name].notnull()
    
    # Change the type of notNaNs from 'string' to (empty) 'list'
    data.loc[not_NaN_rows, column_name] = data.loc[not_NaN_rows, column_name].apply(lambda x: x.split(','))

def clean_m(data):
    
    df=data
    
    reg_new = df.registration[~df.registration.str.contains("-")]
    reg_new = pd.to_datetime(reg_new, format='%m/%Y')
    reg_year = reg_new.apply(lambda x: x.year)
    
    df['age'] = 2019 - reg_year
    
    df=df.join(df['gearing_type'].str.join('|').str.get_dummies().add_prefix('gearing_type_'))
    
    df=df.join(df['body'].str.join('|').str.get_dummies().add_prefix('body_'))
    
    df=df.join(df['body_color'].str.join('|').str.get_dummies().add_prefix('body_color_'))
    
    df=df.join(df['entertainment_media'].str.join('|').str.get_dummies().add_prefix('entertainment_media_'))
    
    string_to_list(df, 'vat')
    df=df.join(df['vat'].str.join('|').str.get_dummies().add_prefix('vat_'))
    
    df=df.join(df['gears'].str.join('|').str.get_dummies().add_prefix('gears_'))
    
    df=df.join(df['paint_type'].str.join('|').str.get_dummies().add_prefix('paint_type_'))
    
    name_columns(df)
    
    drop_list=['entertainment_media', 'availability', 'available_from', 'body',
       'body_color', 'body_color_original', 'full_service', 'gearing_type',
       'gears', 'inspection_new', 'last_service_date',
       'last_timing_belt_service_date', 'paint_type', 'null', 
       'registration', 'short_description', 'vat', 'gearing_type_',
       'body_', 'body_color_']
    df.drop(drop_list, axis=1, inplace=True)
    
    df.columns=df.columns.str.translate({ord('\n'): None})
    
    return df