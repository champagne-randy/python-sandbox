import numpy as np
from timeit import default_timer as timer
from numba import vectorize, cuda


def VectorAdd(a, b, c):
    for i in range(a.size):
        c[i] = a[i] + b[i]

@vectorize(['float32(float32, float32)'], target='parallel')
def ScalarAdd(a,b):
    return a + b


def main():
    N = 32000000       # Number of elements per array


    ## Pure python
    A = np.ones(N, dtype=np.float32)
    B = np.ones(N, dtype=np.float32)
    C = np.zeros(N, dtype=np.float32)

    start = timer()
    VectorAdd(A, B, C)
    vectoradd_time = timer() - start

    print("C[:5] = ", str(C[:5]))
    print("C[-5:] = ", str(C[-5:]))

    print("VectorAdd took for %f seconds" % vectoradd_time)



    ## Accelerated python
    A = np.ones(N, dtype=np.float32)
    B = np.ones(N, dtype=np.float32)
    C = np.zeros(N, dtype=np.float32)

    start = timer()
    C = ScalarAdd(A,B)
    scalaradd_time = timer() - start

    print("C[:5] = ", str(C[:5]))
    print("C[-5:] = ", str(C[-5:]))

    print("ScalarAdd took for %f seconds" % scalaradd_time)




if __name__=='__main__':
    main()
    #cuda.profile_stop()