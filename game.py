import pygame
import sys
# 1.初始化 Pygame 引擎
pygame.init()
# 2.建⽴ 600x600 像素的遊戲視窗
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("闕河正講師 — Pygame 基礎教學")
# 3.遊戲主迴圈 (Game Loop)
while True:
    #監聽使⽤者事件（例如點擊關閉視窗）
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
#填滿背景底⾊ (RGB:暖⽶⽩ 245, 240, 230)
    screen.fill((245, 240, 230))
    pygame.display.flip()