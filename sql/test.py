with open('C:/Users/huangxin/Downloads/LumenGame/sql/user.csv') as f:
    for name in f.read().splitlines():
        print(name)