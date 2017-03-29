
# coding: utf-8

# In[24]:

# Import workflow elements
from nipype import Node, Workflow
from IPython.display import Image
import warnings
from nipype.interfaces import fsl
import glob


# In[16]:

# Import necessary interfaces


# In[17]:

# make nodes
node_bet = Node(fsl.BET (functional=True), name='fsl_bet')
# gonna want plots and mat
node_mcFlirt = Node(fsl.MCFLIRT(save_mats=True,save_plots=True), name='motion_corr')


# In[20]:

# define workflow
wf = Workflow(name="group_workflow")
#make sure you define a base dir, else it will put everything in the temp dir
wf.base_dir = 'Group_test'


# In[21]:

# workflow connect
# the out_file is the file produced by bet, which then becomes the input of mcflirt
wf.connect([
    (node_bet, node_mcFlirt, [("out_file", "in_file")])
])


# In[22]:

#make neat graph
Image(filename=wf.write_graph())


# In[23]:

#define the inputs
wf.inputs.fsl_bet.in_file = '/home/jovyan/work/ds000114/sub-01/func/sub-01_task-linebisection_bold.nii.gz'
execution_graph=wf.run()


# In[ ]:



