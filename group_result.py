
import os
import pandas as pd

exps = ["E1", "E2", "E3"]
path = r"/data1/myz/upload/RQ1_Result/{}/rq1_group_result"

for exp in exps:
    models = os.listdir(path.format(exp))

    for model in models:
        data = pd.read_csv(path.format(exp) + "/" +model+"/group_result.csv")
        new_data = data.iloc[:,range(3)]
        new_data.columns = ["pt_ms", "pt_tf", "ms_tf"]
        new_data.to_csv(path.format(exp) + "/" +model+"/group_result.csv",index=False)

print(new_data)