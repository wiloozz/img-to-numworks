So, you want to convert an image to send it to your numworks ?

First of all, you need to know that the calculator only has a 320x240 resolution, so you need to scale down the image. The getImage script will automaticly convert the image to black and white.

To start converting an image, start by changing the parameters in "parameters.py" (the most important are SRCimage and outputFile)

Then, run the getImage script that converts the image to binary (1 for white, 0 for black)

Finally, run the encode.py script, it compresses the binary.

All you have to do now is to copy the decode.py script, change the "compressed_input" variable to what was written in the output file, and send it to your numworks calculator :)

(The minified decode file does the same as the normal decode file but it is more compact to save space on your numworks)
