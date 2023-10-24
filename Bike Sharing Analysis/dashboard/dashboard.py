import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title('Bike Sharing Analysis')
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Yearly", "Monthly 2011", "Monthly 2012", "Weather", "Hourly"])

def create_byyear_df(df):
    byyear_df = df.groupby(by='yr').agg({
        'casual': 'sum',
        'registered': 'sum',
    }).reset_index()
    byyear_df.rename(columns={
        "yr": "year",
    }, inplace=True)

    byyear_df['year'].replace(to_replace=0, value=2011, inplace=True)
    byyear_df['year'].replace(to_replace=1, value=2012, inplace=True)

    return byyear_df

def create_bymonth11_df(df):
    bymonth11_df = df.groupby(by='mnth').agg({
        'casual': 'sum',
        'registered': 'sum',
        'cnt': 'sum'
    }).reset_index()
    bymonth11_df.rename(columns={
        "mnth": "month",
        "cnt": "total_users"
    }, inplace=True)

    bymonth11_df['month'].replace(to_replace=1, value='Jan11', inplace=True)
    bymonth11_df['month'].replace(to_replace=2, value='Feb11', inplace=True)
    bymonth11_df['month'].replace(to_replace=3, value='Mar11', inplace=True)
    bymonth11_df['month'].replace(to_replace=4, value='Apr11', inplace=True)
    bymonth11_df['month'].replace(to_replace=5, value='May11', inplace=True)
    bymonth11_df['month'].replace(to_replace=6, value='Jun11', inplace=True)
    bymonth11_df['month'].replace(to_replace=7, value='Jul11', inplace=True)
    bymonth11_df['month'].replace(to_replace=8, value='Aug11', inplace=True)
    bymonth11_df['month'].replace(to_replace=9, value='Sep11', inplace=True)
    bymonth11_df['month'].replace(to_replace=10, value='Oct11', inplace=True)
    bymonth11_df['month'].replace(to_replace=11, value='Nov11', inplace=True)
    bymonth11_df['month'].replace(to_replace=12, value='Dec11', inplace=True)
    
    return bymonth11_df

def create_bymonth12_df(df):
    bymonth12_df = df.groupby(by='mnth').agg({
        'casual': 'sum',
        'registered': 'sum',
        'cnt': 'sum'
    }).reset_index()
    bymonth12_df.rename(columns={
        "mnth": "month",
        "cnt": "total_users"
    }, inplace=True)

    bymonth12_df['month'].replace(to_replace=1, value='Jan12', inplace=True)
    bymonth12_df['month'].replace(to_replace=2, value='Feb12', inplace=True)
    bymonth12_df['month'].replace(to_replace=3, value='Mar12', inplace=True)
    bymonth12_df['month'].replace(to_replace=4, value='Apr12', inplace=True)
    bymonth12_df['month'].replace(to_replace=5, value='May12', inplace=True)
    bymonth12_df['month'].replace(to_replace=6, value='Jun12', inplace=True)
    bymonth12_df['month'].replace(to_replace=7, value='Jul12', inplace=True)
    bymonth12_df['month'].replace(to_replace=8, value='Aug12', inplace=True)
    bymonth12_df['month'].replace(to_replace=9, value='Sep12', inplace=True)
    bymonth12_df['month'].replace(to_replace=10, value='Oct12', inplace=True)
    bymonth12_df['month'].replace(to_replace=11, value='Nov12', inplace=True)
    bymonth12_df['month'].replace(to_replace=12, value='Dec12', inplace=True)
    
    return bymonth12_df

def create_jan11_df(df):
    byday11_df = df.groupby(by=['mnth', 'weekday']).agg({
        'casual': 'sum',
        'registered': 'sum',
    })
    byday11_df.rename(columns={
        "mnth": "month",
        "weekday": "day"
    }, inplace=True)

    d = {
        'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 
        'casual': [byday11_df.casual.iloc[0], byday11_df.casual.iloc[1], byday11_df.casual.iloc[2], byday11_df.casual.iloc[3], byday11_df.casual.iloc[4], byday11_df.casual.iloc[5], byday11_df.casual.iloc[6]], 
        'registered': [byday11_df.registered.iloc[0], byday11_df.registered.iloc[1], byday11_df.registered.iloc[2], byday11_df.registered.iloc[3], byday11_df.registered.iloc[4], byday11_df.registered.iloc[5], byday11_df.registered.iloc[6]]
    }
    jan11_df = pd.DataFrame(d)
    return jan11_df

def create_feb11_df(df):
    byday11_df = df.groupby(by=['mnth', 'weekday']).agg({
        'casual': 'sum',
        'registered': 'sum',
    })
    byday11_df.rename(columns={
        "mnth": "month",
        "weekday": "day"
    }, inplace=True)

    d = {
        'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 
        'casual': [byday11_df.casual.iloc[7], byday11_df.casual.iloc[8], byday11_df.casual.iloc[9], byday11_df.casual.iloc[10], byday11_df.casual.iloc[11], byday11_df.casual.iloc[12], byday11_df.casual.iloc[13]], 
        'registered': [byday11_df.registered.iloc[7], byday11_df.registered.iloc[8], byday11_df.registered.iloc[9], byday11_df.registered.iloc[10], byday11_df.registered.iloc[11], byday11_df.registered.iloc[12], byday11_df.registered.iloc[13]]
    }
    feb11_df = pd.DataFrame(d)
    return feb11_df

def create_mar11_df(df):
    byday11_df = df.groupby(by=['mnth', 'weekday']).agg({
        'casual': 'sum',
        'registered': 'sum',
    })
    byday11_df.rename(columns={
        "mnth": "month",
        "weekday": "day"
    }, inplace=True)

    d = {
        'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 
        'casual': [byday11_df.casual.iloc[14], byday11_df.casual.iloc[15], byday11_df.casual.iloc[16], byday11_df.casual.iloc[17], byday11_df.casual.iloc[18], byday11_df.casual.iloc[19], byday11_df.casual.iloc[20]], 
        'registered': [byday11_df.registered.iloc[14], byday11_df.registered.iloc[15], byday11_df.registered.iloc[16], byday11_df.registered.iloc[17], byday11_df.registered.iloc[18], byday11_df.registered.iloc[19], byday11_df.registered.iloc[20]]
    }
    mar11_df = pd.DataFrame(d)
    return mar11_df

def create_apr11_df(df):
    byday11_df = df.groupby(by=['mnth', 'weekday']).agg({
        'casual': 'sum',
        'registered': 'sum',
    })
    byday11_df.rename(columns={
        "mnth": "month",
        "weekday": "day"
    }, inplace=True)

    d = {
        'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 
        'casual': [byday11_df.casual.iloc[21], byday11_df.casual.iloc[22], byday11_df.casual.iloc[23], byday11_df.casual.iloc[24], byday11_df.casual.iloc[25], byday11_df.casual.iloc[26], byday11_df.casual.iloc[27]], 
        'registered': [byday11_df.registered.iloc[21], byday11_df.registered.iloc[22], byday11_df.registered.iloc[23], byday11_df.registered.iloc[24], byday11_df.registered.iloc[25], byday11_df.registered.iloc[26], byday11_df.registered.iloc[27]]
    }
    apr11_df = pd.DataFrame(d)
    return apr11_df

def create_may11_df(df):
    byday11_df = df.groupby(by=['mnth', 'weekday']).agg({
        'casual': 'sum',
        'registered': 'sum',
    })
    byday11_df.rename(columns={
        "mnth": "month",
        "weekday": "day"
    }, inplace=True)

    d = {
        'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 
        'casual': [byday11_df.casual.iloc[28], byday11_df.casual.iloc[29], byday11_df.casual.iloc[30], byday11_df.casual.iloc[31], byday11_df.casual.iloc[32], byday11_df.casual.iloc[33], byday11_df.casual.iloc[34]], 
        'registered': [byday11_df.registered.iloc[28], byday11_df.registered.iloc[29], byday11_df.registered.iloc[30], byday11_df.registered.iloc[31], byday11_df.registered.iloc[32], byday11_df.registered.iloc[33], byday11_df.registered.iloc[34]]
    }
    may11_df = pd.DataFrame(d)
    return may11_df

def create_jun11_df(df):
    byday11_df = df.groupby(by=['mnth', 'weekday']).agg({
        'casual': 'sum',
        'registered': 'sum',
    })
    byday11_df.rename(columns={
        "mnth": "month",
        "weekday": "day"
    }, inplace=True)

    d = {
        'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 
        'casual': [byday11_df.casual.iloc[35], byday11_df.casual.iloc[36], byday11_df.casual.iloc[37], byday11_df.casual.iloc[38], byday11_df.casual.iloc[39], byday11_df.casual.iloc[40], byday11_df.casual.iloc[41]], 
        'registered': [byday11_df.registered.iloc[35], byday11_df.registered.iloc[36], byday11_df.registered.iloc[37], byday11_df.registered.iloc[38], byday11_df.registered.iloc[39], byday11_df.registered.iloc[40], byday11_df.registered.iloc[41]]
    }
    jun11_df = pd.DataFrame(d)
    return jun11_df

def create_jul11_df(df):
    byday11_df = df.groupby(by=['mnth', 'weekday']).agg({
        'casual': 'sum',
        'registered': 'sum',
    })
    byday11_df.rename(columns={
        "mnth": "month",
        "weekday": "day"
    }, inplace=True)

    d = {
        'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 
        'casual': [byday11_df.casual.iloc[42], byday11_df.casual.iloc[43], byday11_df.casual.iloc[44], byday11_df.casual.iloc[45], byday11_df.casual.iloc[46], byday11_df.casual.iloc[47], byday11_df.casual.iloc[48]], 
        'registered': [byday11_df.registered.iloc[42], byday11_df.registered.iloc[43], byday11_df.registered.iloc[44], byday11_df.registered.iloc[45], byday11_df.registered.iloc[46], byday11_df.registered.iloc[47], byday11_df.registered.iloc[48]]
    }
    jul11_df = pd.DataFrame(d)
    return jul11_df

def create_aug11_df(df):
    byday11_df = df.groupby(by=['mnth', 'weekday']).agg({
        'casual': 'sum',
        'registered': 'sum',
    })
    byday11_df.rename(columns={
        "mnth": "month",
        "weekday": "day"
    }, inplace=True)

    d = {
        'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 
        'casual': [byday11_df.casual.iloc[49], byday11_df.casual.iloc[50], byday11_df.casual.iloc[51], byday11_df.casual.iloc[52], byday11_df.casual.iloc[53], byday11_df.casual.iloc[54], byday11_df.casual.iloc[55]], 
        'registered': [byday11_df.registered.iloc[49], byday11_df.registered.iloc[50], byday11_df.registered.iloc[51], byday11_df.registered.iloc[52], byday11_df.registered.iloc[53], byday11_df.registered.iloc[54], byday11_df.registered.iloc[55]]
    }
    aug11_df = pd.DataFrame(d)
    return aug11_df

def create_sep11_df(df):
    byday11_df = df.groupby(by=['mnth', 'weekday']).agg({
        'casual': 'sum',
        'registered': 'sum',
    })
    byday11_df.rename(columns={
        "mnth": "month",
        "weekday": "day"
    }, inplace=True)

    d = {
        'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 
        'casual': [byday11_df.casual.iloc[56], byday11_df.casual.iloc[57], byday11_df.casual.iloc[58], byday11_df.casual.iloc[59], byday11_df.casual.iloc[60], byday11_df.casual.iloc[61], byday11_df.casual.iloc[62]], 
        'registered': [byday11_df.registered.iloc[56], byday11_df.registered.iloc[57], byday11_df.registered.iloc[58], byday11_df.registered.iloc[59], byday11_df.registered.iloc[60], byday11_df.registered.iloc[61], byday11_df.registered.iloc[62]]
    }
    sep11_df = pd.DataFrame(d)
    return sep11_df

def create_oct11_df(df):
    byday11_df = df.groupby(by=['mnth', 'weekday']).agg({
        'casual': 'sum',
        'registered': 'sum',
    })
    byday11_df.rename(columns={
        "mnth": "month",
        "weekday": "day"
    }, inplace=True)

    d = {
        'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 
        'casual': [byday11_df.casual.iloc[63], byday11_df.casual.iloc[64], byday11_df.casual.iloc[65], byday11_df.casual.iloc[66], byday11_df.casual.iloc[67], byday11_df.casual.iloc[68], byday11_df.casual.iloc[69]], 
        'registered': [byday11_df.registered.iloc[63], byday11_df.registered.iloc[64], byday11_df.registered.iloc[65], byday11_df.registered.iloc[66], byday11_df.registered.iloc[67], byday11_df.registered.iloc[68], byday11_df.registered.iloc[69]]
    }
    oct11_df = pd.DataFrame(d)
    return oct11_df

def create_nov11_df(df):
    byday11_df = df.groupby(by=['mnth', 'weekday']).agg({
        'casual': 'sum',
        'registered': 'sum',
    })
    byday11_df.rename(columns={
        "mnth": "month",
        "weekday": "day"
    }, inplace=True)

    d = {
        'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 
        'casual': [byday11_df.casual.iloc[70], byday11_df.casual.iloc[71], byday11_df.casual.iloc[72], byday11_df.casual.iloc[73], byday11_df.casual.iloc[74], byday11_df.casual.iloc[75], byday11_df.casual.iloc[76]], 
        'registered': [byday11_df.registered.iloc[70], byday11_df.registered.iloc[71], byday11_df.registered.iloc[72], byday11_df.registered.iloc[73], byday11_df.registered.iloc[74], byday11_df.registered.iloc[75], byday11_df.registered.iloc[76]]
    }
    nov11_df = pd.DataFrame(d)
    return nov11_df

def create_dec11_df(df):
    byday11_df = df.groupby(by=['mnth', 'weekday']).agg({
        'casual': 'sum',
        'registered': 'sum',
    })
    byday11_df.rename(columns={
        "mnth": "month",
        "weekday": "day"
    }, inplace=True)

    d = {
        'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 
        'casual': [byday11_df.casual.iloc[77], byday11_df.casual.iloc[78], byday11_df.casual.iloc[79], byday11_df.casual.iloc[80], byday11_df.casual.iloc[81], byday11_df.casual.iloc[82], byday11_df.casual.iloc[83]], 
        'registered': [byday11_df.registered.iloc[77], byday11_df.registered.iloc[78], byday11_df.registered.iloc[79], byday11_df.registered.iloc[80], byday11_df.registered.iloc[81], byday11_df.registered.iloc[82], byday11_df.registered.iloc[83]]
    }
    dec11_df = pd.DataFrame(d)
    return dec11_df

def create_jan12_df(df):
    byday12_df = df.groupby(by=['mnth', 'weekday']).agg({
        'casual': 'sum',
        'registered': 'sum',
    })
    byday12_df.rename(columns={
        "mnth": "month",
        "weekday": "day"
    }, inplace=True)

    d = {
        'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 
        'casual': [byday12_df.casual.iloc[0], byday12_df.casual.iloc[1], byday12_df.casual.iloc[2], byday12_df.casual.iloc[3], byday12_df.casual.iloc[4], byday12_df.casual.iloc[5], byday12_df.casual.iloc[6]], 
        'registered': [byday12_df.registered.iloc[0], byday12_df.registered.iloc[1], byday12_df.registered.iloc[2], byday12_df.registered.iloc[3], byday12_df.registered.iloc[4], byday12_df.registered.iloc[5], byday12_df.registered.iloc[6]]
}
    jan12_df = pd.DataFrame(d)
    return jan12_df

def create_feb12_df(df):
    byday12_df = df.groupby(by=['mnth', 'weekday']).agg({
        'casual': 'sum',
        'registered': 'sum',
    })
    byday12_df.rename(columns={
        "mnth": "month",
        "weekday": "day"
    }, inplace=True)

    d = {
        'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 
        'casual': [byday12_df.casual.iloc[7], byday12_df.casual.iloc[8], byday12_df.casual.iloc[9], byday12_df.casual.iloc[10], byday12_df.casual.iloc[11], byday12_df.casual.iloc[12], byday12_df.casual.iloc[13]], 
        'registered': [byday12_df.registered.iloc[7], byday12_df.registered.iloc[8], byday12_df.registered.iloc[9], byday12_df.registered.iloc[10], byday12_df.registered.iloc[11], byday12_df.registered.iloc[12], byday12_df.registered.iloc[13]]
    }
    feb12_df = pd.DataFrame(d)
    return feb12_df

def create_mar12_df(df):
    byday12_df = df.groupby(by=['mnth', 'weekday']).agg({
        'casual': 'sum',
        'registered': 'sum',
    })
    byday12_df.rename(columns={
        "mnth": "month",
        "weekday": "day"
    }, inplace=True)

    d = {
        'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 
        'casual': [byday12_df.casual.iloc[14], byday12_df.casual.iloc[15], byday12_df.casual.iloc[16], byday12_df.casual.iloc[17], byday12_df.casual.iloc[18], byday12_df.casual.iloc[19], byday12_df.casual.iloc[20]], 
        'registered': [byday12_df.registered.iloc[14], byday12_df.registered.iloc[15], byday12_df.registered.iloc[16], byday12_df.registered.iloc[17], byday12_df.registered.iloc[18], byday12_df.registered.iloc[19], byday12_df.registered.iloc[20]]
    }
    mar12_df = pd.DataFrame(d)
    return mar12_df

def create_apr12_df(df):
    byday12_df = df.groupby(by=['mnth', 'weekday']).agg({
        'casual': 'sum',
        'registered': 'sum',
    })
    byday12_df.rename(columns={
        "mnth": "month",
        "weekday": "day"
    }, inplace=True)

    d = {
        'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 
        'casual': [byday12_df.casual.iloc[21], byday12_df.casual.iloc[22], byday12_df.casual.iloc[23], byday12_df.casual.iloc[24], byday12_df.casual.iloc[25], byday12_df.casual.iloc[26], byday12_df.casual.iloc[27]], 
        'registered': [byday12_df.registered.iloc[21], byday12_df.registered.iloc[22], byday12_df.registered.iloc[23], byday12_df.registered.iloc[24], byday12_df.registered.iloc[25], byday12_df.registered.iloc[26], byday12_df.registered.iloc[27]]
    }
    apr12_df = pd.DataFrame(d)
    return apr12_df

def create_may12_df(df):
    byday12_df = df.groupby(by=['mnth', 'weekday']).agg({
        'casual': 'sum',
        'registered': 'sum',
    })
    byday12_df.rename(columns={
        "mnth": "month",
        "weekday": "day"
    }, inplace=True)

    d = {
        'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 
        'casual': [byday12_df.casual.iloc[28], byday12_df.casual.iloc[29], byday12_df.casual.iloc[30], byday12_df.casual.iloc[31], byday12_df.casual.iloc[32], byday12_df.casual.iloc[33], byday12_df.casual.iloc[34]], 
        'registered': [byday12_df.registered.iloc[28], byday12_df.registered.iloc[29], byday12_df.registered.iloc[30], byday12_df.registered.iloc[31], byday12_df.registered.iloc[32], byday12_df.registered.iloc[33], byday12_df.registered.iloc[34]]
    }
    may12_df = pd.DataFrame(d)
    return may12_df

def create_jun12_df(df):
    byday12_df = df.groupby(by=['mnth', 'weekday']).agg({
        'casual': 'sum',
        'registered': 'sum',
    })
    byday12_df.rename(columns={
        "mnth": "month",
        "weekday": "day"
    }, inplace=True)

    d = {
        'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 
        'casual': [byday12_df.casual.iloc[35], byday12_df.casual.iloc[36], byday12_df.casual.iloc[37], byday12_df.casual.iloc[38], byday12_df.casual.iloc[39], byday12_df.casual.iloc[40], byday12_df.casual.iloc[41]], 
        'registered': [byday12_df.registered.iloc[35], byday12_df.registered.iloc[36], byday12_df.registered.iloc[37], byday12_df.registered.iloc[38], byday12_df.registered.iloc[39], byday12_df.registered.iloc[40], byday12_df.registered.iloc[41]]
    }
    jun12_df = pd.DataFrame(d)
    return jun12_df

def create_jul12_df(df):
    byday12_df = df.groupby(by=['mnth', 'weekday']).agg({
        'casual': 'sum',
        'registered': 'sum',
    })
    byday12_df.rename(columns={
        "mnth": "month",
        "weekday": "day"
    }, inplace=True)

    d = {
        'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 
        'casual': [byday12_df.casual.iloc[42], byday12_df.casual.iloc[43], byday12_df.casual.iloc[44], byday12_df.casual.iloc[45], byday12_df.casual.iloc[46], byday12_df.casual.iloc[47], byday12_df.casual.iloc[48]], 
        'registered': [byday12_df.registered.iloc[42], byday12_df.registered.iloc[43], byday12_df.registered.iloc[44], byday12_df.registered.iloc[45], byday12_df.registered.iloc[46], byday12_df.registered.iloc[47], byday12_df.registered.iloc[48]]
    }
    jul12_df = pd.DataFrame(d)
    return jul12_df

def create_aug12_df(df):
    byday12_df = df.groupby(by=['mnth', 'weekday']).agg({
        'casual': 'sum',
        'registered': 'sum',
    })
    byday12_df.rename(columns={
        "mnth": "month",
        "weekday": "day"
    }, inplace=True)

    d = {
        'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 
        'casual': [byday12_df.casual.iloc[49], byday12_df.casual.iloc[50], byday12_df.casual.iloc[51], byday12_df.casual.iloc[52], byday12_df.casual.iloc[53], byday12_df.casual.iloc[54], byday12_df.casual.iloc[55]], 
        'registered': [byday12_df.registered.iloc[49], byday12_df.registered.iloc[50], byday12_df.registered.iloc[51], byday12_df.registered.iloc[52], byday12_df.registered.iloc[53], byday12_df.registered.iloc[54], byday12_df.registered.iloc[55]]
    }
    aug12_df = pd.DataFrame(d)
    return aug12_df

def create_sep12_df(df):
    byday12_df = df.groupby(by=['mnth', 'weekday']).agg({
        'casual': 'sum',
        'registered': 'sum',
    })
    byday12_df.rename(columns={
        "mnth": "month",
        "weekday": "day"
    }, inplace=True)

    d = {
        'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 
        'casual': [byday12_df.casual.iloc[56], byday12_df.casual.iloc[57], byday12_df.casual.iloc[58], byday12_df.casual.iloc[59], byday12_df.casual.iloc[60], byday12_df.casual.iloc[61], byday12_df.casual.iloc[62]], 
        'registered': [byday12_df.registered.iloc[56], byday12_df.registered.iloc[57], byday12_df.registered.iloc[58], byday12_df.registered.iloc[59], byday12_df.registered.iloc[60], byday12_df.registered.iloc[61], byday12_df.registered.iloc[62]]
    }
    sep12_df = pd.DataFrame(d)
    return sep12_df

def create_oct12_df(df):
    byday12_df = df.groupby(by=['mnth', 'weekday']).agg({
        'casual': 'sum',
        'registered': 'sum',
    })
    byday12_df.rename(columns={
        "mnth": "month",
        "weekday": "day"
    }, inplace=True)

    d = {
        'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 
        'casual': [byday12_df.casual.iloc[63], byday12_df.casual.iloc[64], byday12_df.casual.iloc[65], byday12_df.casual.iloc[66], byday12_df.casual.iloc[67], byday12_df.casual.iloc[68], byday12_df.casual.iloc[69]], 
        'registered': [byday12_df.registered.iloc[63], byday12_df.registered.iloc[64], byday12_df.registered.iloc[65], byday12_df.registered.iloc[66], byday12_df.registered.iloc[67], byday12_df.registered.iloc[68], byday12_df.registered.iloc[69]]
    }
    oct12_df = pd.DataFrame(d)
    return oct12_df

def create_nov12_df(df):
    byday12_df = df.groupby(by=['mnth', 'weekday']).agg({
        'casual': 'sum',
        'registered': 'sum',
    })
    byday12_df.rename(columns={
        "mnth": "month",
        "weekday": "day"
    }, inplace=True)

    d = {
        'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 
        'casual': [byday12_df.casual.iloc[70], byday12_df.casual.iloc[71], byday12_df.casual.iloc[72], byday12_df.casual.iloc[73], byday12_df.casual.iloc[74], byday12_df.casual.iloc[75], byday12_df.casual.iloc[76]], 
        'registered': [byday12_df.registered.iloc[70], byday12_df.registered.iloc[71], byday12_df.registered.iloc[72], byday12_df.registered.iloc[73], byday12_df.registered.iloc[74], byday12_df.registered.iloc[75], byday12_df.registered.iloc[76]]
    }
    nov12_df = pd.DataFrame(d)
    return nov12_df

def create_dec12_df(df):
    byday12_df = df.groupby(by=['mnth', 'weekday']).agg({
        'casual': 'sum',
        'registered': 'sum',
    })
    byday12_df.rename(columns={
        "mnth": "month",
        "weekday": "day"
    }, inplace=True)

    d = {
        'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 
        'casual': [byday12_df.casual.iloc[77], byday12_df.casual.iloc[78], byday12_df.casual.iloc[79], byday12_df.casual.iloc[80], byday12_df.casual.iloc[81], byday12_df.casual.iloc[82], byday12_df.casual.iloc[83]], 
        'registered': [byday12_df.registered.iloc[77], byday12_df.registered.iloc[78], byday12_df.registered.iloc[79], byday12_df.registered.iloc[80], byday12_df.registered.iloc[81], byday12_df.registered.iloc[82], byday12_df.registered.iloc[83]]
    }
    dec12_df = pd.DataFrame(d)
    return dec12_df

def create_season11_df(df):
    season11_df = df.groupby(by='season').agg({
        'casual': 'sum',
        'registered': 'sum',
    }).reset_index()

    season11_df['season'].replace(to_replace=1, value='Spring', inplace=True)
    season11_df['season'].replace(to_replace=2, value='Summer', inplace=True)
    season11_df['season'].replace(to_replace=3, value='Fall', inplace=True)
    season11_df['season'].replace(to_replace=4, value='Winter', inplace=True)

    return season11_df

def create_season12_df(df):
    season12_df = df.groupby(by='season').agg({
        'casual': 'sum',
        'registered': 'sum',
    }).reset_index()

    season12_df['season'].replace(to_replace=1, value='Spring', inplace=True)
    season12_df['season'].replace(to_replace=2, value='Summer', inplace=True)
    season12_df['season'].replace(to_replace=3, value='Fall', inplace=True)
    season12_df['season'].replace(to_replace=4, value='Winter', inplace=True)

    return season12_df

def create_temp_df(df):
    temp_df = df.groupby(by='temp_group').agg({
        'casual': 'sum',
        'registered': 'sum',
    }).reset_index()

    temp_df['temp_group'].replace(to_replace=1, value='Cold (0-12)', inplace=True)
    temp_df['temp_group'].replace(to_replace=2, value='Good (12-25)', inplace=True)
    temp_df['temp_group'].replace(to_replace=3, value='Warm (25-34)', inplace=True)
    temp_df['temp_group'].replace(to_replace=4, value='Hot (>34)', inplace=True)

    return temp_df

def create_atemp_df(df):
    atemp_df = df.groupby(by='atemp_group').agg({
        'casual': 'sum',
        'registered': 'sum',
    }).reset_index()

    atemp_df['atemp_group'].replace(to_replace='1', value='Cold (0-12)', inplace=True)
    atemp_df['atemp_group'].replace(to_replace='2', value='Good (12-25)', inplace=True)
    atemp_df['atemp_group'].replace(to_replace='3', value='Warm (25-34)', inplace=True)
    atemp_df['atemp_group'].replace(to_replace='4', value='Hot (>34)', inplace=True)

    return atemp_df

def create_weather_df(df):
    weather_df = df.groupby(by='weathersit').agg({
        'casual': 'sum',
        'registered': 'sum',
    }).reset_index()
    weather_df.loc[len(weather_df.index)] = [4, 0, 0]

    return weather_df

def create_byhour_df(df):
    byhour_df = df.groupby(by='hr_group').agg({
        'casual': 'sum',
        'registered': 'sum'
    }).reset_index()

    byhour_df['hr_group'].replace(to_replace=1, value='Midnight to Dawn', inplace=True)
    byhour_df['hr_group'].replace(to_replace=2, value='Dawn to Noon', inplace=True)
    byhour_df['hr_group'].replace(to_replace=3, value='Noon to Dusk', inplace=True)
    byhour_df['hr_group'].replace(to_replace=4, value='Dusk to Midnight', inplace=True)

    return byhour_df

def create_springhour_df(df):
    hour_season_df = df.groupby(by=['hr_group', 'season']).agg({
        'casual': 'sum',
        'registered': 'sum'
    })

    d = {
        'category': ['Midnight to Dawn', 'Dawn to Noon', 'Noon to Dusk', 'Dusk to Midnight'], 
        'casual': [hour_season_df.casual.iloc[0], hour_season_df.casual.iloc[1], hour_season_df.casual.iloc[2], hour_season_df.casual.iloc[3]], 
        'registered': [hour_season_df.registered.iloc[0], hour_season_df.registered.iloc[1], hour_season_df.registered.iloc[2], hour_season_df.registered.iloc[3]]
    }
    springhour_df = pd.DataFrame(d)
    return springhour_df

def create_summerhour_df(df):
    hour_season_df = df.groupby(by=['hr_group', 'season']).agg({
        'casual': 'sum',
        'registered': 'sum'
    })

    d = {
        'category': ['Midnight to Dawn', 'Dawn to Noon', 'Noon to Dusk', 'Dusk to Midnight'], 
        'casual': [hour_season_df.casual.iloc[4], hour_season_df.casual.iloc[5], hour_season_df.casual.iloc[6], hour_season_df.casual.iloc[7]], 
        'registered': [hour_season_df.registered.iloc[4], hour_season_df.registered.iloc[5], hour_season_df.registered.iloc[6], hour_season_df.registered.iloc[7]]
    }
    summerhour_df = pd.DataFrame(d)
    return summerhour_df

def create_fallhour_df(df):
    hour_season_df = df.groupby(by=['hr_group', 'season']).agg({
        'casual': 'sum',
        'registered': 'sum'
    })

    d = {
        'category': ['Midnight to Dawn', 'Dawn to Noon', 'Noon to Dusk', 'Dusk to Midnight'], 
        'casual': [hour_season_df.casual.iloc[8], hour_season_df.casual.iloc[9], hour_season_df.casual.iloc[10], hour_season_df.casual.iloc[11]], 
        'registered': [hour_season_df.registered.iloc[8], hour_season_df.registered.iloc[9], hour_season_df.registered.iloc[10], hour_season_df.registered.iloc[11]]
    }
    fallhour_df = pd.DataFrame(d)
    return fallhour_df

def create_winterhour_df(df):
    hour_season_df = df.groupby(by=['hr_group', 'season']).agg({
        'casual': 'sum',
        'registered': 'sum'
    })

    d = {
        'category': ['Midnight to Dawn', 'Dawn to Noon', 'Noon to Dusk', 'Dusk to Midnight'], 
        'casual': [hour_season_df.casual.iloc[12], hour_season_df.casual.iloc[13], hour_season_df.casual.iloc[14], hour_season_df.casual.iloc[15]], 
        'registered': [hour_season_df.registered.iloc[12], hour_season_df.registered.iloc[13], hour_season_df.registered.iloc[14], hour_season_df.registered.iloc[15]]
    }
    winterhour_df = pd.DataFrame(d)
    return winterhour_df

day_df = pd.read_csv("day.csv")
day_2011_df = pd.read_csv("day_2011.csv")
day_2012_df = pd.read_csv("day_2012.csv")
day_updated_df = pd.read_csv("day_updated.csv")
hour_df = pd.read_csv("hour_updated.csv")

byyear_df = create_byyear_df(day_df)
bymonth11_df = create_bymonth11_df(day_2011_df)
bymonth12_df = create_bymonth12_df(day_2012_df)
jan11_df = create_jan11_df(day_2011_df)
feb11_df = create_feb11_df(day_2011_df)
mar11_df = create_mar11_df(day_2011_df)
apr11_df = create_apr11_df(day_2011_df)
may11_df = create_may11_df(day_2011_df)
jun11_df = create_jun11_df(day_2011_df)
jul11_df = create_jul11_df(day_2011_df)
aug11_df = create_aug11_df(day_2011_df)
sep11_df = create_sep11_df(day_2011_df)
oct11_df = create_oct11_df(day_2011_df)
nov11_df = create_nov11_df(day_2011_df)
dec11_df = create_dec11_df(day_2011_df)
jan12_df = create_jan11_df(day_2012_df)
feb12_df = create_feb11_df(day_2012_df)
mar12_df = create_mar11_df(day_2012_df)
apr12_df = create_apr11_df(day_2012_df)
may12_df = create_may11_df(day_2012_df)
jun12_df = create_jun11_df(day_2012_df)
jul12_df = create_jul11_df(day_2012_df)
aug12_df = create_aug11_df(day_2012_df)
sep12_df = create_sep11_df(day_2012_df)
oct12_df = create_oct11_df(day_2012_df)
nov12_df = create_nov11_df(day_2012_df)
dec12_df = create_dec11_df(day_2012_df)
season11_df = create_season11_df(day_2011_df)
season12_df = create_season12_df(day_2012_df)
temp_df = create_temp_df(day_updated_df)
atemp_df = create_atemp_df(day_updated_df)
weather_df = create_weather_df(day_updated_df)
byhour_df = create_byhour_df(hour_df)
springhour_df = create_springhour_df(hour_df)
summerhour_df = create_summerhour_df(hour_df)
fallhour_df = create_fallhour_df(hour_df)
winterhour_df = create_winterhour_df(hour_df)

with tab1:
    st.header("Bike Sharing Users per User Categories")

    fig, ax = plt.subplots(figsize=(16,8))
    byyear_df.plot(x='year', kind='bar', stacked=False, rot=0, ax=ax)

    st.pyplot(fig)
    st.caption('Casual: Count on casual users (unregistered)')
    st.caption('Registered: Count on registered users')

with tab2:
    st.header("Bike Sharing Users per Months in 2011")

    st.subheader("Casual and Registered Users")
    fig, ax = plt.subplots(figsize=(16,8))
    ax.plot(
        bymonth11_df["month"],
        bymonth11_df["casual"],
        marker='o', 
        linewidth=2,
        color="#3647EB"
    )
    ax.plot(
        bymonth11_df["month"],
        bymonth11_df["registered"],
        marker='o', 
        linewidth=2,
        color="#F21B1B"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    ax.legend(['Casual Users', 'Registered Users'])
    st.pyplot(fig)

    st.subheader("Total Users")
    fig, ax = plt.subplots(figsize=(16,8))
    ax.plot(
        bymonth11_df["month"],
        bymonth11_df["total_users"],
        marker='o', 
        linewidth=2,
        color="#00C87F"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    st.pyplot(fig)        

    st.header("Bike Sharing Users per Days in a Month (2011)")

    st.subheader("January 2011")
    fig, ax = plt.subplots(figsize=(16,8))
    jan11_df.plot(x='day', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)

    st.subheader("February 2011")
    fig, ax = plt.subplots(figsize=(16,8))
    feb11_df.plot(x='day', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)

    st.subheader("March 2011")
    fig, ax = plt.subplots(figsize=(16,8))
    mar11_df.plot(x='day', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)    

    st.subheader("April 2011")
    fig, ax = plt.subplots(figsize=(16,8))
    apr11_df.plot(x='day', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)

    st.subheader("May 2011")
    fig, ax = plt.subplots(figsize=(16,8))
    may11_df.plot(x='day', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)

    st.subheader("June 2011")
    fig, ax = plt.subplots(figsize=(16,8))
    jun11_df.plot(x='day', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)  

    st.subheader("July 2011")
    fig, ax = plt.subplots(figsize=(16,8))
    jul11_df.plot(x='day', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)

    st.subheader("August 2011")
    fig, ax = plt.subplots(figsize=(16,8))
    aug11_df.plot(x='day', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)

    st.subheader("September 2011")
    fig, ax = plt.subplots(figsize=(16,8))
    sep11_df.plot(x='day', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)

    st.subheader("October 2011")
    fig, ax = plt.subplots(figsize=(16,8))
    oct11_df.plot(x='day', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)

    st.subheader("November 2011")
    fig, ax = plt.subplots(figsize=(16,8))
    nov11_df.plot(x='day', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)

    st.subheader("December 2011")
    fig, ax = plt.subplots(figsize=(16,8))
    dec11_df.plot(x='day', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)

with tab3:
    st.header("Bike Sharing Users per Months in 2012")

    st.subheader("Casual and Registered Users")
    fig, ax = plt.subplots(figsize=(16,8))
    ax.plot(
        bymonth12_df["month"],
        bymonth12_df["casual"],
        marker='o',
        linewidth=2,
        color="#3647EB"
    )
    ax.plot(
        bymonth12_df["month"],
        bymonth12_df["registered"],
        marker='o',
        linewidth=2,
        color="#F21B1B"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    ax.legend(['Casual Users', 'Registered Users'])
    st.pyplot(fig)

    st.subheader("Total Users")
    fig, ax = plt.subplots(figsize=(16,8))
    ax.plot(
        bymonth12_df["month"],
        bymonth12_df["total_users"],
        marker='o',
        linewidth=2,
        color="#00C87F"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    st.pyplot(fig)

    st.header("Bike Sharing Users per Days in a Month (2012)")

    st.subheader("January 2012")
    fig, ax = plt.subplots(figsize=(16,8))
    jan12_df.plot(x='day', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)

    st.subheader("February 2012")
    fig, ax = plt.subplots(figsize=(16,8))
    feb12_df.plot(x='day', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)

    st.subheader("March 2012")
    fig, ax = plt.subplots(figsize=(16,8))
    mar12_df.plot(x='day', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)    

    st.subheader("April 2012")
    fig, ax = plt.subplots(figsize=(16,8))
    apr12_df.plot(x='day', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)

    st.subheader("May 2012")
    fig, ax = plt.subplots(figsize=(16,8))
    may12_df.plot(x='day', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)

    st.subheader("June 2012")
    fig, ax = plt.subplots(figsize=(16,8))
    jun12_df.plot(x='day', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)  

    st.subheader("July 2012")
    fig, ax = plt.subplots(figsize=(16,8))
    jul12_df.plot(x='day', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)

    st.subheader("August 2012")
    fig, ax = plt.subplots(figsize=(16,8))
    aug12_df.plot(x='day', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)

    st.subheader("September 2012")
    fig, ax = plt.subplots(figsize=(16,8))
    sep12_df.plot(x='day', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)

    st.subheader("October 2012")
    fig, ax = plt.subplots(figsize=(16,8))
    oct12_df.plot(x='day', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)

    st.subheader("November 2012")
    fig, ax = plt.subplots(figsize=(16,8))
    nov12_df.plot(x='day', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)

    st.subheader("December 2012")
    fig, ax = plt.subplots(figsize=(16,8))
    dec12_df.plot(x='day', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)

with tab4:
    st.header("Bike Sharing Users based on Season")

    st.subheader("Year 2011")
    fig, ax = plt.subplots(figsize=(16,8))
    season11_df.plot(x='season', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)

    st.subheader("Year 2012")
    fig, ax = plt.subplots(figsize=(16,8))
    season12_df.plot(x='season', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)

    st.header("Bike Sharing Users based on Temperature")

    st.subheader("Real Temperature")
    fig, ax = plt.subplots(figsize=(16,8))
    temp_df.plot(x='temp_group', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)
    with st.expander("Temperature category explanation"):
        st.write(
            """
            Cold: 0-12 Celcius Degree\n
            Good: 12-25 Celcius Degree\n
            Warm: 25-34 Celcius Degree\n
            Hot: >34 Celcius Degree
            """
        )
    
    st.subheader("Felt Temperature")
    fig, ax = plt.subplots(figsize=(16,8))
    atemp_df.plot(x='atemp_group', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)
    with st.expander("Temperature category explanation"):
        st.write(
            """
            Cold: 0-12 Celcius Degree\n
            Good: 12-25 Celcius Degree\n
            Warm: 25-34 Celcius Degree\n
            Hot: >34 Celcius Degree
            """
        )
    
    st.subheader("Weather Situation")
    fig, ax = plt.subplots(figsize=(16,8))
    weather_df.plot(x='weathersit', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)
    with st.expander("Weather situation category explanation"):
        st.write(
            """
            1: Clear, Few clouds, Partly cloudy, Partly cloudy\n
            2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist\n
            3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds\n
            4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
            """
        )

with tab5:
    st.header("Bike Sharing Users based on Hour Time")

    st.subheader("All Seasons")
    fig, ax = plt.subplots(figsize=(16,8))
    byhour_df.plot(x='hr_group', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)
    with st.expander("Time category explanation"):
        st.write(
            """
            Midnight to Dawn: 00:00 until 06:00\n
            Dawn to Noon: 06:00 until 12:00\n
            Noon to Dusk: 12:00 until 18:00\n
            Dusk to Midnight: 18:00 until 00:00
            """
        )
    
    st.subheader("Spring Season")
    fig, ax = plt.subplots(figsize=(16,8))
    springhour_df.plot(x='category', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)
    with st.expander("Time category explanation"):
        st.write(
            """
            Midnight to Dawn: 00:00 until 06:00\n
            Dawn to Noon: 06:00 until 12:00\n
            Noon to Dusk: 12:00 until 18:00\n
            Dusk to Midnight: 18:00 until 00:00
            """
        )
    
    st.subheader("Summer Season")
    fig, ax = plt.subplots(figsize=(16,8))
    summerhour_df.plot(x='category', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)
    with st.expander("Time category explanation"):
        st.write(
            """
            Midnight to Dawn: 00:00 until 06:00\n
            Dawn to Noon: 06:00 until 12:00\n
            Noon to Dusk: 12:00 until 18:00\n
            Dusk to Midnight: 18:00 until 00:00
            """
        )
    
    st.subheader("Fall Season")
    fig, ax = plt.subplots(figsize=(16,8))
    fallhour_df.plot(x='category', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)
    with st.expander("Time category explanation"):
        st.write(
            """
            Midnight to Dawn: 00:00 until 06:00\n
            Dawn to Noon: 06:00 until 12:00\n
            Noon to Dusk: 12:00 until 18:00\n
            Dusk to Midnight: 18:00 until 00:00
            """
        )
    
    st.subheader("Winter Season")
    fig, ax = plt.subplots(figsize=(16,8))
    winterhour_df.plot(x='category', kind='bar', stacked=False, rot=0, ax=ax)
    st.pyplot(fig)
    with st.expander("Time category explanation"):
        st.write(
            """
            Midnight to Dawn: 00:00 until 06:00\n
            Dawn to Noon: 06:00 until 12:00\n
            Noon to Dusk: 12:00 until 18:00\n
            Dusk to Midnight: 18:00 until 00:00
            """
        )