import random
import os

class RandomPhoto:
    @staticmethod
    def get_photo_paths():
        # folder_path = '/Users/dobonmu/Desktop/IBAS/mysite/polls/photo'
        folder_path = './polls/photo'
        file_paths = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_paths.append(os.path.join(root, file))
        return file_paths[1:]
    
    
    def choose(random_list):
        random_value1=random.randint(0,len(random_list)-1)
        random_value2=random.randint(0,len(random_list)-1)
        while random_value1==random_value2:
            random_value2=random.randint(0,len(random_list))-1
        r_photo_1=random_list[random_value1][1:]
        r_photo_2=random_list[random_value2][1:]
        return r_photo_1,r_photo_2
