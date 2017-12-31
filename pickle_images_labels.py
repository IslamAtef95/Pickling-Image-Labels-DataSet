import pickle
import os
import cv2

# loading the dataset
data_dir = "D:\\Neural dataset"
pickle_in = open("train.p", "wb")

images = [] # place to store images
labels = [] # place to store label for each image
files_names = [os.path.join(data_dir, f) 
	for f in os.listdir(data_dir) if f.endswith(".txt")]

for f in files_names:
    file = open(f,encoding="utf8")
    string = file.readline()
    stringss = string.split(" ")

    # get label for each image
    if stringss[len(stringss)-1][0] == '#':
        x = 0
    else:
        x = 1
    labels.append(x)

# loading the images
files_names = [os.path.join(data_dir, f) 
	for f in os.listdir(data_dir) if f.endswith(".jpg")]
for f in files_names:
    img = cv2.resize(cv2.imread(f), (32,32))
    images.append(img)
    
dict_data = {'features':images,'labels':labels} # dictionary for images and associated labels

# pickle the dictionary
pickle.dump(dict_data,pickle_in)
pickle_in.close()
