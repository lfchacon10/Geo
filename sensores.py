
import numpy as np
import matplotlib.pyplot as plt

X1= [120, 130, 180, 30, 10, 200, 150, 50, 150, 200]
X2= [75, 85, 190, 2, 5, 235, 240, 60, 150, 260]
X3= [60, 60, 220, 40, 25, 200, 190, 40, 110, 200]
X4= [110, 140, 150, 80, 60, 200, 160, 180, 200, 255]
X5= [30, 60, 100, 80, 40, 150, 160, 90, 230, 130]

plt.figure()
plt.subplot(2,2,1)
plt.title("Banda X1 vs X2")
plt.grid()
plt.scatter(X1,X2)

plt.subplot(2,2,2)
plt.title("Banda X1 vs X3")
plt.grid()
plt.scatter(X1,X3)

plt.subplot(2,2,3)
plt.xlabel("Banda Xl1 vs X4")
plt.grid()
plt.scatter(X1,X4)

plt.subplot(2,2,4)
plt.xlabel("Banda X1 vs X5")
plt.grid()
plt.scatter(X1,X5)

plt.figure()
plt.subplot(2,2,1)
plt.title("Banda X2 vs X1")
plt.grid()
plt.scatter(X2,X1)

plt.subplot(2,2,2)
plt.title("Banda X2 vs X3")
plt.grid()
plt.scatter(X2,X3)

plt.subplot(2,2,3)
plt.xlabel("Banda X2 vs X4")
plt.grid()
plt.scatter(X2,X4)

plt.subplot(2,2,4)
plt.xlabel("Banda X2 vs X5")
plt.grid()
plt.scatter(X2,X5)


#Parte dos 
matriz= np.array([X1,X2,X3,X4,X5])
cova = np.cov(np.transpose(matriz))
eig_vals, eig_vecs = np.linalg.eig(cova)
#mul= np.matmul(cova,eig_vecs)
print(eig_vecs)

plt.figure()
plt.title("PCA")
plt.subplot(1,2,1)
plt.scatter(X1,X2)
x= np.dot(X1,eig_vecs[:,1])
y= np.dot(X2,eig_vecs[:,0])
#x= np.dot(np.transpose(matriz),eig_vecs[:,1])
#y= np.dot(np.transpose(matriz),eig_vecs[:,0])
plt.subplot(1,2,2)
plt.scatter(x,y)
plt.show()


#p1= np.dot(np.transpose(matriz),eig_vecs[0])
#p2= np.dot(np.transpose(matriz),eig_vecs[1])
#p3= np.dot(np.transpose(matriz),eig_vecs[2])
#p4= np.dot(np.transpose(matriz),eig_vecs[3])
#p5= np.dot(np.transpose(matriz),eig_vecs[4])

plt.figure()
plt.grid()

plt.subplot(2,2,1)
plt.title("P1,P2")
plt.scatter(p1,p2)
plt.subplot(2,2,2)
plt.title("P1,P3")
plt.scatter(p1,p3)
plt.subplot(2,2,3)
plt.xlabel("P1,P4")
plt.scatter(p1,p4)
plt.subplot(2,2,4)
plt.xlabel("P1,P5")
plt.scatter(p1,p5)
plt.show()


