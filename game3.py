import pygame, sys
def get_mock_level_packet():
    return {
        "level": 1,
        # 10x10 遮罩陣列: 0 = 隱藏背景格, 1 = 玩家可填字空⽩格, 2 = 預設顯示且不
        "grid_mask": [
            [2, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 1, 1, 1, 2, 0],
            [1, 0, 0, 0, 2, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ] + [[0]*10 for _ in range(6)],

        "solution_grid": [
            ["C", "L", "O", "U", "D", "", "", "", "", ""],
            ["O", "", "", "", "O", "C", "E", "A", "N", ""],
            ["D", "", "", "", "G", "L", "O", "W", "R", "Y"],
            ["E", "", "", "", "", "", "", "", "", ""]
        ] + [[""]*10 for _ in range(6)]
    }
packet = get_mock_level_packet()
print(f"位置 (0,0) 的 Mask 碼: {packet['grid_mask'][0][0]}") 
print(f"位置 (0,0) 的預設顯示文字: {packet['solution_grid'][0][0]}")
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Step 3 - 10x10 網格陣列")
font_title = pygame.font.SysFont("Arial", 32, bold=True)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((245, 240, 230))

    for j in range(10):
        for i in range(10):
            if packet['grid_mask'][j][i] == 0:
                continue
            x = 50 + i * 50
            y = 50 + j * 50
            pygame.draw.rect(screen, (183, 212, 135), (x, y, 40, 40))
            pygame.draw.rect(screen, (20, 43, 64), (x, y, 40, 40), 2)

            if packet['grid_mask'][j][i] == 2:
                t = font_title.render(packet['solution_grid'][j][i], True, "black")
                screen.blit(t, (x + 10, y + 1))

   
   

    pygame.display.flip()