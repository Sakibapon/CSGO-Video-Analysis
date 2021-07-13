import os

dataset_path = "E:/Data"
death_path = os.path.join(dataset_path, "death/")
kill_path = os.path.join(dataset_path, "kill/")
#smoke_path = os.path.join(dataset_path, "smoke/")
#t_path = os.path.join(dataset_path, "t/")
train_frames_path_name = 'train_frames'
val_frames_path_name = 'val_frames'
test_frames_path_name = 'test_frames'
train_frames_path = os.path.join(dataset_path, train_frames_path_name, "")
val_frames_path = os.path.join(dataset_path, val_frames_path_name, "")
test_frames_path = os.path.join(dataset_path, test_frames_path_name, "")

val_dataset_ratio = 0.2
test_dataset_ratio = 0.2
