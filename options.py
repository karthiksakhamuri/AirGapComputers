rate = 44100 # number of samples collected per second
freq =19100# chosen because it is outside most people's hearing and worked for my microphone and speakers
channels = 1 # number of audio channels mono or stero
frame_length = 3 # length of audio  buffer
chunk = 256 # number of frames in buffer
datasize = chunk * frame_length
sigil = "00" # for identification of different bits in continoous stream
