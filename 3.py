import pandas as pd
jobs_data = {
    "JOB_ID": ["AD_PRES", "AD_VP", "AD_ASST", "FI_MGR", "FI_ACCOUNT", "AC_MGR", "AC_ACCOUNT", 
               "SA_MAN", "SA_REP", "PU_MAN", "PU_CLERK", "ST_MAN", "ST_CLERK", "SH_CLERK", "IT_PROG"],
    "JOB_TITLE": [
        "President", "Administration Vice President", "Administration Assistant", "Finance Manager", 
        "Accountant", "Accounting Manager", "Public Accountant", "Sales Manager", "Sales Representative",
        "Purchasing Manager", "Purchasing Clerk", "Stock Manager", "Stock Clerk", "Shipping Clerk", "Programmer"
    ]
}
jobs_df = pd.DataFrame(jobs_data)
sorted_jobs_df = jobs_df.sort_values(by="JOB_TITLE", ascending=False)
print(sorted_jobs_df)

