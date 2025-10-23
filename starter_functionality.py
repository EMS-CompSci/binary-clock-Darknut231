def getTimeInBinary():
    import datetime
    print(datetime.datetime.now().hour)

    print(datetime.datetime.now().minute)

    print(datetime.datetime.now().second)

    def convert(num):
        bin = ""
        num = int(num)
        while (num > 0):
            r = str(num % 2)
            bin = r + bin
            num = num // 2
        while(len(bin)<7):
            bin = "0" + bin
        return (bin[0],bin[1],bin[2],bin[3],bin[4],bin[5])
    hourInBinary = convert(datetime.datetime.now().hour)
    minutesInBinary = convert(datetime.datetime.now().hour)
    secondsInBinary = convert(datetime.datetime.now().minute)
    return(hourInBinary,minutesInBinary,secondsInBinary)



