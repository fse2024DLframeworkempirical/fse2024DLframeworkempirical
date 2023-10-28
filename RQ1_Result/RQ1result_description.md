### RQ1: What factors impact the performance of model-mutation testing methods?

The current folder stores the results collected from experiments conducted on three groups of experimental subjects: E1, E2, and E3. In the current RQ, we have explored the effects of mutation operator type, mutation position, and mutation order on the performance of framework testing. The experimental results are stored in three folders: "rq1_singleop_result", "rq1_location_result", and "rq1_group_result". We will introduce the composition of the result files under these three folders in the following content.

The "rq1_group_result" folder stores result files by model type, for example, the "vgg16" folder stores the results of multiple variations of the vgg16 model using 11 mutation operators as candidates, with the mutation range covering all middle layers of the model. The "mut_trace_info.csv" file records the trajectory of mutation execution, and each row contains specific information about a round of mutation: the first column represents the type of mutation operator selected for the current round, the second column represents the middle layer of the selected mutation model, and the third column represents whether the generated mutation pattern is legal after the completion of the current round of mutation. The 'group_result.csv' file stores the distance metrics (defined in Section 4.3) differences between the results of the mutation model running on different frameworks during the mutation process. The three columns in the file are the distance between the mutation model on the Python framework and the Mindshare framework, the distance between the mutation model on the Python framework and the TensorFlow framework, and the distance between the mutation model on the TensorFlow framework and the Mindshare framework. Please note that since only Unet, OpenPose, and Resnet50 models can be converted through onnx2keras, we uniformly record the distances of other failed models on the framework as -100. When the distance difference exceeds the valid expression of float32 precision (distance calculation is NAN or inf), the values of these three columns are displayed as empty in the CSV file.

The folder 'rq1_singleop_result' stores the results of a single mutation operator generating a mutation model and testing it on different frameworks, divided and stored according to a single operator type. The file content of 'modelname. csv' is the same as the 'group' in the 'rq1ugroup.result' folder_ The content of the 'result. csv' file is consistent, and the 'modelname_mut_trace_info. csv' file is consistent with the content of the 'group_result. csv' file in the 'mut_trace_info. csv' folder.

Similar to the "rq1_singleop_result" folder, the "rq1_location_result" folder also stores result files based on the type of mutation operator. If the file name contains the words' backbone 'or' classhead ', it indicates that the file is mutated in the middle layer of the' backbone 'or' classhead ' part of the current model. The 'modelname_backone/classead.csv' file is consistent with the 'group-result. csv' file in 'rq1ugroup.result', and the 'modelname_backone/classead_mut_trace_info.csv' file is consistent with the 'mut_trace_info.csv' file in 'rq1ugroup.result',











