import os 

train_ragas = os.listdir("training") 

test_ragas = os.listdir("testing") 

trainRagaDict = {}
testRagaDict = {}

for raga in train_ragas: 
	trainRagaDict['raga'] = os.listdir(f"training/{raga}") 
	print(len(trainRagaDict['raga'])) 

for raga in test_ragas:
	testRagaDict['raga'] = os.listdir(f"testing/{raga}")
	print(len(testRagaDict['raga'])) 


