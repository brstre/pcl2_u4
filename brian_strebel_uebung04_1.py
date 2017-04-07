# Brian Strebel, 11-919-966
import glob
import lxml
import mmh3

files = glob.iglob('./SAC-Jahrbuch_.*\.xml')

for file in files:
    with open(file) as src, open('top_20_sents.txt', 'w') as trg:
        sentence_hashes = set()
        for sentence in src:
            sentence_hash = mmh3.hash(sentence)
            if sentence_hash not in sentence_hashes:
                sentence_hashes.add(sentence_hash)
                trg.write(sentence)