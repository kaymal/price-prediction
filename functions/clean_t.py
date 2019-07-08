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