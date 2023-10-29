
import os
import pandas as pd

exps = ["E1", "E2", "E3"]
path = r"/data1/myz/upload/RQ2_Result/{}"

for exp in exps:
    models = os.listdir(path.format(exp))

    for model in models:
        files = os.listdir(path.format(exp) + "/" +model)
        for file in files:
            if ".log" in file or "middlayer_distance.csv" in file:
                os.remove(path.format(exp) + "/" +model + "/" + file)


