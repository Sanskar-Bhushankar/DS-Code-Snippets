def analyze_dataset(file_path):
    # Load the dataset based on file type
    if isinstance(file_path, pd.DataFrame):
        df = file_path
    elif file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Please use CSV or Excel files.")
    
    # Initialize an empty list to hold the summary data
    summary = []

    for col in df.columns:
        col_data = df[col]
        
        if pd.api.types.is_numeric_dtype(col_data):
            col_type = 'Numeric'
        elif pd.api.types.is_datetime64_any_dtype(col_data):
            col_type = 'Datetime'
        elif pd.api.types.is_bool_dtype(col_data):
            col_type = 'Boolean'
        elif pd.api.types.is_object_dtype(col_data):
            # Check if column contains mixed data types
            unique_types = set(col_data.apply(lambda x: type(x)).unique())
            if len(unique_types) > 1:
                # Fixing the issue with backslash in f-string
                col_type = f'Mixed: {", ".join([str(t).split(".")[1] for t in unique_types])}'
            else:
                col_type = 'String'
        else:
            col_type = 'Other'

        # Get the number of unique values, missing values, and total values
        unique_values = col_data.nunique()
        missing_values = col_data.isnull().sum()
        total_values = len(col_data)

        # Append the column summary to the list
        summary.append({
            'Column Name': col,
            'Data Type': col_type,
            'Unique Values': unique_values,
            'Missing Values': missing_values,
            'Total Values': total_values,
            'Percentage Missing': (missing_values / total_values) * 100
        })

    # Return the summary as a DataFrame
    return pd.DataFrame(summary)

summary_output = analyze_dataset(data)
print(summary_output)
