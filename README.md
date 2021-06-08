# Installation of Rasa
conda create -n rasa python=3.6

# Need to run in every terminal for rasa sandbox 
conda activate rasa
# pip install rasa[full] # adds all dependencies of rasa
pip install rasa

#  Initialize with Rasa 
rasa init

#  Training the Chatbot
rasa train
#  Running actions
rasa run actions
