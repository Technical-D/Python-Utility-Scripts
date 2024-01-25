
def speedDetection(ort, speed):
    nrt = ort / speed

    return nrt

originalRunTime = int(input('Give Original runtime of video(in Minute): '))
speed = float(input('Speed of video: '))

print(f"New runtime for the video is {speedDetection(originalRunTime, speed)} Minutes.")