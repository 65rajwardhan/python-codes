#PYTHON PROGRAM TO DRAW A LINE WITH SUITABLE LABEL
import matplotlib.pyplot as plt
X=range(1,50)
Y=[value*3 for value in X]
print("values of x")
print(*range(1,50))

print("values of y(thrice of X)")
print(Y)

#plot lines and/or markers to the axes
plt.plot(X,Y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Draw a line")
plt.show()

#############################
import matplotlib.pyplot as plt
x=[1,2,3]
y=[2,4,1]
plt.plot(x,y)

plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("show graph")
plt.show()

############################
#python program to plot two or more lines
#on same graph plot wwith suitable leagends
import matplotlib.pyplot as plt
x1=[1,2,3]
y1=[4,5,6]

#line 2 points
x2=[2,1,3]
y2=[4,5,3]

#plotting line 1 points
plt.plot(x1,y1,label="line 1")
#plot the line 2 points
plt.plot(x2,y2,label="line 2")
plt.xlabel("x axis")

#set y axis label to current axis
plt.ylabel("y axis")
plt.legend()
plt.show()

#################################
import matplotlib.pyplot as plt
x1=[10,20,30]
y1=[40,50,60]

#line 2 points
x2=[20,10,30]
y2=[40,50,30]

plt.plot(x,y)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("show graph")
plt.show()

plt.plot(x1,y1,color='blue',linewidth=3,label='line1-width3')
plt.plot(x2,y2,color='red',linewidth=4,label='line2-width4')
plt.legend()
plt.show()

##########################
import matplotlib.pyplot as plt
x1=[10,20,30]
y1=[40,50,60]

#line 2 points
x2=[20,10,30]
y2=[40,50,30]

plt.plot(x,y)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("show graph")
plt.show()

plt.plot(x1,y1,color='blue',linewidth=3,label='line1-dotted',linestyle='dotted')
plt.plot(x2,y2,color='red',linewidth=4,label='line2-dashed',linestyle='dashed')
plt.legend()
plt.show()