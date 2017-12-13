# convert .flac to .wav
# References from baidu-research/ba-dls-deepspeech
# Link: https://github.com/baidu-research/ba-dls-deepspeech

# find from local directory
# Find file base on file name, with form "*.flac"
# wc - print newline, word, and byte counts for each file [Ubuntu manpages]

find ../. -iname "*.flac" | wc

for flacfile in `find ../. -iname "*.flac"`
do
    avconv -y -f flac -i $flacfile -ab 64k -ac 1 -ar 16000 -f wav "${flacfile%.*}.wav"
done
