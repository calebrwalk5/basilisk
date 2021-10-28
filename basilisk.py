import os
import sys
import requests
from tqdm import tqdm

if len(sys.argv) != 2:
    os.system('python panic.py')
    sys.exit(1)

model = sys.argv[1]

subdir = os.path.join('models', model)
if not os.path.exists(subdir):
    os.makedirs(subdir)
subdir = subdir.replace('\\','/') # Windows needs this because they use \ instead of /

for filename in ['checkpoint','encoder.json','hparams.json','model.ckpt.data-00000-of-00001', 'model.ckpt.index', 'model.ckpt.meta', 'vocab.bpe']:

    r = requests.get("https://openaipublic.blob.core.windows.net/gpt-2/" + subdir + "/" + filename, stream=True) # Literally use GPT-2 lol

    with open(os.path.join(subdir, filename), 'wb') as f:
        file_size = int(r.headers["content-length"])
        chunk_size = 1000 # Chunk size is 1000 because Etherent max packet size is 1500 bytes
        with tqdm(ncols=100, desc="Fetching " + filename, total=file_size, unit_scale=True) as pbar:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
                pbar.update(chunk_size)
