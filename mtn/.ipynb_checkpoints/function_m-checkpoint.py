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
    
    # Replace "\n" with ""
    data.columns = data.columns.str.replace("\n", "")
    
    return data.columns

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
       'last_timing_belt_service_date', 'null', 'registration', 'short_description', 'gears',
       'paint_type', 'inspection_new', 'available_after_days', 'last_service_date', 
       'available_from', 'vat']
    df.drop(drop_list, axis=1, inplace=True)
        
    return df

def clean_v(data):
    
    df_v=data
    
    # Standardisation of column names
    df_v.columns = [x.casefold().strip().replace(" ","_").replace("_&_","_").replace(".","").replace("-", "_") for x in df_v.columns]
    
    # Create dummies using the items in the list of 'safety&security' column
    df_v = df_v.join(df_v['comfort_convenience'].str.join('|').str.get_dummies().add_prefix('cc_'))

    # Create dummies using the items in the list of 'safety&security' column
    df_v = df_v.join(df_v['extras'].str.join('|').str.get_dummies().add_prefix('ext_'))

    #cleaning and reassigning "drive_chain" column
    chain = df_v.drive_chain
    chain_str = [item[0].strip() if type(item) == list else item for item in chain]
    df_v.drive_chain = pd.DataFrame(chain_str)
    
    #cleaning and reassigning "electricity_consumption" column
    electricity = [item[0].strip() if type(item) == list else item for item in df_v.electricity_consumption]
    df_v.electricity_consumption = pd.DataFrame(electricity)
    #cleaning and reassigning "emission_class" column 1/3
    emis = df_v['emission_class']
    #cleaning and reassigning "emission_class" column 2/3
    emis_list = []
    for item in emis:
        if type(item) == list:
            if len(item[0]) >= 1:
                emis_list.append(item[0].strip())
            else:
                emis_list.append(np.nan)
        else:
            emis_list.append(np.nan)
    #cleaning and reassigning "emission_class" column 3/3
    df_v.emission_class = pd.DataFrame(emis_list)
    #cleaning and reassigning "emission_label" column 1/3
    emlabel = df_v.emission_label
    #cleaning and reassigning "emission_label" column 2/3
    emlabel_list = []
    for item in emlabel:
        if type(item) == list:
            if len(item[0]) >= 1:
                emlabel_list.append(item[0].strip())
            else:
                emlabel_list.append(np.nan)
        else:
            emlabel_list.append(np.nan)
    #cleaning and reassigning "emission_label" column 3/3
    df_v.emission_label = pd.DataFrame(emlabel_list)
    #cleaning and reassigning "first_registration" column 1/3
    freg = df_v.first_registration
    #cleaning and reassigning "first_registration" column 2/3
    freg_list = ["".join(item).strip() if type(item) == list else item for item in freg]
    df_v.first_registration = pd.DataFrame(freg_list)
    
    #cleaning and reassigning "fuel" column 1/3
    fuel = df_v.fuel
    fuel_list = ["".join(item).strip() if type(item) == list else item for item in fuel]
    df_v.fuel = pd.DataFrame(fuel_list)
    
    #cleaning and reassigning "nr_of_doors" column 1/3
    doors = df_v.nr_of_doors
    doors_list = [item[0].strip() if type(item) == list else item for item in doors]
    df_v.nr_of_doors = pd.DataFrame(doors_list)
    
    #cleaning and reassigning "nr_of_seats" column 1/3
    seats = df_v.nr_of_seats
    seats_list = [item[0].strip() if type(item) == list else item for item in seats]
    df_v.nr_of_seats = pd.DataFrame(seats_list)
    
    #cleaning and reassigning "previous_owners" column 1/3
    pre_own = df_v.previous_owners
    pre_list = [item[0].strip() if type(item) == list else item.strip() if type(item) == str else item for item in pre_own]
    df_v.previous_owners = pd.DataFrame(pre_list)
    
    #cleaning and reassigning "type" column 1/3
    types = df_v.type
    types_list = [item[1].strip() if type(item) == list else item for item in types]
    df_v.type = pd.DataFrame(types_list)
    
    #cleaning and reassigning "upholstery" column 1/3
    uph = df_v.upholstery
    uph_list = ["_".join(item).strip() if type(item) == list else item for item in uph]
    df_v.upholstery = pd.DataFrame(uph_list)
    
    #cleaning and reassigning "warranty" column 1/3
    #regarding the design of the website we need to handle this column a bit special.
    #if there is a value in the row that means there is a warranty if NaN it means no warranty.
    # so we will use "0" for missing values and "1" for the others 
    war = df_v.warranty
    war_list = [0 if type(item) == float else 1 for item in war]
    df_v.warranty = pd.DataFrame(war_list)
    
    #cleaning and reassigning "weight" column 1/3
    wei = df_v.weight
    wei_list = [item[0].replace(",","").strip().rstrip(" gk") if type(item) == list else item for item in wei]
    
    #cleaning and reassigning "weight" column 3/3
    #removing also "kg" string and changing column name as "weight_kg"
    #so we can drop "weight" column also
    df_v["weight_kg"] = pd.DataFrame(wei_list)
    
    #cleaning and reassigning "prev_owner" column 1/3
    powner = df_v.prev_owner
    powner_list = [item.split()[0] if type(item) == str else item for item in powner]
    df_v.prev_owner = pd.DataFrame(powner_list)
    columns_to_drop = [ "electricity_consumption", "other_fuel_types", "weight", "comfort_convenience", "extras", ]
    
    # Drop unnecesary columns
    df_v.drop(columns_to_drop, axis=1, inplace=True)
 
    # Standardisation of column names
    df_v.columns = [x.casefold().strip().replace(" ","_").replace("_&_","_").replace(".","").replace("-", "_") for x in     df_v.columns]
    
    return df_v

def clean_t (data):
    
    # Select columns to clean
    df = data
    
    # Create dummies using the items in the list of 'safety&security' column
    df_new = df.join(df['safety_security'].str.join('|').str.get_dummies().add_prefix('ss_'))
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
    
    # Tidy column names
    df_new.columns = name_columns(df_new)
    
    # Change description from list to string
    df_new['description'] = df['description'].str.join('').str.strip("\n")[0]
    
    return df_new