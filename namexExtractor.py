import os
import pickle

data_dir = 'd:/Machine Learning/Projects/Bollywood Celeb Classifier/data'
data_dir_main = 'd:/Machine Learning/Projects/Bollywood Celeb Classifier/'

if not os.path.exists(data_dir):
    raise FileNotFoundError(f"Directory '{data_dir}' does not exist. Please check the path.")

filenames = []

actors = os.listdir(data_dir)
for actor in actors:
    actor_path = os.path.join(data_dir, actor)
    if os.path.isdir(actor_path):
        for file in os.listdir(actor_path):
            file_path = os.path.join(actor_path, file)
            filenames.append(file_path)
    else:
        print(f"'{actor_path}' is not a directory, skipping.")


pickle_file = os.path.join(data_dir_main, 'filenames.pkl')
with open(pickle_file, 'wb') as f:
    pickle.dump(filenames, f)

print(f"Filenames successfully saved to {pickle_file}")
