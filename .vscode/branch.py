class matrix :
    def __init__ (self, n, m, disabled_load) :
        self.n = n+1
        self.m = m+1
        self.matrix = [[0 for col in range(self.m)]for row in range(self.n)]
        self.disabled_load = disabled_load

    def value(self, y, x) :
        if (y<0) :
            y=0
        if (x<0) :
            x=0
        return self.matrix[y][x]

    def add (self, y, x) :
        if (y==0 and x==0) :
            self.matrix[y][x]=1
            return self.matrix[y][x]

        down = self.value(y-1, x) 
        left = self.value(y, x-1)

        if (self.is_d(y, x)=='row') :
            down=0
        if (self.is_d(y, x)=='col') :
            left=0
        self.matrix[y][x]=down + left
        return self.matrix[y][x]

    def is_d(self, y, x) :
        key = f'{y},{x}'
        try :
            value = self.disabled_load[key]
        except KeyError:
            value = 0
        return value

    def destination(self) :
        for row in range(self.n) :
            for col in range(self.m) :
                self.add(row, col)
        return self.value(self.n-1, self.m-1)

import sys
if __name__ == "__main__" :
    n, m = map(int, sys.stdin.readline().split())
    disable_num =  int(sys.stdin.readline())
    

    d_row_li = []
    d_col_li = []

    for _ in range(disable_num) :
        y1, x1, y2, x2 = map(int, sys.stdin.readline().split())
        if (x1==x2) :
            if (y2>y1) :
                d_row_li.append(f'{y2},{x2}') #뒷 친구가 더 크다는 가정
            else :
                d_row_li.append(f'{y1},{x1}')
        else : # (y1==y2)
            if (x2>x1) :
                d_col_li.append(f'{y2},{x2}')
            else :
                d_col_li.append(f'{y1},{x1}')

    if len(d_row_li) != 0 : 
        d_row = {d_row:'row' for d_row in d_row_li}
    else :
        d_row = dict()
    if len(d_col_li) != 0 :
        d_col = {d_col:'col' for d_col in d_col_li}
    else :
        d_col = dict()

    dis = dict(d_row, **d_col)
    answer = matrix(n, m, dis)
    print(answer.destination())


    