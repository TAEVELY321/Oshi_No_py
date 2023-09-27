import pygame

# pygame 초기화
pygame.init()

# 디스플레이 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# sprite 시트 이미지 로드
sprite_sheet = pygame.image.load("sailorMoon (1).png")

# 애니메이션 프레임의 크기와 좌표 계산
frame_width = sprite_sheet.get_width() # num_frames
frame_height = sprite_sheet.get_height()
frames = []
for i in range(num_frames):
    frame = sprite_sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
    frames.append(frame)

# 애니메이션 속도 설정
frame_delay = 100
clock = pygame.time.Clock()

# 애니메이션 루프
running = True
current_frame = 0
while running:
    screen.fill((255, 255, 255))

    # 현재 프레임 그리기
    screen.blit(frames[current_frame], (0, 0))

    # 다음 프레임으로 변경
    current_frame = (current_frame + 1) % num_frames

    pygame.display.flip()
    clock.tick(frame_delay)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# pygame 종료
pygame.quit()
