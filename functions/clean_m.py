def clean_m(data):
    
    df=data
    
    #cleaning registration column and convertinf it to age column
    reg_new = df.registration[~df.registration.str.contains("-")]
    reg_new = pd.to_datetime(reg_new, format='%m/%Y')
    reg_year = reg_new.apply(lambda x: x.year)
    df['age'] = 2019 - reg_year
    
    df['gearing_type'] = df['gearing_type'].apply(lambda x:x[1])
    
    df.loc[df['body'].notnull(), 'body'] = df.loc[df['body'].notnull(), 'body'].apply(lambda x: x[1])
    
    df.loc[df['body_color'].notnull(), 'body_color'] = df.loc[df['body_color'].notnull(), 'body_color'].apply(lambda x: x[1])
      
        
    ent=df[['entertainment_media']].dropna()
    df=df.join(ent['entertainment_media'].str.join('|').str.get_dummies().add_prefix('ent_media_'))        
    
    df['gears']=df.gears.str[0].str.replace("\n", "")
    df['gears'] = pd.to_numeric(df.gears)
    
    df['paint_type']=df.paint_type.str[0].str.replace("\n", "")
    
    # converting inspection_new column to 1 if it contains Yes expression, else: 0
    df["inspection_new"] = df.inspection_new.str[0].str.contains("Yes", na=False)*1
     
    # extracting the number of days in availabiltiy column and converting column name to available_after_days
    df['availability'] = df.availability.str.extract(r'(\d+)')
    df['available_after_days'] = df.availability.apply(pd.to_numeric)
    
    # finding right pattern for date in a mixed column: 2 digits/4 digits to extract the date
    df['last_service_date'] = df.last_service_date.str[0].str.extract(r'(\d{2}\/\d{4})')
    # converting to datetime object
    df['last_service_date'] = pd.to_datetime(df['last_service_date'], format='%m/%Y')
    
    #cleaning the available_from column and converting to datetime
    df['available_from'] = df.available_from.str.strip("\n")
    df['available_from'] = pd.to_datetime(df['available_from'])
        
    name_columns(df)
    
    drop_list=['entertainment_media', 'availability', 'body_color_original', 'full_service',
       'last_timing_belt_service_date', 'null', 'registration']
    df.drop(drop_list, axis=1, inplace=True)
        
    return df