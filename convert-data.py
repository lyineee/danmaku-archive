from datetime import datetime
import os
import traceback
import shutil

# convert timestamp danmaku file name to datetime file name
danmaku_input_dir = "./row"
danmaku_outpu_dir = "./row-date"
file_list = list(os.walk(danmaku_input_dir))[0][2]  # get all file
for danmaku_file in file_list:
    file_name = os.path.splitext(danmaku_file)[0]
    try:
        timestamp = int(file_name)
    except ValueError:
        continue
    date = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%dT%H-%M")
    try:
        shutil.copy(
            os.path.join(danmaku_input_dir, danmaku_file),
            os.path.join(danmaku_outpu_dir, date + ".txt"),
        )
    except FileExistsError:
        traceback.print_exc()
