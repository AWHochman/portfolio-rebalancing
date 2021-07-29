import pandas as pd

COMM = 'Communication'
UTIL = 'Utilities'
ENER = 'Energy'
RE = 'Real_Estate'
CONS = 'Cons_Staples'
HC = 'Healthcare'
FIN = 'Financials'
IND = 'Industrials'
MAT = 'Materials'
COND = 'Cons_Disc'
IT = 'Info_Tech'

Comm_df = pd.read_csv('./sectordata/Comm.csv')
ConsD_df = pd.read_csv('./sectordata/ConsD.csv')
ConsS_df = pd.read_csv('./sectordata/ConsS.csv')
Energy_df = pd.read_csv('./sectordata/Energy.csv')
Financials_df = pd.read_csv('./sectordata/Financials.csv')
Healthcare_df = pd.read_csv('./sectordata/Healthcare.csv')
Industrials_df = pd.read_csv('./sectordata/Industrials.csv')
IT_df = pd.read_csv('./sectordata/IT.csv')
Materials_df = pd.read_csv('./sectordata/Materials.csv')
RealEstate_df = pd.read_csv('./sectordata/RealEstate.csv')
Utilities_df = pd.read_csv('./sectordata/Utilities.csv')
SP500_df = pd.read_csv('./sectordata/SP500.csv')
Sectors_delta_df = pd.read_csv('./CDSData.csv')

SECTOR_TO_DF = {
    COMM: Comm_df,
    UTIL: Utilities_df,
    ENER: Energy_df,
    RE: RealEstate_df,
    CONS: ConsS_df,
    HC: Healthcare_df,
    FIN: Financials_df,
    IND: Industrials_df,
    MAT: Materials_df,
    COND: ConsD_df,
    IT: IT_df
}

"""
Returns the value 

Parameters:
    sector: string 
    day: (format: YYYY-MM-DD)

Returns: 
    int
"""
def get_sector_value(sector, day):
    df = SECTOR_TO_DF[sector]
    row = df.loc[df['Effective date '] == day]
    return float(row['value'])

def get_SP500_value(day):
    row = SP500_df.loc[SP500_df['Effective date '] == day]
    return float(row['value'])

def get_sectors_delta(start, end):
    df = Sectors_delta_df
    try: 
        s_idx = df.loc[df['Date'] == start].index[0]
        e_idx = df.loc[df['Date'] == end].index[0]
    except IndexError:
        return pd.DataFrame()
    return df[s_idx:e_idx]