def timeConversion(s):
    f = s[-2:]

    hh = s[0:2] 
    mm = s[3:5] 
    ss = s[6:8]

    if f == 'PM':
        if hh== '12':
            res = f"{hh}:{mm}:{ss}"
        else:
            res = f"{(int(hh) + 12):02d}:{mm}:{ss}"
    elif f == 'AM':
        if hh == '12':
            res = f"{(12 - int(hh)):02d}:{mm}:{ss}"
        else:
            res = f"{hh}:{mm}:{ss}"
    
    return res

print(timeConversion("12:40:22AM"))