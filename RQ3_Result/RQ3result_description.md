### RQ3: Can existing methods detect high-priority DL framework defects?

The current folder stores the result files in RQ3. Among them, "Total_Issue_Data" stores the raw data of the issue from MindSpore, PyTorch, and TensorFlow frameworks in recent years (please note that we have filtered out some of the data according to the description in the paper to construct an LDA model). The column names of the three files are consistent: 

The first column is the title information of the issue; 

The second column is the main content information of the issue; 

The third column is the creation time of the issue; 

The fourth column is the label information of the issue; 

The fifth column shows the frequency of discussions between framework developers and users; The sixth column shows the current status of the issue; 

The seventh column is the original link to the issue; 

The eighth column is the subject keywords output by the LDA model for the issue; 

The ninth column is the topic category to which the LDA prediction issue belongs; 

The tenth column contains manually annotated note information. 

Please note that since the LDA model output with a number of subjects of 20 is chosen as the final result in the paper, the information in columns 8 and 9 are all outputs of the LDA model with a number of subjects of 20. Due to coding issues, there may be garbled information in the first and second columns. If you are interested, you can click on the original link of the seventh column issue to access and inquire, or leave a message to contact us.

The 'LDAtopic_output' folder stores the topic results generated by the LDA model with a number of 20 topics on the MindSpore PyTorch, and TensorFlow framework issue data. The content format of the three framework result files is consistent, and each line in the txt represents a topic output by the LDA model. A topic is composed of several keywords, each with different weights.

The file "Table 1-Types_of_High_Priority_Framework_Issues. xlsx" records the high priority framework defect classification obtained by manually annotating the data in the "Total Issue Data" folder. The first column contains the main objects involved in the framework defects, including the framework itself mechanism, DL models built based on the framework, and internal interfaces of the framework; The second column is the category of framework defects; The third column is the topic description of the problem type.



The 'copiescore. pdf' file is a line chart showing the consistency scores of LDA models built on MindSpore PyTorch, and TensorFlow frameworks with a number of topics of 10,20,30,40,50.



