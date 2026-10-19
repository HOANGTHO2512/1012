import pygame, sys

def get_mock_level_packet():
    return {
        "level": 1,
        # 10x10 網格
        # 遮罩陣列: 0 = 隱藏背景格, 1 = 玩家可填字空白格, 2 = 預設顯示且不能更動
        "grid_mask": [
        [2, 1, 1, 1, 2, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 1, 1, 1, 2, 0],
        [2, 0, 0, 0, 2, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ] + [[0]*10 for _ in range(6)], # 後面 6 行補滿 0
       
        # 10x10 解答與預設答案矩陣
        "solution_grid": [
        ["C", "L", "O", "U", "D", "", "", "", "", ""],
        ["O", "", "", "", "O", "C", "E", "A", "N", ""],
        ["D", "", "", "", "G", "L", "O", "W", "R", "Y"],
        ["E", "", "", "", "", "", "", "", "", ""]
        ] + [[""]*10 for _ in range(6)] # 後面 6 行補空字串
    }

# 取得關卡資料包
packet = get_mock_level_packet()

# 初始化玩家自己輸入的資料矩陣 (10x10，預設皆為空字串)
inputData = [["" for i in range(10)] for j in range(10)]

# 初始化 Pygame 相關設定
pygame.init()
screen = pygame.display.set_mode((600, 800)) # 建立 600x800 像素的視窗
pygame.display.set_caption("Step 3 - draw.rect 基礎語法") # 設定視窗標題
font_title = pygame.font.SysFont("Arial", 32, bold=True) # 設定字型與大小

# 記錄目前被選中（點擊）的格子座標索引 (初始為 -1 代表沒有選中)
x_idx = -1
y_idx = -1

# 遊戲主迴圈 (Main Loop)
while True:
    # 事件處理 (Event Handling)
    for event in pygame.event.get():
        # 1. 點擊視窗關閉按鈕時離開遊戲
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
           
        # 2. 滑鼠按鍵彈起事件 (用來選取格子)
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos() # 取得滑鼠點擊的視窗座標 (x, y)
           
            # 檢查點擊位置是否在格子之間的間隙空白處（每格 50px，其中 40px 是格子，10px 是間距）
            if (x - 50) % 50 > 40 or (y - 250) % 50 > 40:
                x_idx = -1
                y_idx = -1
                continue
               
            # 計算被點擊的是第幾行、第幾列的格子
            x_idx = (x - 50) // 50
            y_idx = (y - 250) // 50
           
            # 檢查是否超出 10x10 網格範圍
            if x_idx > 9 or y_idx > 9 or x_idx < 0 or y_idx < 0:
                x_idx = -1
                y_idx = -1
                continue
               
        # 3. 鍵盤按下的事件 (用來輸入文字或刪除文字)
        if event.type == pygame.KEYDOWN:
            # 確保有選中格子才做文字處理
            if x_idx != -1 and y_idx != -1:
                # 如果按下的是 Backspace (退格鍵)，清除該格子的文字
                if event.key == pygame.K_BACKSPACE:
                    inputData[y_idx][x_idx] = ""
                else:
                    # 限制必須輸入英文字母，並將其轉換成大寫後存入玩家輸入矩陣
                    if event.unicode.isalpha():
                        inputData[y_idx][x_idx] = event.unicode.upper()

    # 畫面渲染與繪製
    screen.fill((245, 240, 240)) # 填滿背景色 (淺灰粉色)
   
    # 雙層迴圈遍歷 10x10 網格進行繪製
    for i in range(10):          # i 代表列 (row / y 軸方向)
        for j in range(10):      # j 代表行 (column / x 軸方向)
           
            # 如果遮罩為 0，代表隱藏背景格，直接跳過不畫
            if packet['grid_mask'][i][j] == 0:
                continue
               
            # 繪製方格底色 (淺紫色)
            pygame.draw.rect(screen, (238, 234, 241), (50 + j * 50, 250 + 50 * i, 40, 40))
           
            # 如果當前格子被選中，框線顯示金色；否則顯示深藍色框線
            if i == y_idx and j == x_idx:
                pygame.draw.rect(screen, "#A08801", (50 + j * 50, 250 + 50 * i, 40, 40), 2)    
            else:
                pygame.draw.rect(screen, (20, 43, 64), (50 + j * 50, 250 + 50 * i, 40, 40), 2)
           
            # 根據遮罩與輸入狀態來決定要在格子內印出什麼文字
            if packet['grid_mask'][i][j] == 2:
                # 遮罩為 2 代表預設顯示的題目答案（不能更動），字體顏色為黑色
                t = font_title.render(packet['solution_grid'][i][j], True, "black")
                screen.blit(t, (50 + j * 50 + 10, 250 + 50 * i + 1))
            elif inputData[i][j] != "":
                # 如果玩家有手動輸入文字，則將玩家輸入的字顯示在格子上
                t = font_title.render(inputData[i][j], True, "black")
                screen.blit(t, (50 + j * 50 + 10, 250 + 50 * i + 1))

    # 更新畫面顯示
    pygame.display.flip()