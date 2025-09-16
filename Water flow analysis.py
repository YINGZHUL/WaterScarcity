#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Q: all exceedence mean flow in csv
import pandas as pd
import numpy as np

nodelinks_data = pd.read_csv('nodelinks.csv')
flow_data = pd.read_csv('FlowAtStreamNodes_cms.txt', header=None, delim_whitespace=True)
date_data = pd.read_csv('DateTime_yyyymmdd_hhmmss.txt', header=None, delim_whitespace=True, dtype=str, skiprows=1)
drain_mapping = pd.read_csv('DrainID.csv')  # Load the drain mapping file

def parse_yyyymmdd_to_datetime(yyyymmdd):
    """Converts yyyymmdd string format to a Python datetime object."""
    return pd.to_datetime(yyyymmdd, format='%Y%m%d')

def average_exceedence_to_data(pnode, ystart, yend, drain_name, LNname):
    nlNodeId = nodelinks_data['0'].tolist()
    DownNodeId = nodelinks_data['1'].tolist()
    nlDrainId = nodelinks_data['2'].tolist()
    ProjNodeId = nodelinks_data['3'].tolist()
    
    nfdn = date_data[1].apply(parse_yyyymmdd_to_datetime)
    d_start = pd.Timestamp(f"{ystart}-10-01")
    d_end = pd.Timestamp(f"{yend}-09-30")
    idx = (nfdn >= d_start) & (nfdn <= d_end)
    
    print(d_start)
    
    node_index = np.where(np.array(ProjNodeId) == str(pnode))[0][0]
    node = nlNodeId[node_index]
    drain = nlDrainId[node_index]
    flow_column_index = nlNodeId.index(node)

    Qnode = flow_data.iloc[1:, flow_column_index].values.astype(float)
    
    mos = [10, 11, 12] + list(range(1, 10))
    Qex = np.zeros(12) #initialize array

    sorted_data = pd.DataFrame({"Date": nfdn[idx], "Flow": Qnode[idx]})
    sorted_data = sorted_data.sort_values(by="Date")
    
    for imo in range(12):
        mo = mos[imo]
        monthly_data = sorted_data[sorted_data["Date"].dt.month == mo]
        #month_values = nfdn[idx].dt.month.values
        #ind = np.where(month_values == mo)[0]  #find all flow values in that month in the period identified
        #Q1 = Qnode[ind] * 35.31467 # convert to cfs
        Q1 = monthly_data["Flow"].values * 35.31467  # convert to cfs
        
        Qex[imo] = np.mean(Q1)
    

    return drain_name, drain_id, node, Qex


all_data = []

for drain_id, drain_name in zip(drain_mapping['DrainID'], drain_mapping['DRAIN_NAME']): 
    pnodes = nodelinks_data.loc[nodelinks_data['2'] == str(drain_id), '3']
    for pnode in pnodes:
        drain_name, drain_id_out, node, Qex = average_exceedence_to_data(
            pnode, 1952, 2011, drain_name, 'LNExisting'
        )
        all_data.append([drain_name, drain_id_out, pnode] + list(Qex))

columns = ["Location", "DrainID", "pnode",
           "Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep"]
df = pd.DataFrame(all_data, columns=columns)

df.to_csv('Q_pnodes.csv', index=False, encoding='utf-8')


# In[ ]:


# IFR: 90% exceedence flow

nodelinks_data = pd.read_csv('nodelinks.csv')
flow_data = pd.read_csv('FlowAtStreamNodes_cms.txt', header=None, delim_whitespace=True)
date_data = pd.read_csv('DateTime_yyyymmdd_hhmmss.txt', header=None, delim_whitespace=True, dtype=str, skiprows=1)
drain_mapping = pd.read_csv('DrainID.csv')

def parse_yyyymmdd_to_datetime(yyyymmdd):
    """Converts yyyymmdd string format to a Python datetime object."""
    return pd.to_datetime(yyyymmdd, format='%Y%m%d')

def get_exceedence_data_for_pnode(pnode, ystart, yend, drain_name, LNname):
    nlNodeId = nodelinks_data['0'].tolist()
    DownNodeId = nodelinks_data['1'].tolist()
    nlDrainId = nodelinks_data['2'].tolist()
    ProjNodeId = nodelinks_data['3'].tolist()
    
    nfdn = date_data[1].apply(parse_yyyymmdd_to_datetime)
    d_start = pd.Timestamp(f"{ystart}-10-01")
    d_end = pd.Timestamp(f"{yend}-09-30")
    idx = (nfdn >= d_start) & (nfdn <= d_end)
    
    print(d_start)
    
    node_index = np.where(np.array(ProjNodeId) == str(pnode))[0][0]
    node = nlNodeId[node_index]
    drain = nlDrainId[node_index]
    flow_column_index = nlNodeId.index(node)
    Qnode = flow_data.iloc[1:, flow_column_index].values.astype(float)
    
    mos = [10, 11, 12] + list(range(1, 10))
    Qex = np.zeros(12) #initialize array
    
    sorted_data = pd.DataFrame({"Date": nfdn[idx], "Flow": Qnode[idx]})
    sorted_data = sorted_data.sort_values(by="Date")
    
    for imo in range(12):
        mo = mos[imo]
        monthly_data = sorted_data[sorted_data["Date"].dt.month == mo]
        Q1 = monthly_data["Flow"].values * 35.31467  # convert to cfs
        
        Qex[imo] = np.quantile(Q1,0.1)
    

    return drain_name, drain_id, node, Qex


all_data = []
with pd.ExcelWriter('Exceedence_Flow_90.xlsx') as writer:
    for drain_id, drain_name in zip(drain_mapping['DrainID'], drain_mapping['DRAIN_NAME']): 
        pnodes = nodelinks_data.loc[nodelinks_data['2'] == str(drain_id), '3'] 
        for pnode in pnodes:
            drain_name, drain_id, node, Qex = get_exceedence_data_for_pnode(pnode, 1952, 2011, drain_name, 'LNExisting') 
            #df.to_excel(writer, sheet_name=f'{drain_name}_{pnode}', index=False)
            all_data.append([drain_name, drain_id, pnode] + list(Qex))       
            short_drain_name = drain_name[:20] 
            short_pnode = str(pnode)[:10]  
            invalid_chars = ':*?/\\[]'
            for char in invalid_chars:
                short_drain_name = short_drain_name.replace(char, '_')
                short_pnode = short_pnode.replace(char, '_')
                
    columns = ["Location", "DrainID", "pnode", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep"]
    df = pd.DataFrame(all_data, columns=columns)
    
    df.to_excel(writer, sheet_name="All_Locations", index=False)


# In[ ]:


# D & A

q_pnodes = pd.read_csv('Q_pnodes.csv')
sum_di = pd.read_csv('Sum_Di.csv')[['DrainID', 'DRAIN_NAME', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 
                                              'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']]
# Calculate monthly proportions for Q_pnodes
monthly_sum = q_pnodes.groupby('DrainID').sum(numeric_only=True)
proportion_data = q_pnodes.merge(monthly_sum, on='DrainID', suffixes=('', '_total'))
for month in ['Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']:
    proportion_data[month] = proportion_data[month] / proportion_data[f'{month}_total']

# Compute D_SUM_pnodes by merging with Sum_Di and multiplying proportions by monthly totals
d_sum_pnodes = proportion_data.drop(columns=[f'{m}_total' for m in ['Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']])
d_sum_pnodes = d_sum_pnodes.merge(sum_di, on='DrainID', suffixes=('_prop', '_total'))
for month in ['Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']:
    d_sum_pnodes[month] = d_sum_pnodes[f'{month}_prop'] * d_sum_pnodes[f'{month}_total']

d_sum_pnodes = d_sum_pnodes.drop(columns=[f'{m}_prop' for m in ['Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']] + 
                                 [f'{m}_total' for m in ['Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']])

d_sum_pnodes.to_csv("D_SUM_pnodes.csv", index=False)

# Add PFRs to both Q_pnodes and D_SUM_pnodes
def add_extended_columns(df):
    df['annual'] = df[[f'{m}' for m in ['Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']]].mean(axis=1)
    df['Sep_Nov'] = df[['Sep', 'Oct', 'Nov']].mean(axis=1)
    df['Dec_Jan'] = df[['Dec', 'Jan']].mean(axis=1)
    df['Feb_Jul'] = df[['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']].mean(axis=1)
    df['July_Nov'] = df[['Jul', 'Aug', 'Sep', 'Oct', 'Nov']].mean(axis=1)
    df['Feb_Jun'] = df[['Feb', 'Mar', 'Apr', 'May', 'Jun']].mean(axis=1)
    df['Oct_Jan'] = df[['Oct', 'Nov', 'Dec', 'Jan']].mean(axis=1)
    df['Sep_Dec'] = df[['Sep', 'Oct', 'Nov', 'Dec']].mean(axis=1)
    df['Jan_Jul'] = df[['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']].mean(axis=1)
    df['Feb_May'] = df[['Feb', 'Mar', 'Apr', 'May']].mean(axis=1)
    df['Jun_Jul'] = df[['Jun', 'Jul']].mean(axis=1)
    df['Aug_Dec'] = df[['Aug', 'Sep', 'Oct', 'Nov', 'Dec']].mean(axis=1)
    df['Jan_Jun'] = df[['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']].mean(axis=1)
    return df

# Apply extended calculations
d_sum_pnodes_extended = add_extended_columns(d_sum_pnodes.copy())
q_pnodes_extended = add_extended_columns(q_pnodes.copy())

# Save Q_pnodes_extended and D_SUM_pnodes_extended as outputs
q_pnodes_extended.to_csv("Q_pnodes_extended.csv", index=False)
d_sum_pnodes_extended.to_csv("D_SUM_pnodes_extended.csv", index=False)

# A:Combine Q_pnodes and D_SUM_pnodes
A = q_pnodes[['Location', 'DrainID', 'pnode']].merge(
    q_pnodes_extended.groupby('pnode').sum().add(d_sum_pnodes_extended.groupby('pnode').sum(), fill_value=0).reset_index(),
    on='pnode'
)

# Remove any 'DrainID_y' if present, keep only one 'DrainID'
if 'DrainID_y' in A.columns:
    A = A.drop(columns=['DrainID_y']).rename(columns={'DrainID_x': 'DrainID'})

column_order = ['Location', 'DrainID', 'pnode', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 
                'annual', 'Sep_Nov', 'Dec_Jan', 'Feb_Jul', 'July_Nov', 'Feb_Jun', 'Oct_Jan', 'Sep_Dec', 
                'Jan_Jul', 'Feb_May', 'Jun_Jul', 'Aug_Dec', 'Jan_Jun']

# Reorder columns based on the defined order and keep only available columns in the dataset
final_columns = [col for col in column_order if col in A.columns]
A = A[final_columns]

A.to_csv("A_pnodes_result.csv", index=False)


# In[ ]:


# flowdurationcurve (Supplementary Fig.1b) generation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker

nodelinks_data = pd.read_csv('nodelinks.csv',header = 1)
flow_data = pd.read_csv('FlowAtStreamNodes_cms.txt', header=0, delim_whitespace=True)
date_data = pd.read_csv('DateTime_yyyymmdd_hhmmss.txt', header=None, delim_whitespace=True, dtype=str, skiprows=1)

def parse_yyyymmdd_to_datetime(yyyymmdd):
    """Converts yyyymmdd string format to a Python datetime object."""
    return pd.to_datetime(yyyymmdd, format='%Y%m%d')

def final_export_exceedence_to_csv(pnode, ystart, yend, LNname):
    nlNodeId = nodelinks_data['NodeId'].tolist()
    DownNodeId = nodelinks_data['DownNodeId'].tolist()
    nlDrainId = nodelinks_data['DrainId'].tolist()
    ProjNodeId = nodelinks_data['ProjNodeId'].tolist()
    print(nlNodeId)
    
    nfdn = date_data[1].apply(parse_yyyymmdd_to_datetime)
    d_start = pd.Timestamp(f"{ystart}-10-01")
    d_end = pd.Timestamp(f"{yend}-09-30")
    idx = (nfdn >= d_start) & (nfdn <= d_end)
    
    print(d_start)
    
    node_index = np.where(np.array(ProjNodeId) == int(pnode))[0][0]
    node = nlNodeId[node_index]
    drain = nlDrainId[node_index]
    
    flow_column_index = nlNodeId.index(node)+1
    
    print(node)
    print(flow_column_index)
    print(flow_data.iloc[:, flow_column_index])
    
    # Extract the flow data for the node
    Qnode = flow_data.iloc[:, flow_column_index].values.astype(float)
    
    exds = np.arange(0.05, 1, 0.05) #Exceedence probabilities from 0.05 to 0.95
    mos = [10, 11, 12] + list(range(1, 10))
    Qex = np.zeros((len(exds), 12)) #initialize array

    sorted_data = pd.DataFrame({"Date": nfdn[idx], "Flow": Qnode[idx]})
    sorted_data = sorted_data.sort_values(by="Date")
    
    for imo in range(12):
        mo = mos[imo]
        monthly_data = sorted_data[sorted_data["Date"].dt.month == mo]
        Q1 = monthly_data["Flow"].values * 35.31467  # convert to cfs
        
        for iex in range(len(exds)):
            Qex[iex, imo] = np.quantile(Q1, 1 - exds[iex])
    
    fnameout = f'AccuDistribution_{pnode}.csv'
    with open(fnameout, 'w') as file:
        file.write(f"Prob/cfs,Oct,Nov,Dec,Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep\n")
        for iex in range(len(exds)):
            line = [str(exds[iex])]
            line.extend([str(Qex[iex, imo]) for imo in range(12)])
            file.write(",".join(line) + "\n")
    return fnameout

final_export_exceedence_to_csv(401, 1952, 2011,'LNExisting')


# In[ ]:


# flowdurationcurve (Supplementary Fig.1b) generation
data = pd.read_csv('AccuDistribution_401.csv')
x = data['Prob/cfs'].values
y = data.iloc[:,1:].values
months = data.columns[1:]

fig, ax = plt.subplots(figsize=(5, 3),dpi = 300)

plt.xlabel('Quantile',fontsize = 14)
plt.ylabel('Flow (cfs)',fontsize = 14)

plt.plot(x,y, label=months, linewidth=1)

# Add a horizontal line at y=0.9
ax.axvline(0.9, linestyle='--', color='red', alpha=0.5)
ax.set_title('Flow Duration Curve', fontsize = 16)

plt.legend().set_draggable(state=True)
ax.legend(prop = font1, ncol = 2, loc = 'upper right')

from matplotlib.pyplot import MultipleLocator
y_major_locator = MultipleLocator(40)
ax = plt.gca()
ax.yaxis.set_major_locator(y_major_locator)
plt.xlim(0,1)

plt.yticks(fontproperties = 'Arial',size = 16)
plt.xticks(fontproperties = 'Arial',size = 14)
plt.gca().xaxis.set_major_formatter(ticker.PercentFormatter(xmax = 1))

plt.savefig('flowdurationcurve', transparent=True)

