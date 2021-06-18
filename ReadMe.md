# Installation of Rasa
conda create -n rasa python=3.6

pip install rasa
# Installation of Rasa

# Need to run in every terminal for rasa sandbox 
conda activate rasa

#  Initialize with Rasa 
rasa init

#  Training the Chatbot
rasa train
#  Running actions
rasa run actions
