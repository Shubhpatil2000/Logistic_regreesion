def binary_cleanup(data):
    data = data.copy()
    data["Gender"] = data["Gender"].map( {'Male': 1, 'Female': 0} )
    data["OverTime"] = data["OverTime"].map( {'Yes': 1, 'No': 0} )
    drop_cols = ["EmployeeCount", "StandardHours", "Over18", "EmployeeNumber"]
    return data.drop(columns=drop_cols)