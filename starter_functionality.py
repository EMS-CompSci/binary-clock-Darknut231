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

def drawCircles(screen,color,hb,mb,sb):
    import pygame
    for i in range (5):
        pygame.draw.circle(screen,color,[90,i*50-20],20,int(hb[i]))
        pygame.draw.circle(screen,color,[210,i*50-20],20,int(mb[i]))
        pygame.draw.circle(screen,color,[330,i*50-20],20,int(sb[i]))
        if (i >= 3):
            pygame.draw.circle(screen,color,[30,i*50-20],20,int(hb[i]))
            pygame.draw.circle(screen,color,[150,i*50-20],20,int(mb[i]))
            pygame.draw.circle(screen,color,[270,i*50-20],20,int(sb[i]))
