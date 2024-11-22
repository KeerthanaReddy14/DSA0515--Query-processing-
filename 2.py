import pandas as pd
job_history_data = {
    "EMPLOYEE_ID": [102, 101, 101, 201, 114, 122, 200, 176, 176, 200],
    "START_DATE": [
        "2001-01-13", "1997-09-21", "2001-10-28", "2004-02-17", "2006-03-24", 
        "2007-01-01", "1995-09-17", "2006-03-24", "2007-01-01", "2002-07-01"
    ],
    "JOB_ID": ["IT_PROG", "AC_ACCOUNT", "AC_MGR", "MK_REP", "ST_CLERK", 
               "ST_CLERK", "AD_ASST", "SA_REP", "SA_MAN", "AC_ACCOUNT"]
}
job_history_df = pd.DataFrame(job_history_data)
employee_job_counts = job_history_df.groupby("EMPLOYEE_ID").size()
employees_with_multiple_jobs = employee_job_counts[employee_job_counts > 1].index.tolist()
print(employees_with_multiple_jobs)
