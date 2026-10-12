import pygame, sys
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Step 2 - ⽂字渲染")
#設定字型: SysFont( 字型名稱, 字級⼤⼩, bold= 粗體)
font_title = pygame.font.SysFont("Arial", 32, bold=True)
font_hint = pygame.font.SysFont("SimHei", 20) # SimHei 為⿊體，⽀援中⽂
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((245, 240, 230))
    # 1.渲染標題英⽂: render( 字串, 抗鋸⿒, RGB顏⾊)
    title_surface = font_title.render("Wordle Puzzle Game", True, (233, 91,210))
    screen.blit(title_surface, (50, 30)) # blit 貼到 (X=50, Y=30)

    # 2.渲染中⽂提⽰訊息
    hint_surface = font_hint.render("提示：與 Google 雲端服務有關的單字", True,(120,210,180))
    screen.blit(hint_surface, (50, 80))
    bottom_surface = font_hint.render("按下 [ESC] 鍵退出遊戲", False , (154,130,149),(0,0,0))
    screen.blit(bottom_surface , (50,530))
    pygame.display.flip()