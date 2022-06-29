from multiprocessing import Pool
import time
def f(n):
    return n*n
if __name__ == "__main__" :
    t1 =  time.time ( )
    P = Pool ( )
    a=[5,6,7,8]
    result = P.map(f, a)

    P.close()
    P.join()
    print(sum(result))