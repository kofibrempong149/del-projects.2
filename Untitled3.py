#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


df = pd.read_csv("C:/Users/HP/Desktop/bank_account_or_service_complaints.csv")


# In[7]:


df


# In[9]:


df.drop(["sub_issue","consumer_complaint_narrative","company_public_response","zip_code","tags","consumer_consent_provided"],axis=1,inplace=True)


# In[11]:


df.head()


# In[39]:


import matplotlib.pyplot as plt


# In[196]:


bank_complaints_by_submission = df['submitted_via'].value_counts()
colors = ['gold', 'blue', 'green', 'grey', 'black','red']

fig, ax = plt.subplots()
bars = ax.bar(bank_complaints_by_submission.index, bank_complaints_by_submission.values, color=colors)
ax.set_title('COMPLAINTS BY SUBMISSION METHOD')
ax.set_xlabel('Submitted_via')
ax.set_ylabel('Number of Complaints')

# Add a legend
legend_labels = ['web', 'referral', 'phone', 'postal mail', 'fax','email']
ax.legend(bars, legend_labels, title='KEY', loc='upper right')

plt.show()


# In[77]:


import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[165]:


top_states_data = df['state'].value_counts().head(6).reset_index()
top_states_data.columns = ['state', 'complaint_count']
colors = ['gold', 'blue', 'green', 'grey', 'black','red']


# Use seaborn to create a bar plot
plt.figure(figsize=(8, 3))
sns.barplot(x='state', y='complaint_count', data=top_states_data, palette=colors)
plt.title('Top 6 States with Highest Number of Complaints')
plt.xlabel('State')
plt.ylabel('Number of Complaints')
legend_labels = ['CA', 'FL', 'NY', 'TX', 'NJ','PA']
plt.legend(bars, legend_labels, title='key', loc='upper right')
plt.show()


# In[191]:


least_states_data = df['state'].value_counts().tail(6).reset_index()
least_states_data.columns = ['state', 'complaint_count']
colors = ['gold', 'blue', 'green', 'grey', 'black','red']

# Use seaborn to create a bar plot
plt.figure(figsize=(7, 3))
sns.barplot(x='state', y='complaint_count', data=least_states_data, palette='viridis')
plt.title('The States with Lowest Number of Complaints')
plt.xlabel('State')
plt.ylabel('Number of Complaints')
legend_labels = ['AS', 'MP', 'MH', 'FM', 'AA','PW']
plt.legend(bars, legend_labels, title='key', loc='upper right')
plt.show()


# In[90]:


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[148]:


top_states_data = df['state'].value_counts().head(62).reset_index()
top_states_data.columns = ['state', 'complaint_count']


# In[149]:


top_submitted_via_data = df['submitted_via'].value_counts().head(62).reset_index()
top_submitted_via_data.columns = ['submitted_via', 'complaint_count']


# In[150]:


print("Top States Data:")
print(top_states_data)


# In[135]:


print("\nTop Submitted Via Data:")
print(top_submitted_via_data)


# In[152]:


top_issue_data = df['issue'].value_counts().head().reset_index()
top_issue_data.columns = ['issue', 'complaint_count']


# In[153]:


print("Top issue Data:")
print(top_issue_data)


# In[167]:


df['date_received'] = pd.to_datetime(df['date_received'])


# In[168]:


df_2016 = df[df['date_received'].dt.year == 2016]


# In[169]:


number_of_issues_2016 = len(df_2016)


# In[170]:


print(f"Number of issues in 2016: {number_of_issues_2016}")


# In[172]:


import pandas as pd 


# In[173]:


df['date_received'] = pd.to_datetime(df['date_received'])


# In[174]:


df_2016 = df[df['date_received'].dt.year == 2016].copy()


# In[175]:


number_of_issues_2016 = len(df_2016)


# In[176]:


print(f"Number of issues in 2016: {number_of_issues_2016}")


# In[177]:


df_2016['month'] = df_2016['date_received'].dt.month


# In[183]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[184]:


df_2016['month_abbr'] = df_2016['date_received'].dt.strftime('%b')


# In[193]:


plt.figure(figsize=(10, 5))
sns.countplot(x='month_abbr', data=df_2016, palette='viridis')
plt.title('Number of Issues per Month in 2016')
plt.xlabel('Month')
plt.ylabel('Number of Issues')
plt.show()


# In[189]:


# Get value counts for each 'submitted_via' value grouped by 'state'
submitted_via_counts_by_state = df.groupby(['state', 'submitted_via']).size().reset_index(name='count')

# Pivot the data to have 'submitted_via' values as columns
submitted_via_counts_pivot = submitted_via_counts_by_state.pivot(index='state', columns='submitted_via', values='count').fillna(0)

# Display the result
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

print(submitted_via_counts_pivot)


# In[ ]:




