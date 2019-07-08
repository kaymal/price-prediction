#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def clean_v(data):
    
    df_v=data
    
    # Standardisation of column names
    df_v.columns = [x.casefold().strip().replace(" ","_").replace("_&_","_").replace(".","").replace("-", "_") for x in df_v.columns]
    
    # Create dummies using the items in the list of 'safety&security' column
    co_co = df_v[['comfort_convenience']].dropna()
    df_v = df_v.join(co_co['comfort_convenience'].str.join('|').str.get_dummies().add_prefix('cc_'))
    
    # Create dummies using the items in the list of 'safety&security' column
    ext = df_v[['extras']].dropna()
    df_v = df_v.join(ext['extras'].str.join('|').str.get_dummies().add_prefix('ext_'))

    #cleaning and reassigning "drive_chain" column
    chain = df_v.drive_chain
    chain_str = [item[0].strip() if type(item) == list else item for item in chain]
    df_v.drive_chain = pd.DataFrame(chain_str)
    
    #cleaning and reassigning "electricity_consumption" column
    electricity = [item[0].strip()[0] if type(item) == list else item for item in df_v.electricity_consumption]
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

