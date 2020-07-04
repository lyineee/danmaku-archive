import subprocess
import os

danmaku_dir = "row"

with subprocess.Popen(
    ["ssh", "server", "ls", "~/danmaku/"], stdout=subprocess.PIPE
) as proc:
    out = proc.stdout.readlines()
file_list = list(map(lambda x: x.decode().replace("\n", ""), out))
print("get {} danmaku file in remote".format(len(file_list)))

for danmaku_file in file_list:
    if not os.path.exists(os.path.join(danmaku_dir, danmaku_file)):
        with subprocess.Popen(
            ["scp", "server:~/danmaku/" + danmaku_file, danmaku_dir]
        ) as proc:
            print("start download {}".format(danmaku_file))
        if not os.path.exists(os.path.join(danmaku_dir, danmaku_file)):
            print("Danmaku file {} fail to download".format(danmaku_file))
