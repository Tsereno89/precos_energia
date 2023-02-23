#Arquivo alterado no github
#Alterado no vscode

def prep_df(file):

    """Takes a dataframe with n columns (regions) and separates them into n dataframes containing 2 columns, 1 for timestamp and another with the region label and eletricity prices"""
    import pandas as pd 
    container = []
    regions= list(file.columns)[1:]
    regions_df = []
    for region in regions:
        regions_df.append('DF'+ '_' + str(region))
        for place in regions_df:
            place = file.loc[:,['DATA_INICIO', region]]
            container.append(place)

    return container





def read_clean(file_path, drop_columns, axis):
    import pandas as pd

    df = pd.read_csv(file_path, sep=';')

    df.drop(drop_columns, axis=1, inplace=True)

    return df

