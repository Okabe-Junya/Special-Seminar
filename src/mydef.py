from random import randint
import gurobipy as grb
import pickle


node_num = 10  # node の数
INF = 10**9

def init_list(n):  # n × n の対称行列を乱数で作成
    res = [[0 for _ in range(n)] for _ in range(n)]
    for index in range(n):
        for col in range(n):
            if index > col:
                continue
            tmp = randint(1, 10)
            res[index][col] = tmp
            res[col][index] = tmp
    return res

def check_through_hub(i, j, k, m, q=3):
    c_hub = solve_c_ijkm(c, alpha, i, j, k, m)
    if h[i][j] > q and h[j][i] > q and c[i][j] < c_hub:
        return False
    else:
        return True


def solve_c_ijkm(c, alpha, i, j, k, m):
    cost = c[i][k] + alpha * c[k][m] + c[m][j]
    return cost

# input ---
# i -> j への需要
h = [[randint(1, 10) * 10 if i != j else 0 for i in range(node_num)]
     for j in range(node_num)]
# i -> j へのコスト
c = init_list(node_num)
# i -> j への距離
d = init_list(node_num)
# ディスカウントファクター
alpha = 0.6

model = grb.Model("my_def")

# --- 変数の設定 ---
# ハブか否かを表す変数（ハブ: 1, 非ハブ: 0）
x = [
    model.addVar(
        vtype=grb.GRB.BINARY,
        name="x[{}]".format(i),
    ) for i in range(node_num)
]

# ハブ k, m を経由する i -> j へのフロー
z_ijkm = [[[[
    model.addVar(
        vtype=grb.GRB.BINARY,
        name="z[{}][{}][{}][{}]".format(i, j, k, m),
    ) for m in range(node_num)
]for k in range(node_num)] for j in range(node_num)] for i in range(node_num)]

# 非ハブ間でノードを作成するかの判定
z_ij_tmp2 = []
z_ij_index = [[False for _ in range(node_num)] for _ in range(node_num)]
for i in range(node_num):
    tmp_list = []
    for j in range(node_num):
        if i == j:
            continue
        tmp = []
        for k in range(node_num):
            for m in range(node_num):
                tmp.append(solve_c_ijkm(c, alpha, i, j, k, m))
        if c[i][j] < min(tmp) and h[i][j] > 90 and h[j][i] > 90:
            tmp_list.append((i, j))
            z_ij_tmp2.append((i, j))
            z_ij_index[i][j] = True
        else:
            tmp_list.append(False)
            
z_ij = [[
    model.addVar(
        vtype=grb.GRB.BINARY,
        name="z[{}][{}]".format(i, j),
    )for i, j in z_ij_tmp2
]]
# --- 制約条件 ---
# ハブの数が3つなる制約
model.addConstr(sum(x) == 3)

# 各 i, j に対してフローの和が1になる制約
for i in range(node_num):
    for j in range(node_num):
        tmp = 0
        if z_ij_index[i][j]:
            #print("z_ij_index[{}][{}]".format(i, j))
            tmp = 1
        model.addConstr(sum(z_ijkm[i][j][k][m] for k in range(
            node_num) for m in range(node_num)) + tmp == 1)

# --- 目的関数 ---
model.setObjective(
    grb.quicksum((solve_c_ijkm(c, alpha, i, j, k, m) * h[i][j] * z_ijkm[i][j][k][m] for i in range(node_num)
                 for j in range(node_num) for k in range(node_num) for m in range(node_num))) + 
    grb.quicksum(c[i][j] * h[i][j] if z_ij_index[i][j] else 0 for i in range(node_num) for j in range(node_num)),
    grb.GRB.MINIMIZE
)

# --- 最適化の実行
model.optimize()

print("Opt, Value =", model.ObjVal)

txt = ""
for v in model.getVars():
    # print(v.varName, v.x)
    if v.x == 1:
        txt += str(v.varName) + "\n"

with open("./res/result.txt", "w") as f:
    f.write(txt)

pickle.dump(z_ij_tmp2, open("./res/result_nonhub.pkl", "wb"))