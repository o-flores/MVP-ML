import pandas as pd

# Transform into categories
active_modes = ['Walking', 'Bike']
obesity = ['Overweight_Level_I', 'Obesity_Type_I', 'Overweight_Level_II',  'Obesity_Type_II', 'Obesity_Type_III']

# Mapping binary categorical variables
binary_map = {'yes': 1, 'no': 0}
gender_map = {'Male': 1, 'Female': 0}

def transform_dataset(df: pd.DataFrame):
  df.dropna(inplace=True)

  df['family_history_with_overweight'] = df['family_history_with_overweight'].map(binary_map)
  df['FAVC'] = df['FAVC'].map(binary_map)
  df['SMOKE'] = df['SMOKE'].map(binary_map)
  df['SCC'] = df['SCC'].map(binary_map)
  df['Gender'] = df['Gender'].map(gender_map)
  df['CALC'] = df['CALC'].apply(lambda x: 0 if x == 'no' else 1)
  df['CAEC'] = df['CAEC'].apply(lambda x: 0 if x == 'no' else 1)
  df['MTRANS_active'] = df['MTRANS'].isin(active_modes).astype(int)
  df['IS_OBESE'] = df['NObeyesdad'].isin(obesity).astype(int)

  df = df.drop(columns=['MTRANS', 'NObeyesdad', 'Weight'], axis=1)
  return df