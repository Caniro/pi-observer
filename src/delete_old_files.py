import os
from datetime import datetime

current_timestamp = datetime.now().timestamp()

def delete_old_files(target_dir, elapsed_day):
    elapsed_second = elapsed_day * 24 * 60 * 60
#    print('elapsed_second :', elapsed_second)
    for video in os.listdir(target_dir):
        if (video.find('.h264') == -1):
            continue
        else:
            video = target_dir + video
            time_after_last_modify = current_timestamp - \
                    os.stat(video).st_mtime
#            print(video, ':', time_after_last_modify)
            if (time_after_last_modify > elapsed_second):
                try:
                    os.remove(video)
                    print(video, 'is deleted')
                except OSError:
                    print('Error: Cannot delete', video)


#delete files elasped 3 days in ~/CCTV/data/
delete_old_files('../data/', 3)
