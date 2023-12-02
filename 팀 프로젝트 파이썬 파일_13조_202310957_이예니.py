import pygame
import pygame_gui
import random
import time

# 파이게임 라이브러리 초기화
pygame.init()

# 창 생성
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("알게콘 프로젝트")

# pygame_gui 모듈을 사용하기 위해 UI 관리창 생성
MANAGER = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))

# UITextBox를 사용할 때 오류를 안 뜨게 하는 장치
MANAGER.preload_fonts([{'name': 'fira_code', 'point_size': 24, 'style': 'bold'}])

###################################################################################################################################################

# 게임 루프
def main():
    run = True
    score = 0
    username = "user"
    s = 1

    # 1. 시작 화면
    bg_main = pygame.image.load("background.png") # 메인 배경으로 사용할 이미지를 불러옴
    bg_main = pygame.transform.scale(bg_main, (SCREEN_WIDTH, SCREEN_HEIGHT)) # 메인 배경의 사이즈를 가로 1200(SCREEN_WIDTH), 세로 700(SCREEN_HEIGHT)로 맞춤

    FRAME_START_RECT = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT) # 직사각형: UI 요소의 크기를 결정하는 역할을 함 # (0, 0) 은 위치를 (SCREENWIDTH, SCREEN_HEIGHT)는 크기를 의미함

    frame_start = pygame_gui.elements.UIPanel(    # 패널을 프레임으로 사용함
        relative_rect=FRAME_START_RECT, manager=MANAGER
    )

    frame_start_bg = pygame_gui.elements.UIImage(
        relative_rect=FRAME_START_RECT, image_surface=bg_main, manager=MANAGER, container=frame_start    # container를 사용하여 시작 화면에 배경을 입힘
    )



    # 1. 시작 화면 - "메모리 게임" 라벨
    image_logo = pygame.image.load("logo.png") # 메모리 게임이 적힌 이미지
    image_logo = pygame.transform.scale(image_logo, (300, 100))

    LOGO_RECT = pygame.Rect(80, 50, 300, 100)

    label_logo = pygame_gui.elements.UIImage(
        relative_rect=LOGO_RECT, image_surface=image_logo, manager=MANAGER, container=frame_start
    )



    # 1. 시작 화면 - 시작 버튼
    button_image_start = pygame.image.load("start.png")
    button_image_start = pygame.transform.scale(button_image_start, (400, 170))

    START_RECT = pygame.Rect(30, 200, 400, 170)

    button_start = pygame_gui.elements.UIImage(
        relative_rect=START_RECT, image_surface=button_image_start, manager=MANAGER, container=frame_start
    )



    # 1. 시작 화면 - 튜토리얼 버튼( 클릭하면 튜토리얼 프레임으로 전환 )
    button_image_tutorial = pygame.image.load("tutorial.png")
    button_image_tutorial = pygame.transform.scale(button_image_tutorial, (400, 170))
    BUTTON_TUTORIAL_RECT = pygame.Rect(30, 350, 400, 170)

    button_tutorial = pygame_gui.elements.UIImage(
        relative_rect=BUTTON_TUTORIAL_RECT, image_surface=button_image_tutorial, manager=MANAGER, container=frame_start
    )



    # 1. 시작 화면 - 닉네임 입력 버튼
    button_image_nickname = pygame.image.load("nickname.png")
    button_image_nickname = pygame.transform.scale(button_image_nickname, (400, 170))

    BUTTON_NICKNAME_RECT = pygame.Rect(30, 500, 400, 170)

    button_nickname = pygame_gui.elements.UIImage(
        relative_rect=BUTTON_NICKNAME_RECT, image_surface=button_image_nickname, manager=MANAGER, container=frame_start
    )



    # 1. 시작 화면 - 닉네임 입력 엔트리
    ENTRY_NICKNAME_RECT = pygame.Rect(75, 630, 300, 50)

    entry_nickname = pygame_gui.elements.UITextEntryLine(
        relative_rect=ENTRY_NICKNAME_RECT, manager=MANAGER, container=frame_start
    )
    entry_nickname.hide() # 해당 엔트리는 닉네임 입력 버튼을 클릭한 후 보여야 하므로 숨김 처리

####################################################################################################################################################

    # 2. 튜토리얼 화면
    FRAME_TUTORIAL_RECT = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    frame_tutorial = pygame_gui.elements.UIPanel(
        relative_rect=FRAME_TUTORIAL_RECT, manager=MANAGER
    )

    frame_image_tutorial = pygame_gui.elements.UIImage(
        relative_rect=FRAME_TUTORIAL_RECT, manager=MANAGER, image_surface=bg_main, container=frame_tutorial
    )



    # 2. 튜토리얼 화면 - 홈 버튼
    button_image_home = pygame.image.load("home.png")
    button_image_home = pygame.transform.scale(button_image_home, (100, 100))

    HOME_RECT = pygame.Rect(SCREEN_WIDTH-200, 100, 100, 100)

    button_home = pygame_gui.elements.UIImage(
        relative_rect=HOME_RECT, image_surface=button_image_home, manager=MANAGER, container=frame_tutorial
    )



    # 2. 튜토리얼 화면 - 튜토리얼 레이블(게임 순서 안내 역할)
    label_image_tutorial = pygame.image.load("tutorial2.png")
    label_image_tutorial = pygame.transform.scale(label_image_tutorial, (900, 600))

    Label_TUTORIAL_RECT = pygame.Rect(30, 30, 900, 600)

    label_tutorial = pygame_gui.elements.UIImage(
        relative_rect=Label_TUTORIAL_RECT, image_surface=label_image_tutorial, manager=MANAGER, container=frame_tutorial
    )

 ##################################################################################################################################################

    # 3. 게임 화면
    FRAME_GAME_RECT  = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

    frame_game = pygame_gui.elements.UIPanel(
        relative_rect=FRAME_GAME_RECT, manager=MANAGER
    )

    frame_image_game = pygame_gui.elements.UIImage(
        relative_rect=FRAME_GAME_RECT, manager=MANAGER, image_surface=bg_main, container=frame_game
    )



    # 트럼프 카드의 위치 조정을 위한 리스트 생성
    x = [200, 400, 600, 800]
    y = [100, 300, 500]

    lst = []
    for i in x:
        for j in y:
            lst.append([i, j])

    # 트럼프 카드를 랜덤하게 배치하기 위해, 위치 리스트의 원소를 무작위로 섞음
    random.shuffle(lst)



    # 3. 게임 화면 - (게임을 진행하며 볼 수 있는) 점수판: 점수를 계속 업데이트해주기 위해 함수로 구현
    def checkScore():
        SCORE_RECT = pygame.Rect( 95, 30, 170, 50)

        html_text = f"<b><font color='#FFFFFF' size=6> score: {score}</font></b>"  # pygame_gui 라이브러리에서는 UITextBox에서만 폰트를 지정할 수 있음. 이를 위해 꼭 필요한 요소가 html_text임

        pygame_gui.elements.UITextBox(
            html_text=html_text, relative_rect=SCORE_RECT, manager=MANAGER, container=frame_game
        )
    checkScore()

    ################################################################################################################################################

    # 4. 점수 화면
    bg_black = pygame.image.load("background_black.png") # 검은 배경
    bg_black = pygame.transform.scale(bg_black, (SCREEN_WIDTH, SCREEN_HEIGHT))

    FRAME_SCORE_RECT = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    frame_score = pygame_gui.elements.UIPanel(
        relative_rect=FRAME_SCORE_RECT, manager=MANAGER
    )

    frame_score_bg = pygame_gui.elements.UIImage(
        relative_rect=FRAME_SCORE_RECT, manager=MANAGER, image_surface=bg_black, container=frame_score
    )



    # 4. 점수 화면 1) 점수 초기화 버튼
    button_reset_image = pygame.image.load("reset.png")
    button_reset_image = pygame.transform.scale(button_reset_image, (400, 170))

    RESET_RECT = pygame.Rect(750, 350, 400, 170)

    button_reset = pygame_gui.elements.UIImage(
        relative_rect=RESET_RECT, manager=MANAGER, image_surface=button_reset_image, container=frame_score
    )



    # 4. 점수 화면 2) 다시 시작 버튼
    button_restart_image = pygame.image.load("restart.png")
    button_restart_image = pygame.transform.scale(button_restart_image, (400, 170))

    RESTART_RECT = pygame.Rect(750, 500, 400, 170)

    button_restart = pygame_gui.elements.UIImage(
        relative_rect=RESTART_RECT, manager=MANAGER, image_surface=button_restart_image, container=frame_score
    )

#######################################################################################################################################################

    # 사용자의 이름과 점수를 기록하는 함수
    def scoreboard():

        with open("score.txt", "r",  encoding="utf-8") as file:
            lines = file.readlines()

        # 새로운 점수와 이름을 추가
        new_entry = f"{username} {score_final}\n"
        lines.append(new_entry)

        # 리스트를 오름차순으로 정렬
        lines.sort(key=lambda x: str(x.split()[1]))

        # "score.txt" 파일을 초기화 (내용을 모두 지우고 다시 작성)
        with open("score.txt", "w") as file:
            file.writelines(lines)

######################################################################################################################################################

    # 시작 화면만 보이도록 설정: 시작 화면을 제외한 화면 숨기기
    frame_tutorial.hide()
    frame_game.hide()
    frame_score.hide()



    # 현재 프레임의 상태를 알려주는 부울형 변수
    isStartFrameVisible = True
    isTutorialFrameVisible = False
    isGameFrameVisible = False
    isScoreFrameVisible = False



    # 유효한(뒷면으로 돌려진) 트럼프 카드를 클릭한 횟수
    count = 0

    # 게임하는 데 걸린 시간을 재기 위한 count_time 변수 : count_time == 1일 때, 시작 시간을 구함 => count_time은 트럼프카드를 클릭할 때마다 1씩 증가
    count_time = 0

    while run:
        # 루프 종료 조건
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # 마우스로 버튼을 클릭하면, 프레임 전환
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 시작 화면에 있는 버튼
                if isStartFrameVisible == True: # 현재 프레임이 시작 화면이라면 if문 실행
                    if START_RECT.collidepoint(event.pos):  # 게임 화면으로 연결되는 시작 버튼
                        frame_start.hide() # 시작 화면 숨김
                        frame_game.show() # 게임 화면 보여줌
                        isStartFrameVisible = False # 현재 시작 화면의 상태
                        isGameFrameVisible = True # 현재 게임 화면의 상태

                        # 3. 게임 화면 -  트럼프 카드 앞면 12개: 시작 버튼을 눌렀을 때, 트럼프 카드가 랜덤하게 화면에 보이도록 함.
                        image_card1 = pygame.image.load("트럼프카드1.png")
                        image_card1 = pygame.transform.scale(image_card1, (100, 150))

                        CARD_RECT1 = pygame.Rect(lst[0][0], lst[0][1], 100, 150)

                        card1 = pygame_gui.elements.UIImage(
                            relative_rect=CARD_RECT1, manager=MANAGER, image_surface=image_card1, container=frame_game
                        )

                        CARD_RECT2 = pygame.Rect(lst[1][0], lst[1][1], 100, 150)

                        card2 = pygame_gui.elements.UIImage(
                            relative_rect=CARD_RECT2, manager=MANAGER, image_surface=image_card1, container=frame_game
                        )

                        image_card2 = pygame.image.load("트럼프카드2.png")
                        image_card2 = pygame.transform.scale(image_card2, (100, 150))

                        CARD_RECT3 = pygame.Rect(lst[2][0], lst[2][1], 100, 150)

                        card3 = pygame_gui.elements.UIImage(
                            relative_rect=CARD_RECT3, manager=MANAGER, image_surface=image_card2, container=frame_game
                        )

                        CARD_RECT4 = pygame.Rect(lst[3][0], lst[3][1], 100, 150)

                        card4 = pygame_gui.elements.UIImage(
                            relative_rect=CARD_RECT4, manager=MANAGER, image_surface=image_card2, container=frame_game
                        )

                        image_card3 = pygame.image.load("트럼프카드3.png")
                        image_card3 = pygame.transform.scale(image_card3, (100, 150))

                        CARD_RECT5 = pygame.Rect(lst[4][0], lst[4][1], 100, 150)

                        card5 = pygame_gui.elements.UIImage(
                            relative_rect=CARD_RECT5, manager=MANAGER, image_surface=image_card3, container=frame_game
                        )

                        CARD_RECT6 = pygame.Rect(lst[5][0], lst[5][1], 100, 150)

                        card6 = pygame_gui.elements.UIImage(
                            relative_rect=CARD_RECT6, manager=MANAGER, image_surface=image_card3, container=frame_game
                        )

                        image_card4 = pygame.image.load("트럼프카드4.png")
                        image_card4 = pygame.transform.scale(image_card4, (100, 150))

                        CARD_RECT7 = pygame.Rect(lst[6][0], lst[6][1], 100, 150)

                        card7 = pygame_gui.elements.UIImage(
                            relative_rect=CARD_RECT7, manager=MANAGER, image_surface=image_card4, container=frame_game
                        )

                        CARD_RECT8 = pygame.Rect(lst[7][0], lst[7][1], 100, 150)

                        card8 = pygame_gui.elements.UIImage(
                            relative_rect=CARD_RECT8, manager=MANAGER, image_surface=image_card4, container=frame_game
                        )

                        image_card5 = pygame.image.load("트럼프카드5.png")
                        image_card5 = pygame.transform.scale(image_card5, (100, 150))

                        CARD_RECT9 = pygame.Rect(lst[8][0], lst[8][1], 100, 150)

                        card9 = pygame_gui.elements.UIImage(
                            relative_rect=CARD_RECT9, manager=MANAGER, image_surface=image_card5, container=frame_game
                        )

                        CARD_RECT10 = pygame.Rect(lst[9][0], lst[9][1], 100, 150)

                        card10 = pygame_gui.elements.UIImage(
                            relative_rect=CARD_RECT10, manager=MANAGER, image_surface=image_card5, container=frame_game
                        )

                        image_card6 = pygame.image.load("트럼프카드6.png")
                        image_card6 = pygame.transform.scale(image_card6, (100, 150))

                        CARD_RECT11 = pygame.Rect(lst[10][0], lst[10][1], 100, 150)

                        card11 = pygame_gui.elements.UIImage(
                            relative_rect=CARD_RECT11, manager=MANAGER, image_surface=image_card6, container=frame_game
                        )

                        CARD_RECT12 = pygame.Rect(lst[11][0], lst[11][1], 100, 150)

                        card12 = pygame_gui.elements.UIImage(
                            relative_rect=CARD_RECT12, manager=MANAGER, image_surface=image_card6, container=frame_game
                        )

                        # 트럼프 카드 앞면 숨기기
                        card1.hide()
                        card2.hide()
                        card3.hide()
                        card4.hide()
                        card5.hide()
                        card6.hide()
                        card7.hide()
                        card8.hide()
                        card9.hide()
                        card10.hide()
                        card11.hide()
                        card12.hide()

                        # 3. 게임 화면 - 트럼프 카드 뒷면 12개
                        image_card = pygame.image.load("트럼프카드.png")
                        image_card = pygame.transform.scale(image_card, (100, 150))

                        card1_back = pygame_gui.elements.UIImage(
                            relative_rect=CARD_RECT1, manager=MANAGER, image_surface=image_card, container=frame_game
                        )

                        card2_back = pygame_gui.elements.UIImage(
                            relative_rect=CARD_RECT2, manager=MANAGER, image_surface=image_card, container=frame_game
                        )

                        card3_back = pygame_gui.elements.UIImage(
                            relative_rect=CARD_RECT3, manager=MANAGER, image_surface=image_card, container=frame_game
                        )

                        card4_back = pygame_gui.elements.UIImage(
                            relative_rect=CARD_RECT4, manager=MANAGER, image_surface=image_card, container=frame_game
                        )

                        card5_back = pygame_gui.elements.UIImage(
                            relative_rect=CARD_RECT5, manager=MANAGER, image_surface=image_card, container=frame_game
                        )

                        card6_back = pygame_gui.elements.UIImage(
                            relative_rect=CARD_RECT6, manager=MANAGER, image_surface=image_card, container=frame_game
                        )

                        card7_back = pygame_gui.elements.UIImage(
                            relative_rect=CARD_RECT7, manager=MANAGER, image_surface=image_card, container=frame_game
                        )

                        card8_back = pygame_gui.elements.UIImage(
                            relative_rect=CARD_RECT8, manager=MANAGER, image_surface=image_card, container=frame_game
                        )

                        card9_back = pygame_gui.elements.UIImage(
                            relative_rect=CARD_RECT9, manager=MANAGER, image_surface=image_card, container=frame_game
                        )

                        card10_back = pygame_gui.elements.UIImage(
                            relative_rect=CARD_RECT10, manager=MANAGER, image_surface=image_card, container=frame_game
                        )

                        card11_back = pygame_gui.elements.UIImage(
                            relative_rect=CARD_RECT11, manager=MANAGER, image_surface=image_card, container=frame_game
                        )

                        card12_back = pygame_gui.elements.UIImage(
                            relative_rect=CARD_RECT12, manager=MANAGER, image_surface=image_card, container=frame_game
                        )

                        # 현재 카드의 상태(앞면인지 뒷면인지)를 알려주는 부울형 변수
                        isCard1Visible = False
                        isCard2Visible = False
                        isCard3Visible = False
                        isCard4Visible = False
                        isCard5Visible = False
                        isCard6Visible = False
                        isCard7Visible = False
                        isCard8Visible = False
                        isCard9Visible = False
                        isCard10Visible = False
                        isCard11Visible = False
                        isCard12Visible = False

                        isCard1BackVisible = True
                        isCard2BackVisible = True
                        isCard3BackVisible = True
                        isCard4BackVisible = True
                        isCard5BackVisible = True
                        isCard6BackVisible = True
                        isCard7BackVisible = True
                        isCard8BackVisible = True
                        isCard9BackVisible = True
                        isCard10BackVisible = True
                        isCard11BackVisible = True
                        isCard12BackVisible = True

                    elif BUTTON_TUTORIAL_RECT.collidepoint(event.pos):  # 튜토리얼 화면으로 연결되는 튜토리얼 버튼
                        frame_start.hide()
                        frame_tutorial.show()
                        isStartFrameVisible = False
                        isTutorialFrameVisible = True
                    elif BUTTON_NICKNAME_RECT.collidepoint(event.pos):  # 닉네임을 입력할 수 있는 엔트리와 연결되는 닉네임 입력 버튼
                        entry_nickname.show()



                # 튜토리얼 화면에 있는 버튼
                elif isTutorialFrameVisible == True:
                    if HOME_RECT.collidepoint(event.pos):  # 홈 화면과 연결되는 홈 버튼
                        frame_tutorial.hide()
                        frame_start.show()
                        entry_nickname.hide()
                        isTutorialFrameVisible = False
                        isStartFrameVisible = True



                # 게임 화면에 있는 버튼
                elif isGameFrameVisible == True:
                    if count_time == 0: #count_time이 1일 경우
                        start = time.time() # 시작 시간을 구함
                    if count < 2: # 유효한 트럼프 카드를 2장 미만을 선택한 경우
                        if CARD_RECT1.collidepoint(event.pos): #1번 카드 클릭하면 if문 실행
                            if isCard1BackVisible: # 1번 카드가 뒷면으로 돌려진 상태라면 if문 실행
                                card1_back.hide() # 1번 카드 뒷면을 숨김
                                card1.show() # 1번 카드 앞면을 보여줌
                                isCard1BackVisible = False # 현재 1번 카드 뒷면의 상태
                                isCard1Visible = True # 현재 1번 카드 앞면의 상태
                                count += 1 # count 변수에 1을 더함
                        elif CARD_RECT2.collidepoint(event.pos):
                            if isCard2BackVisible:
                                card2_back.hide()
                                card2.show()
                                isCard2BackVisible = False
                                isCard2Visible = True
                                count += 1
                        elif CARD_RECT3.collidepoint(event.pos):
                            if isCard3BackVisible:
                                card3_back.hide()
                                card3.show()
                                isCard3BackVisible = False
                                isCard3Visible = True
                                count += 1
                        elif CARD_RECT4.collidepoint(event.pos):
                            if isCard4BackVisible:
                                card4_back.hide()
                                card4.show()
                                isCard4BackVisible = False
                                isCard4Visible = True
                                count += 1
                        elif CARD_RECT5.collidepoint(event.pos):
                            if isCard5BackVisible:
                                card5_back.hide()
                                card5.show()
                                isCard5BackVisible = False
                                isCard5Visible = True
                                count += 1
                        elif CARD_RECT6.collidepoint(event.pos):
                            if isCard6BackVisible:
                                card6_back.hide()
                                card6.show()
                                isCard6BackVisible = False
                                isCard6Visible = True
                                count += 1
                        elif CARD_RECT7.collidepoint(event.pos):
                            if isCard7BackVisible:
                                card7_back.hide()
                                card7.show()
                                isCard7BackVisible = False
                                isCard7Visible = True
                                count += 1
                        elif CARD_RECT8.collidepoint(event.pos):
                            if isCard8BackVisible:
                                card8_back.hide()
                                card8.show()
                                isCard8BackVisible = False
                                isCard8Visible = True
                                count += 1
                        elif CARD_RECT9.collidepoint(event.pos):
                            if isCard9BackVisible:
                                card9_back.hide()
                                card9.show()
                                isCard9BackVisible = False
                                isCard9Visible = True
                                count += 1
                        elif CARD_RECT10.collidepoint(event.pos):
                            if isCard10BackVisible:
                                card10_back.hide()
                                card10.show()
                                isCard10BackVisible = False
                                isCard10Visible = True
                                count += 1
                        elif CARD_RECT11.collidepoint(event.pos):
                            if isCard11BackVisible:
                                card11_back.hide()
                                card11.show()
                                isCard11BackVisible = False
                                isCard11Visible = True
                                count += 1
                        elif CARD_RECT12.collidepoint(event.pos):
                            if isCard12BackVisible:
                                card12_back.hide()
                                card12.show()
                                isCard12BackVisible = False
                                isCard12Visible = True
                                count += 1

                    elif count == 2: # 트럼프 카드를 두 장 선택했다면 if문 실행
                        count = 0 # count 변수 초기화

                        if isCard1Visible and isCard2Visible:  # 플레이어가 1번 카드와 2번 카드를 선택했다면 if문 실행
                            card1.hide()  # 1번 카드 숨김
                            card2.hide()  # 2번 카드 숨김
                            isCard1Visible = False  # 현재 1번 카드의 앞면 상태
                            isCard2Visible = False  # 현재 2번 카드의 앞면 상태
                            if score == 80:  # 만약 score가 80점이었다면 100점으로 score 업그레이드
                                score = 100
                            else:  # 그렇지 않다면 100//6점이 증가된 값으로 score 업그레이드
                                score += 100 // 6
                        elif isCard3Visible and isCard4Visible:
                            card3.hide()
                            card4.hide()
                            isCard3Visible = False
                            isCard4Visible = False
                            if score == 80:
                                score = 100
                            else:
                                score += 100 // 6
                        elif isCard5Visible and isCard6Visible:
                            card5.hide()
                            card6.hide()
                            isCard5Visible = False
                            isCard6Visible = False
                            if score == 80:
                                score = 100
                            else:
                                score += 100 // 6
                        elif isCard7Visible and isCard8Visible:
                            card7.hide()
                            card8.hide()
                            isCard7Visible = False
                            isCard8Visible = False
                            if score == 80:
                                score = 100
                            else:
                                score += 100 // 6
                        elif isCard9Visible and isCard10Visible:
                            card9.hide()
                            card10.hide()
                            isCard9Visible = False
                            isCard10Visible = False
                            if score == 80:
                                score = 100
                            else:
                                score += 100 // 6
                        elif isCard11Visible and isCard12Visible:
                            card11.hide()
                            card12.hide()
                            isCard11Visible = False
                            isCard12Visible = False
                            if score == 80:
                                score = 100
                            else:
                                score += 100 // 6

                        else:  # 서로 다른 그림이 그려진 트럼프 카드를 선택한 경우 if문 실행
                            if isCard1Visible:  # 플레이어가 1번 카드를 선택한 경우
                                card1.hide()  # 1번 카드의 앞면 숨김
                                card1_back.show()  # 1번 카드의 뒷면 보여줌
                                isCard1Visible = False  # 현재 1번 카드의 앞면 상태
                                isCard1BackVisible = True  # 현재 1번 카드의 뒷면 상태
                            if isCard2Visible:
                                card2.hide()
                                card2_back.show()
                                isCard2Visible = False
                                isCard2BackVisible = True
                            if isCard3Visible:
                                card3.hide()
                                card3_back.show()
                                isCard3Visible = False
                                isCard3BackVisible = True
                            if isCard4Visible:
                                card4.hide()
                                card4_back.show()
                                isCard4Visible = False
                                isCard4BackVisible = True
                            if isCard5Visible:
                                card5.hide()
                                card5_back.show()
                                isCard5Visible = False
                                isCard5BackVisible = True
                            if isCard6Visible:
                                card6.hide()
                                card6_back.show()
                                isCard6Visible = False
                                isCard6BackVisible = True
                            if isCard7Visible:
                                card7.hide()
                                card7_back.show()
                                isCard7Visible = False
                                isCard7BackVisible = True
                            if isCard8Visible:
                                card8.hide()
                                card8_back.show()
                                isCard8Visible = False
                                isCard8BackVisible = True
                            if isCard9Visible:
                                card9.hide()
                                card9_back.show()
                                isCard9Visible = False
                                isCard9BackVisible = True
                            if isCard9Visible:
                                card9.hide()
                                card9_back.show()
                                isCard9Visible = False
                                isCard9BackVisible = True
                            if isCard10Visible:
                                card10.hide()
                                card10_back.show()
                                isCard10Visible = False
                                isCard10BackVisible = True
                            if isCard11Visible:
                                card11.hide()
                                card11_back.show()
                                isCard11Visible = False
                                isCard11BackVisible = True
                            if isCard12Visible:
                                card12.hide()
                                card12_back.show()
                                isCard12Visible = False
                                isCard12BackVisible = True



                        # 게임 화면 속 점수판 업그레이드
                        checkScore()

                        # count_time 변수 1씩 증가
                        count_time += 1

                    if (isCard1Visible==False) and (isCard2Visible==False) and (isCard3Visible==False) and (isCard4Visible==False) and (isCard5Visible==False) and (isCard6Visible==False) and (isCard7Visible==False) and (isCard8Visible==False) and (isCard9Visible==False) and (isCard10Visible==False) and (isCard11Visible==False) and (isCard12Visible==False):
                        if (isCard1BackVisible==False) and (isCard2BackVisible==False) and (isCard3BackVisible==False) and (isCard4BackVisible==False) and (isCard5BackVisible==False) and (isCard6BackVisible==False) and (isCard7BackVisible==False) and (isCard8BackVisible==False) and (isCard9BackVisible==False) and (isCard10BackVisible==False) and (isCard11BackVisible==False) and (isCard12BackVisible==False):
                            end = time.time()  # 종료 시간을 구함
                            time_game = int(end - start)  # 종료 시간 - 시작 시간

                            # 게임하는 데 걸린 시간에 따라 점수 차등 부여
                            if time_game <= 13:
                                score_final = "A"
                            elif time_game <= 25:
                                score_final = "B"
                            else:
                                score_final = "C"
                            frame_game.hide()
                            frame_score.show()
                            isGameFrameVisible = False
                            isScoreFrameVisible = True

                            # 점수 화면 속 점수판(최종 점수판) 업그레이드
                            scoreboard()

                            # 점수판 프레임 생성
                            FRAME_SCOREBOARD_RECT = pygame.Rect(30, 30, 700, 700)

                            frame_scoreboard = pygame_gui.elements.UIPanel(
                                relative_rect=FRAME_SCOREBOARD_RECT, manager=MANAGER, container=frame_score
                            )

                            # 점수판 프레임의 배경색을 검정으로 지정
                            bg_black = pygame.transform.scale(bg_black, (700, 700))

                            frame_scoreboard_bg = pygame_gui.elements.UIImage(
                                relative_rect=FRAME_SCOREBOARD_RECT, manager=MANAGER, container=frame_score,
                                image_surface=bg_black
                            )

                            # 점수판 이미지를 점수판 프레임에 붙임
                            image_scoreboard = pygame.image.load("scoreboard.png")
                            image_scoreboard = pygame.transform.scale(image_scoreboard, (700, 700))

                            IMAGE_SCOREBOARD_RECT = pygame.Rect(0, 0, 700, 700)

                            _scoreboard = pygame_gui.elements.UIImage(
                                relative_rect=IMAGE_SCOREBOARD_RECT, manager=MANAGER, container=frame_scoreboard,
                                image_surface=image_scoreboard
                            )

                            # "점수판" 라벨 생성
                            image_score_title = pygame.image.load("label_scoreboard.png")  # "점수판"이 적힌 이미지 불러옴
                            image_score_title = pygame.transform.scale(image_score_title, (200, 100))

                            SCORE_TITLE_RECT = pygame.Rect(250, 60, 200, 100)

                            label_score_title = pygame_gui.elements.UIImage(
                                relative_rect=SCORE_TITLE_RECT, manager=MANAGER, container=frame_scoreboard,
                                image_surface=image_score_title
                            )

                            # 점수판에 순위를 기록하는 함수
                            with open("score.txt", "r", encoding="utf-8") as file:
                                lines = file.readlines()

                                height = 200
                                for line in lines:
                                    text = line

                                    html_text = f"<b><font color='#FFFFFF' size=6>{text}</font></b>"  # UITextBox에 들어가는 텍스트의 폰트 지정

                                    SCORE_RECT2 = pygame.Rect(100, height, 500, 50)

                                    text_box = pygame_gui.elements.UITextBox(html_text=html_text,
                                                                             relative_rect=SCORE_RECT2,
                                                                             manager=MANAGER,
                                                                             container=frame_scoreboard)
                                    height += 50

                # 점수 화면에 있는 버튼
                elif isScoreFrameVisible == True:
                    if RESTART_RECT.collidepoint(event.pos): # 다시 시작 버튼을 클릭한 경우 if문 실행
                        frame_scoreboard.kill()  # 점수판 프레임 삭제
                        entry_nickname.kill() # 닉네임 입력칸 삭제

                        # 트럼프 카드의 앞/ 뒷면 삭제: 플레이어가 다시 시작 버튼을 눌렀을 때, 카드를 랜덤으로 재배열하기 위함
                        card1.kill()
                        card2.kill()
                        card3.kill()
                        card4.kill()
                        card5.kill()
                        card6.kill()
                        card7.kill()
                        card8.kill()
                        card9.kill()
                        card10.kill()
                        card11.kill()
                        card12.kill()

                        card1_back.kill()
                        card2_back.kill()
                        card3_back.kill()
                        card4_back.kill()
                        card5_back.kill()
                        card6_back.kill()
                        card7_back.kill()
                        card8_back.kill()
                        card9_back.kill()
                        card10_back.kill()
                        card11_back.kill()
                        card12_back.kill()

                        frame_score.hide() # 점수 화면 숨김
                        frame_start.show() # 시작 화면 보여줌
                        isScoreFrameVisible = False # 현재 점수 화면 상태
                        isStartFrameVisible = True # 현재 시작 화면 상태

                        score = 0 # 점수 초기화
                        count_time = 0 # 시작 시간과 종료 시간을 구하기 위해 꼭 필요한 count_time 변수 초기화

                        checkScore() # 초기화된 점수를 바탕으로 게임 화면의 점수판 업그레이드

                        random.shuffle(lst) # 트럼프 카드의 위치 리스트를 무작위로 섞음

                        # 닉네임 입력칸 생성
                        entry_nickname = pygame_gui.elements.UITextEntryLine(
                            relative_rect=ENTRY_NICKNAME_RECT, manager=MANAGER, container=frame_start)
                        entry_nickname.hide() # 닉네임 입력칸 숨기기

                    elif RESET_RECT.collidepoint(event.pos): # 리셋 버튼을 클릭한 경우
                        scorefile = open("score.txt", 'w')
                        scorefile.truncate(0)  # 내용 지우기
                        scorefile.close()
                        try:
                            frame_scoreboard.kill() # 점수판 프레임 삭제
                        except UnboundLocalError:
                            pass
                        # 점수판 프레임 생성
                        FRAME_SCOREBOARD_RECT = pygame.Rect(30, 30, 700, 700)

                        frame_scoreboard = pygame_gui.elements.UIPanel(
                            relative_rect=FRAME_SCOREBOARD_RECT, manager=MANAGER, container=frame_score
                        )

                        # 점수판 프레임의 배경색을 검정으로 지정
                        bg_black = pygame.transform.scale(bg_black, (700, 700))

                        frame_scoreboard_bg = pygame_gui.elements.UIImage(
                            relative_rect=FRAME_SCOREBOARD_RECT, manager=MANAGER, container=frame_score,
                            image_surface=bg_black
                        )

                        # 점수판 이미지를 점수판 프레임에 붙임
                        image_scoreboard = pygame.image.load("scoreboard.png")
                        image_scoreboard = pygame.transform.scale(image_scoreboard, (700, 700))

                        IMAGE_SCOREBOARD_RECT = pygame.Rect(0, 0, 700, 700)

                        _scoreboard = pygame_gui.elements.UIImage(
                            relative_rect=IMAGE_SCOREBOARD_RECT, manager=MANAGER, container=frame_scoreboard,
                            image_surface=image_scoreboard
                        )

                        # "점수판" 라벨 생성
                        image_score_title = pygame.image.load("label_scoreboard.png")  # "점수판"이 적힌 이미지 불러옴
                        image_score_title = pygame.transform.scale(image_score_title, (200, 100))

                        SCORE_TITLE_RECT = pygame.Rect(250, 60, 200, 100)

                        label_score_title = pygame_gui.elements.UIImage(
                            relative_rect=SCORE_TITLE_RECT, manager=MANAGER, container=frame_scoreboard,
                            image_surface=image_score_title
                        )


            # 닉네임을 입력하고 엔터를 누른 경우
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    entry_nickname.hide() # 닉네임 입력칸 숨김
                    username = entry_nickname.text # username에 사용자가 입력한 텍스트 할당
                    pygame.display.set_caption(f"Welcome {username}!!") # 윈도우 창 이름 다시 지정

            MANAGER.process_events(event)

            MANAGER.update(1 / 60)
            MANAGER.draw_ui(SCREEN)

            # 디스플레이 업데이트
            pygame.display.update()

main()

# 게임 종료
pygame.quit()