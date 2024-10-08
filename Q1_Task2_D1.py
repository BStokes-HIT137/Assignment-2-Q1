#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#Q1_T2
#to load error library
import os
import warnings

#consider creating a virtual environment to install libraries as recommended

#pip install or python3<FILE_NAME>.py install
import subprocess

#need PyTorch first to run scispacY
subprocess.run(['pip', 'install','torch'])

#access the libraries call the cmd prompt to download required libraries from the internet
subprocess.run(['pip', 'install','https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_core_sci_sm-0.5.4.tar.gz'])
subprocess.run(['pip', 'install','https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_ner_bc5cdr_md-0.5.4.tar.gz'])
subprocess.run(['pip', 'install','git+https://github.com/huggingface/transformers'])

#validate loop to check the installation of the libraries
try:
    #Pytorch is needed to run spacy libraries
    import torch
    #natural language processing needed for tokenization of words to logical items ---- which requires to be referenced add that in or ELSE!
#    import nltk                 will need to add to pip if needed
    import transformers
    #load Biobert from hugging face
    from transformers import AutoTokenizer, AutoModel
    model_name = 'dmis-lab/biobert-base-cased-v1.1'
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    import spacy
    spacy.load('en_core_sci_sm')
    spacy.load('en_ner_bc5cdr_md')

    #ignore update versions messages (not sure they were activly suppressed)
    warnings.filterwarnings('ignore', message = 'possible set union')
    warnings.filterwarnings('ignore', message = 'clean_up_tokenization_spaces')
    #Message to validate loading    
    print("congratulations all libraries were installed and successfully loaded")

except ImportError as e:
    print(f'Error in loading library: {e}')
except OSError as e:
    print(f'Check your operating system: {e}')
except Exception as e:
    print(f'Surprise, an unextpected error has occured: {e}')
#Q1_T2_end task
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------

