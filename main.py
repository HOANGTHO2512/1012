from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "service": "Wordle API",
        "status": "running"
    }


@app.get("/health")
def health():
    return {"ok": True}

@app.get("/newRound")
def newRound():
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