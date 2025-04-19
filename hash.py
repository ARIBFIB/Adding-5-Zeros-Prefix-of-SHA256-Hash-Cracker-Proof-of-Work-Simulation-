import hashlib

prefix = "Haider Ali Saima 2000 Saima Ali 100 Saqib Saqib 1500 Sara Sara I am graphic designer haider ali jjddjjdsodoskdoskdoskd dsdiajdoasd asdnasodasd w rtw e sd g sd gsd gsd gs dgsdgd s gsd gs dg sd gsd gsd g s gsd g sdojaoijasiodas dasiodjasodi2 135 4534 534 3 g w gvsd  sg 35 t5 h 5h3 5h h 3 f 43 f3 rrw  sd bw rb er thh y 56 u56 5 u6  356 uv 36 5v 4 eg ge gdfhtrjeyb y jy jty burt vhe cg reqc q t34 535656 34 7364 736 7 yve tvy ytr vy hr bj ry bj  eyn yu y ur ynue 5b y v erg r cge rcqwrcnowfxejwex re rwex w w tcq 34 654 5 5757 5u yu tr h g bdfd b s bas vsd vsd v d"

i = 0

while True:
    text = f"{prefix}{i}"
    hash_result = hashlib.sha256(text.encode()).hexdigest()
    if hash_result.startswith("00000"):
        print(f"Found! Input: {text} → Hash: {hash_result}")
        break
    i += 1