import subprocess
import json
input_file = "test.mp4"
execution_file = "/usr/local/bin/exiftool"
process = subprocess.Popen(
    [execution_file, input_file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
metadata = []
for output in process.stdout:
    info = {}
    line = output.strip().split(":")
    info[line[0].strip()] = line[1].strip()
    metadata.append(line)
    # print(info)

for e in metadata:
    print(e)

with open('data.json', 'w') as fp:
    json.dump(metadata, fp)
