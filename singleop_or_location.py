
import os
import pandas as pd

exps = ["E1", "E2", "E3"]
path = r"/data1/myz/upload/RQ1_Result/{}/rq1_location_result"#rq1_singleop_result

for exp in exps:
    mut_ops = os.listdir(path.format(exp))

    for mut_op in mut_ops:
        files = os.listdir(path.format(exp) + "/" + mut_op)

        for file in files:
            if "mut_trace_info" in file:
                continue
            data = pd.read_csv(path.format(exp) + "/" + mut_op + "/" +file)
            new_data = data.iloc[:,range(3)]
            new_data.columns = ["pt_ms", "pt_tf", "ms_tf"]
            #new_data.to_csv(path.format(exp) + "/" + mut_op + "/" +file,index=False)

print(new_data)