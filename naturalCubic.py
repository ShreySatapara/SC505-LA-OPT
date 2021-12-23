import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 


def generat_matrix():
  for i in  range(0,length-1) :
    matrix[i][i] = float(2 * (h[i]+h[i+1]))
  
  for i in range(0,length-2):
    matrix[i][i+1] = float(h[i+1])
    matrix[i+1][i] = float(h[i+1])

  for i in range(0,length):
    matrix[i-1][length-1] = float(y[i+1]-y[i]) * 6/ float(h[i]) - float(y[i] - y[i-1]) *6 /float(h[i-1])


def guassElimination():
  for i in range(0,length-2,1):
       for k in range(i+1,length-1,1):
           
            term=matrix[k][i]/ matrix[i][i]
            for j in range(0,length,1):
                matrix[k][j]=matrix[k][j]-term*matrix[i][j]
            
        
    
   
  for i in range(length-2,-1,-1):
        mtemp[i]=matrix[i][length-1]
        for j in range(i+1,length-1,1):
            mtemp[i]=mtemp[i]- (matrix[i][j]*mtemp[j])
        
        mtemp[i]=mtemp[i]/matrix[i][i]
    
  
def coefficientCalculation():
  for i in range(0,length):
    d[i] = float(y[i])
    b[i] = float(M[i])/2.0
    a[i] = (M[i+1] - M[i]) /(float(h[i]) *6.0)
    c[i] = (y[i+1]- y[i])/h[i] -h[i]*(2*M[i]+M[i+1]) /6.0


# x - point

# x = np.array([0,1,2,3])
# y = np.exp(x)
# data = pd.read_csv("datapoints.csv") 
# x = data['x'].to_numpy()
# print(x)
# y = data['y'].to_numpy()
# x = np.arange(0,50,2)
# y = np.sin(x)
# length of x
# x = np.array([i/10 for i in range(20) ]);
# y = np.sin(x);
# x = [1, 2,3,4];
# y = [1,5,11,8];
x = np.arange(0,100,1)
# y = np.zeros(len(x))
y = 1/(1+25*(x**2))
length = len(x) - 1

h = np.zeros(length)

for i in range(length):
    h[i] = x[i+1] - x[i]
# print(h)
a = np.zeros(length)
b = np.zeros(length)
c = np.zeros(length)
d = np.zeros(length)
M = np.zeros(length+1)
M[0] = 0
M[length] =0
mtemp = np.zeros(length-1)
print(length)
matrix = np.zeros(length*(length-1)).reshape(length-1,length)


#generat matrix
generat_matrix()
# print(matrix)

#solve the equation
guassElimination()

for i in range(1,length):
  M[i] = mtemp[i-1]
# print(M)

coefficientCalculation()
# for i in range(0,length):
#     print("S",i,"(x)","[",x[i],",",x[i+1],"] =",a[i],"*(x-",x[i],")^3+",b[i],"*(x-",x[i],")^2+",c[i],"*(x-",x[i],")+",d[i])

# for i in range(0,length):
  # print(a[i], b[i],c[i],d[i])

# X = np.array([i/10 for i in range(5*10)])
S = np.zeros(length+1)
for i in range(length):
  # for j in range():
  #  if x[i] >= float(i) and int(x[i+1]) > float(i) :
    S[i] = a[i] * ((x[i])**3) + b[i] *((x[i])**2) + c[i] * (x[i]) + d[i]
    print(S[i])
# X = np.arange(0,25,0.5)

np.delete(S,length-1)
np.delete( x,length-1)   
plt.plot(x[:30],y[:30],"o")
plt.plot(x[:30],S[:30])
# plt.show()
plt.savefig("naturalsplines.png")