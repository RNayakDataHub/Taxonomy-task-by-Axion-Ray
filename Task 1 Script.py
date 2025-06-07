#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[29]:


file_path = "DA - Task 1..xlsx"
df_task = pd.read_excel(file_path, sheet_name="Task")
df_tax = pd.read_excel(file_path, sheet_name="Taxonomy")


# In[30]:


df_tax.columns = df_tax.columns.str.strip()


# In[31]:


root_causes = df_tax['Root Cause'].dropna().unique().tolist()
symptom_conditions = df_tax['Symptom Condition'].dropna().unique().tolist()
symptom_components = df_tax['Symptom Component'].dropna().unique().tolist()
fix_conditions = df_tax['Fix Condition'].dropna().unique().tolist()
fix_components = df_tax['Fix Component'].dropna().unique().tolist()


# In[32]:


def match_root_cause(text, keywords):
    matches = [kw for kw in keywords if pd.notnull(text) and kw.lower() in text.lower()]
    return ', '.join(matches) if matches else ''

df_task['Root Cause'] = df_task.apply(lambda row: match_root_cause(' '.join([str(row['Complaint']), str(row['Cause']), str(row['Correction'])]), root_causes), axis=1)

def get_top_matches(text, keyword_list, max_matches=3):
    text = str(text).lower()
    matches = [kw for kw in keyword_list if kw.lower() in text]
    matches = list(dict.fromkeys(matches))
    return (matches + [''] * max_matches)[:max_matches]


# In[33]:


df_task['combined_text'] = df_task['Complaint'].astype(str) + ' ' + \
                           df_task['Cause'].astype(str) + ' ' + \
                           df_task['Correction'].astype(str)


# In[34]:


df_task[['Symptom Condition 1', 'Symptom Condition 2', 'Symptom Condition 3']] = df_task['combined_text'].apply(lambda x: pd.Series(get_top_matches(x, symptom_conditions)))


# In[35]:


df_task[['Symptom Component 1', 'Symptom Component 2', 'Symptom Component 3']] = df_task['combined_text'].apply(lambda x: pd.Series(get_top_matches(x, symptom_components)))


# In[36]:


df_task[['Fix Condition 1', 'Fix Condition 2', 'Fix Condition 3']] = df_task['combined_text'].apply(lambda x: pd.Series(get_top_matches(x, fix_conditions)))


# In[37]:


df_task[['Fix Component 1', 'Fix Component 2', 'Fix Component 3']] = df_task['combined_text'].apply(lambda x: pd.Series(get_top_matches(x, fix_components)))


# In[38]:


df_task.to_excel('Task_with_Matched_Taxonomy.xlsx', index=False)


# In[ ]:




