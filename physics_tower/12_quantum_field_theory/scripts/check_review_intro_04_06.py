"""導入再レビューの代表的な計算を確認する。"""
import math
import numpy as np

def close(a,b):
    np.testing.assert_allclose(a,b,rtol=1e-10,atol=1e-10)

U=np.array([[1,1],[1,-1]])/math.sqrt(2)
close(U@U,np.eye(2))
close([U[1,0]*U[0,0],U[1,1]*U[1,0]],[.5,-.5])
for x,S in [(.25,.625),(.5,.5)]:
    close(.5*((x/.5)**2/2+((1-x)/.5)**2/2),S)
P=np.eye(4)[[0,2,1,3]]
close(P@P,np.eye(4))
plus=(np.eye(4)+P)/2
minus=(np.eye(4)-P)/2
close(plus@plus,plus)
close(plus@minus,np.zeros((4,4)))
close(np.linalg.matrix_rank(plus),3)
close(np.linalg.matrix_rank(minus),1)
close(math.comb(4,2),6)
close(sum(1 for i in range(3) for j in range(3) for k in range(3) if i+j+k==2),6)
close(np.array([5,3])@np.diag([1,-1])@np.array([2,1]),7)
beta=.6
gamma=1/math.sqrt(1-beta*beta)
close(gamma*np.array([[1,-beta],[-beta,1]])@np.array([5,3]),[4,0])
close(gamma*beta**2+1/gamma,gamma)
print("introductory review chapters 04-06: checks OK")
