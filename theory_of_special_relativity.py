import pygame

def timeA():
    c = (299792458/299792458)*2
    v_train = float(input('기차의 속도(단위: c): '))*c

    # 파이게임 초기화(반드시 필요)
    pygame.init()
    
    # 화면 크기 설정
    screen_width = 1440       #화면 가로 크기
    screen_height = 960         #화면 세로 크기
    screen = pygame.display.set_mode((screen_width, screen_height))  # 튜플 형태=>가로 세로를 1개의 인자로

    # 화면 타이틀 설정
    pygame.display.set_caption("theory of special relativity")

    #배경 이미지 불러오기
    bg=pygame.image.load("imgs\\background.png")
    #이미지 사이즈 변경
    bg=pygame.transform.scale(bg, (screen_width,screen_height))

    A=pygame.image.load("imgs\\A.png")
    B=pygame.image.load("imgs\\B.png")
    
    #fps 설정
    clock = pygame.time.Clock()     #프레임 설정

    #폰트 정의
    game_font = pygame.font.Font(None, 70)      #폰트 객체 생성(글꼴, 크기)




    #기차 불러오기
    train=pygame.image.load("imgs\\train_black.jpg")
    train=pygame.transform.scale(train, (screen_width/2,screen_width/5))      
    train_size=train.get_rect().size     #이미지 크기를 구해옴
    train_width=train_size[0]
    train_height=train_size[1]
    lines = [ ]

    train_xpos= 0
    train_ypos=(screen_height-train_height)/2
    fps = 120
    #light_y = train_ypos+train_height*1/3
    light_y = train_ypos+train_height*5/6
    light_flag = 1
    # 이벤트 루프
    running = True  # 게임이 진행중인가?
    while running:
        clock.tick(fps)
        for event in pygame.event.get():  # 어떤 이벤트가 발생하는 동안 반복(큐 자료구조=>FIFO)
            if event.type == pygame.QUIT: # 창닫힘 이벤트 발생하면(x버튼)
                running = False
        
        train_xpos+=v_train
        light_x=train_xpos+train_width*1/3
        if light_y >= train_ypos+train_height*5/6 or light_y <= train_ypos+train_height*1/3:
            light_flag *= -1
            lines.append([light_x,light_y])
        if light_flag == -1:
            light_y-=c
        elif light_flag == 1:
            light_y+=c


        screen.blit(bg,(0,0))   #배경 그리기
        screen.blit(train,(train_xpos,train_ypos)) #캐릭터 그리기
        screen.blit(B,(train_xpos+train_width*2/5-70,train_ypos+train_height*5/6-60))
        screen.blit(A,(screen_width-70,screen_height-70))
        for i in range(len(lines)-1):
            pygame.draw.line(screen, (255,255,0), (lines[i][0], lines[i][1]), (lines[i+1][0], lines[i+1][1]), 2)
        pygame.draw.circle(screen, (255,255,0), (light_x, light_y), 10)



        pygame.display.update()





def timeB():
    c = (299792458/299792458)*2
    v_train = float(input('기차의 속도(단위: c): '))*c

    # 파이게임 초기화(반드시 필요)
    pygame.init()
    
    # 화면 크기 설정
    screen_width = 1440       #화면 가로 크기
    screen_height = 960         #화면 세로 크기
    screen = pygame.display.set_mode((screen_width, screen_height))  # 튜플 형태=>가로 세로를 1개의 인자로

    # 화면 타이틀 설정
    pygame.display.set_caption("theory of special relativity")

    #배경 이미지 불러오기
    bg=pygame.image.load("imgs\\background.png")
    #이미지 사이즈 변경
    bg=pygame.transform.scale(bg, (screen_width,screen_height))

    A=pygame.image.load("imgs\\A.png")
    B=pygame.image.load("imgs\\B.png")
    
    #fps 설정
    clock = pygame.time.Clock()     #프레임 설정

    #폰트 정의
    game_font = pygame.font.Font(None, 70)      #폰트 객체 생성(글꼴, 크기)




    #기차 불러오기
    train=pygame.image.load("imgs\\train_black.jpg")
    train=pygame.transform.scale(train, (screen_width/2,screen_width/5))      
    train_size=train.get_rect().size     #이미지 크기를 구해옴
    train_width=train_size[0]
    train_height=train_size[1]
    lines = [ ]

    train_xpos= 0
    train_ypos=(screen_height-train_height)/2
    fps = 120
    #light_y = train_ypos+train_height*1/3
    light_y = train_ypos+train_height*5/6
    light_flag = 1
    A_pos=screen_width-70
    # 이벤트 루프
    running = True  # 게임이 진행중인가?
    while running:
        clock.tick(fps)
        for event in pygame.event.get():  # 어떤 이벤트가 발생하는 동안 반복(큐 자료구조=>FIFO)
            if event.type == pygame.QUIT: # 창닫힘 이벤트 발생하면(x버튼)
                running = False
        
        #train_xpos+=v_train
        light_x=train_xpos+train_width*1/3
        if light_y >= train_ypos+train_height*5/6 or light_y <= train_ypos+train_height*1/3:
            light_flag *= -1
            lines.append([light_x,light_y])
        if light_flag == -1:
            light_y-=c
        elif light_flag == 1:
            light_y+=c

        A_pos-=v_train

        screen.blit(bg,(0,0))   #배경 그리기
        screen.blit(train,(train_xpos,train_ypos)) #캐릭터 그리기
        screen.blit(B,(train_xpos+train_width*2/5-70,train_ypos+train_height*5/6-60))
        screen.blit(A,(A_pos,screen_height-70))
        for i in range(len(lines)-1):
            pygame.draw.line(screen, (255,255,0), (lines[i][0], lines[i][1]), (lines[i+1][0], lines[i+1][1]), 2)
        pygame.draw.circle(screen, (255,255,0), (light_x, light_y), 10)



        pygame.display.update()
        
    #딜레이
    pygame.time.delay(50)

    # pygame 종료
    pygame.quit()




def lengthA():
    c = (299792458/299792458)*2
    v_train = float(input('기차의 속도(단위: c): '))*c
    #v_train = 0
    # 파이게임 초기화(반드시 필요)
    pygame.init()
    
    # 화면 크기 설정
    screen_width = 1440       #화면 가로 크기
    screen_height = 960         #화면 세로 크기
    screen = pygame.display.set_mode((screen_width, screen_height))  # 튜플 형태=>가로 세로를 1개의 인자로

    # 화면 타이틀 설정
    pygame.display.set_caption("theory of special relativity")

    #배경 이미지 불러오기
    bg=pygame.image.load("imgs\\background.png")
    #이미지 사이즈 변경
    bg=pygame.transform.scale(bg, (screen_width,screen_height))

    A=pygame.image.load("imgs\\A.png")
    B=pygame.image.load("imgs\\B.png")
    
    #fps 설정
    clock = pygame.time.Clock()     #프레임 설정

    #폰트 정의
    game_font = pygame.font.Font(None, 70)      #폰트 객체 생성(글꼴, 크기)

    #기차 불러오기
    train=pygame.image.load("imgs\\train_black.jpg")
    train=pygame.transform.scale(train, (screen_width/2,screen_width/5))      
    train_size=train.get_rect().size     #이미지 크기를 구해옴
    train_width=train_size[0]
    train_height=train_size[1]
    lines = [ ]

    train_xpos= 0
    train_ypos=(screen_height-train_height)/2
    fps = 120
    #light_y = train_ypos+train_height*1/3
    light_y = train_ypos+train_height*1/2
    #light_x = train_xpos+train_width*0.388
    light_x = train_xpos+train_width*0.12
    light_flag = 1
    # 이벤트 루프
    running = True  # 게임이 진행중인가?
    while running:
        clock.tick(fps)
        for event in pygame.event.get():  # 어떤 이벤트가 발생하는 동안 반복(큐 자료구조=>FIFO)
            if event.type == pygame.QUIT: # 창닫힘 이벤트 발생하면(x버튼)
                running = False
        
        if light_x >= train_xpos+train_width*0.388 or light_x <= train_xpos+train_width*0.12:
            light_flag *= -1
            lines.append([light_x,light_y])
        if light_flag == -1:
            light_x+=c
        elif light_flag == 1:
            light_x-=c
        
        train_xpos+=v_train

        screen.blit(bg,(0,0))   #배경 그리기
        screen.blit(train,(train_xpos,train_ypos)) #캐릭터 그리기
        screen.blit(B,(train_xpos+train_width*2/5-70,train_ypos+train_height*5/6-60))
        screen.blit(A,(screen_width-70,screen_height-70))
        for i in range(len(lines)-1):
            pygame.draw.line(screen, (255,255,0), (lines[i][0], lines[i][1]), (lines[i+1][0], lines[i+1][1]), 2)
        pygame.draw.circle(screen, (255,255,0), (light_x, light_y), 10)
        if len(lines) == 3:
            running = False


        pygame.display.update()



while True:
    choice = int(input("1. A가 본 시간팽창\n2. B가 본 시간팽창\n3. A가 본 길이수축\n4. B가 본 길이수축\n"))
    if choice == 1:
        timeA()
    elif choice == 2:
        timeB()
    elif choice == 3:
        lengthA()
    