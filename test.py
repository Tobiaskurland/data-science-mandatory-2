def convert_string_to_int(df, input_list, output_value):
    
    X = df[input_list]
    conditions = []
    choices = []
    
    for i in input_list:
        column_value = df[i].unique()
        condition = []

        for cv in range(len(column_value)):
            condition.append(
            (X[i]==column_value[cv]))
        print()
