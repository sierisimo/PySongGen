#! /bin/bash

for i in $@
do
    wget ${i%:*.mp3} -O ${i##*:}
done
