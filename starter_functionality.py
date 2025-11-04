def getTimeInBinary():
    import datetime
  #  print(datetime.datetime.now().hour//10)

  #  print(datetime.datetime.now().hour%10)

  #  print(datetime.datetime.now().second)

    def convert(num):
        bin = ""
        num = int(num)
        while (num > 0):
            r = str(num % 2)
            bin = r + bin
            num = num // 2
        while(len(bin)<4):
            bin = "0" + bin
        return (bin[0],bin[1],bin[2],bin[3])
    hourInBinary = convert(datetime.datetime.now().hour//10)
    tenHourInBinary = convert(datetime.datetime.now().hour%10)
    minutesInBinary = convert(datetime.datetime.now().minute//10)
    tenMinutesInBinary = convert(datetime.datetime.now().minute%10)
    secondsInBinary = convert(datetime.datetime.now().second//10)
    tenSecondsInBinary = convert(datetime.datetime.now().second%10)
    return(tenHourInBinary,hourInBinary,minutesInBinary,tenMinutesInBinary,secondsInBinary,tenSecondsInBinary)

def drawCircles(screen, color, tenhb, tenmb,tensb):
    import pygame
    for i in range(4):
        # столбцы: часы, минуты, секунды
        x_positions = [40, 160, 280]
        bits = [tenhb, tenmb, tensb]
        for col, bitset in enumerate(bits):
            # позиция круга
            x = x_positions[col]
            y = i * 50 + 50  # смещаем вниз, чтобы всё влезало
            # если бит 1 — закрашенный круг, если 0 — только контур
            if bitset[i-4] == '1':
                pygame.draw.circle(screen, color, (x, y), 20)
            else:
                pygame.draw.circle(screen, color, (x, y), 20, 2)
def oneCircles(screen,color,hb,mb,sb):
    import pygame
    for i in range(4):
        # столбцы: часы, минуты, секунды
        x_positions = [90, 210, 330]
        bits = [hb,mb,sb]
        for col, bitset in enumerate(bits):
            # позиция круга
            x = x_positions[col]
            y = i * 50 + 50  # смещаем вниз, чтобы всё влезало
            # если бит 1 — закрашенный круг, если 0 — только контур
            if bitset[i] == '1':
                pygame.draw.circle(screen, color, (x, y), 20)
            else:
                pygame.draw.circle(screen, color, (x, y), 20, 2)
