import random
import os
import pandas as pd
from tools.settings import *
'''
    This script will save 3 files: train.txt, val.txt, test.txt.
    each file has the following format:
    --------------------------------------------------------------
    PathFile <Tab> actionName
    ex:
        data/video/video_1	death
        data/video/video_2	kill
        data/video/video_2	NoAction

	--------------------------------------------------------------
'''
kill_path = kill_path
#NoAction_path = NoAction_path

def accumulate_videos(videos_path):
    videos = os.listdir(videos_path)
    videos_path_list = []
    for video in videos:
        videos_path_list.append(videos_path + video)
    return videos_path_list

def append_label(videos_path, action):
    data_with_label = []
    for video_path in videos_path:
        data_with_label.append([video_path, action])
    return data_with_label

def split_train_val_test_data(videos):
    random.shuffle(videos)
    number_of_total_data = len(videos)
    number_of_test_videos = int(number_of_total_data * test_dataset_ratio)
    number_of_val_videos = int(number_of_total_data * val_dataset_ratio)

    list_of_test_videos = videos[ : number_of_test_videos]
    list_of_val_videos = videos[number_of_test_videos : (number_of_test_videos+number_of_val_videos)]
    list_of_train_videos = videos[(number_of_test_videos+number_of_val_videos) : ]
    return list_of_train_videos, list_of_val_videos, list_of_test_videos

def split():
    print("Splitting the ginen dataset into Train Test={0} Validation={1}".format(test_dataset_ratio, val_dataset_ratio))
    #Preparing Dataset List
    #death
    death_videos = accumulate_videos(death_path)
    death_videos = append_label(death_videos, "death")
    train_death_videos, val_death_videos, test_death_videos = split_train_val_test_data(death_videos)
    #kill
    kill_videos = accumulate_videos(kill_path)
    kill_videos = append_label(kill_videos, "kill")
    train_kill_videos, val_kill_videos, test_kill_videos = split_train_val_test_data(kill_videos)
    #NoAction
    NoAction_videos = accumulate_videos(NoAction_path)
    NoAction_videos = append_label(NoAction_videos, "NoAction")
    train_NoAction_videos, val_NoAction_videos, test_NoAction_videos = split_train_val_test_data(NoAction_videos)
    #smoke
    smoke_videos = accumulate_videos(smoke_path)
    smoke_videos = append_label(smoke_videos, "smoke")
    train_smoke_videos, val_smoke_videos, test_smoke_videos = split_train_val_test_data(smoke_videos)

    #Preparing Dataset
    train_data_list = train_death_videos + train_kill_videos + train_NoAction_videos + train_smoke_videos
    random.shuffle(train_data_list)
    train = pd.DataFrame(train_data_list, columns = ['Video_url', 'action'])
    train.to_csv(os.path.join(dataset_path, 'train.csv'), index=False)

    val_data_list = val_death_videos + val_kill_videos + val_NoAction_videos + val_smoke_videos
    random.shuffle(val_data_list)
    val = pd.DataFrame(val_data_list, columns = ['Video_url', 'action'])
    val.to_csv(os.path.join(dataset_path, 'val.csv'), index=False)

    test_data_list = test_death_videos + test_kill_videos + test_NoAction_videos + test_smoke_videos
    random.shuffle(test_data_list)
    test = pd.DataFrame(test_data_list, columns = ['Video_url', 'action'])
    test.to_csv(os.path.join(dataset_path, 'test.csv'), index=False)
    print("Done")
