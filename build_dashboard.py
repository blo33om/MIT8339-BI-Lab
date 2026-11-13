import pandas as pd, json, plotly
df = pd.read_csv("submission/BankChurners_cleaned.csv")
cols = ["CLIENTNUM","Attrited","Gender","Card_Category","Income_Category","Age_Band","Risk_Band","Risk_Score","Txn_Frequency_Category",
        "Utilisation_Category","Total_Relationship_Count","Contacts_Count_12_mon","Months_Inactive_12_mon","Credit_Limit",
        "Avg_Utilization_Ratio","Total_Trans_Amt","Total_Trans_Ct"]
data = df[cols].to_dict(orient="list")
plotly_js = plotly.offline.get_plotlyjs()
html = open("dash_template.html").read().replace("/*PLOTLYJS*/", plotly_js).replace("/*DATA*/", json.dumps(data))
open("submission/MIT8339_BI_Dashboard.html","w").write(html)
print(len(html)/1e6,"MB")
