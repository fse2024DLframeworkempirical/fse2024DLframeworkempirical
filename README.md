### DL Framework Testing via Model Mutation: How Far Are We?

This is the implementation repository of our ESEC/FSE 2024 paper:  DL Framework Testing via Model Mutation: How Far Are We?
#### Description ####
In this work, we employed 11 classic DL model mutation operators and collected a total of 11 classic deep learning models from 7 scenario tasks. We conducted empirical research on three popular DL frameworks: PyTorch, MindSpore, and TensorFlow. Due to paper length limitations, we reported results that were not presented in the paper in this open-source repository. If you have any questions, please leave a message here to contact us. The following explains the organizational structure of the result files on this repository.

During the mutation process, we used the ONNX and onnx2keras frameworks to transform the mutation model from PyTorch to TensorFlow for analysis and comparison. In addition, we also collected six newly released versions of the PyTorch and MindSpore frameworks, and one released version of TensorFlow formed three sets of experiments, as shown in next Table. In the paper, only partial experimental results of E3 were reported, while in the current warehouse, we will report them in RQ1_Result, RQ2_Result and RQ3_Result The experimental results of E1 and E2 versions are displayed in three folders. Please note that since RQ3 is a user study on high-value framework issues and does not involve running experimental code to calculate results, there is no distinction between E1, E2, and E3.


| ID | Pytorch | MindSpore | TensorFlow | ONNX   | ONNX2Keras |
|----|---------|-----------|------------|--------|------------|
| E1 | 1.8.1   | 1.10.1    | 2.13.0     | 1.14.0 | 0.0.24     |
| E2 | 1.9.0   | 2.0.0     | 2.13.0     | 1.14.0 | 0.0.24     |
| E3 | 1.10.1  | 2.1.0     | 2.13.0     | 1.14.0 | 0.0.24     |

In addition, we have reported the framework issues detected during our experiments in the 'issue_detected. xlsx' file, which we have submitted to the framework repository. Among them, the first column is the description of the content of the questionnaire, the second column is whether the questionnaire has been confirmed by the framework developer, the third column is whether the questionnaire has been fixed, the fourth column is the label of the questionnaire, the fifth column is the type of questionnaire (divided into inconsistent problems, NAN problems, and Crash problems based on previous work types), and the last column is the framework category to which the questionnaire belongs.



