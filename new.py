def ts_train_test_split(df):
    import pandas as pd
    """Separate time series data between train and test"""
    df_rows = df.shape
    df_list = []
    df_train = df.iloc[1:int(round(df_rows[0]*0.70,0)),:]
    df_test = df.iloc[int(round(df_rows[0]*0.70,0)):,:]
    df_list.append(df_train)
    df_list.append(df_test)
    return  df_list