def clean_t (data):
    
    # Select columns to clean
    df = data
    
    # Create dummies using the items in the list of 'safety&security' column
    ss = df['safety_security'].dropna()
    df_new = df.join(ss.str.join('|').str.get_dummies().add_prefix('ss_'))
    # Drop 'safety_security' column
    df_new.drop('safety_security', axis=1, inplace=True)
    
    # Clean the model column
    df_new['model'] = df.model.apply(lambda x: x[1])
    
    # Strip "\n"s from the 'make' column
    df_new['make'] = df.make.str.strip("\n")
    
    # Drop unnecesary column 'make_model'
    df_new.drop(columns = "make_model", inplace = True)
    
    # Clean 'model_code' column
    df_new.loc[df_new.model_code.notnull(), "model_code"] = df.model_code[df.model_code.notnull()].apply(lambda x: str(x)[4:-4])
    
    # Clean 'country_version' column
    df_new.loc[df_new.country_version.notnull(), "country_version"] = df.country_version[df.country_version.notnull()].apply(lambda x: str(x)[4:-4])
    
    # Clean 'co2_emission' column
    df_new['co2_emission'] = df.co2_emission.str[0].str.extract(r'(\d+)')
    # Change the 'co2' columns data type to numeric
    df_new['co2_emission'] = pd.to_numeric(df_new.co2_emission)
    
    # Clean 'cylinders' column
    df_new['cylinders'] = df.cylinders.str[0].str.extract(r'(\d+)')
    # Change the 'cylinders' columns data type to numeric
    df_new['cylinders'] = pd.to_numeric(df_new['cylinders'])
    
    # Extract displacement values (and remove commas)
    df_new['displacement'] = df.displacement.str[0].str.replace(",","").str.extract(r'(\d+)')
    # Change the type of displacement from object to numeric
    df_new['displacement'] = pd.to_numeric(df_new['displacement'])

    # Extract 'next_inspection' values
    df_new.next_inspection = df.next_inspection.str[0].str.strip("\n")
    # Create a boolean column from `next_inspection`
    df_new['next_inspection_bool'] = df_new.next_inspection.notnull()
    
    # Drop 'non-smoking_vehicle' column
    df_new.drop("non_smoking_vehicle", axis=1, inplace=True)
    
    # Extract hp from 'hp' column
    df_new['hp'] = df.hp.str.extract(r'(\d+)')
    # Change datatype to numeric
    df_new['hp'] = pd.to_numeric(df_new['hp'])
    
    # Drop 'kw' column
    df_new.drop('kw', axis=1, inplace=True)
    
    # Clean 'km' column
    df_new['km'] = df.km.str.replace(",", "").str.extract(r'(\d+)')
    
    
    # Clean "offer_number' column
    df_new['offer_number'] = df.offer_number.str[0].str.replace("\n","")
    
    # Create a boolean for checking "combined" consumption
    comb_bool = df.consumption.str[0].str[0].str.contains("comb", na=False)
    # Create a new column for 'consumption_comb'
    df_new['consumption_comb'] = df[comb_bool].consumption.str[0].str[0].str.extract(r'(\d.\d|\d)')
    # Drop 'consumption' column
    df_new.drop('consumption', axis=1, inplace=True)
    
    # Tidy column names
    df_new.columns = name_columns(df_new)
    
    # Change description from list to string
    df_new['description'] = df['description'].str.join('').str.strip("\n")[0]
    
    return df_new

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


def clean_update(data):
    '''Additional cleaning after performing EDA'''

    df = data
    
    # Change wrong data types to numeric
    df['km'] = pd.to_numeric(df['km'])
    df['consumption_comb'] = pd.to_numeric(df['consumption_comb'])
    df['nr_of_doors'] = pd.to_numeric(df['nr_of_doors'])
    df['nr_of_seats'] = pd.to_numeric(df['nr_of_seats'])
    df['previous_owners'] = pd.to_numeric(df['previous_owners'])
    df['weight_kg'] = pd.to_numeric(df['weight_kg'])
    #df['gears'] = pd.to_numeric(df['gears']) # clean_m updated

    # Change wrong data type to date_time
    df['first_registration'] = pd.to_datetime(df.first_registration, format='%Y')

    # Replace " " with NaNs
    df.loc[df.next_inspection == "",'next_inspection'] = np.nan

    # Drop 'prev_owner' column
    df.drop('prev_owner', axis=1, inplace = True)
    
    # Drop 'body_type' column (duplicate of 'body')
    df.drop('body_type', axis=1, inplace = True)
    
    # Drop 'next_inspection' column (created a new column 'next_inspection_bool')
    df.drop('next_inspection', axis=1, inplace = True)
    
    return df