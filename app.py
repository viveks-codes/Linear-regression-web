from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *
import argparse
from pywebio import start_server

import numpy as np
def lr():
	Nx=input("Please enter how many elements you want to add in X column ",type=NUMBER)
	Ny=input("Please enter how many elements you want to add in Y column ",type=NUMBER)
	while(Nx!=Ny):
		put_text("number of X elements and number of Y elements must be equal ")
		put_text("current size of X elements is X[{}]".format(Nx))
		Ny=input("Please enter how many elements you want to add in Y column ",type=NUMBER)
	X = []
	Y = []
	
	for i in range(0,Nx):
		inpx=input("Please enter X[%.f]"%(i),type=FLOAT)
		put_text("X[{}] = {}".format(i,inpx))
		X.append(inpx)
		
	for j in range(0,Ny):
		inpy=input("Please enter Y[%.f]"%(j),type=FLOAT)
		put_text("Y[{}] = {}".format(j,inpy))
		Y.append(inpy)
	
	sum1 = 0
	for i in range(len(X)):
    		sum1 += X[i]
	put_text("ΣX = {}".format(sum1))
	
	sum2 = 0
	for i in range(len(Y)):
    		sum2 += Y[i]
	put_text("ΣY = {}".format(sum2))
	
	xBar = sum1 / len(X)

	# ## Lets find ȳ (mean)

	yBar = sum2 / len(Y)
	put_text("ȳ = {}".format(yBar))

	# ## Lets Find x - x̄ For every element

	xMin_xBar = []
	for i in range(len(X)):
	    xMin_xBar.append(X[i]-xBar)  

	# ## Lets add a new column to our data frame called 'X-x̄' 

	xMin_xBar = np.array(xMin_xBar)


	# ## Lets Find Y - yBar for every element

	yMin_yBar = []
	for i in range(len(Y)):
    		yMin_yBar.append(Y[i]-yBar) 
	
	upperSum = 0
	lower = xMin_xBar * xMin_xBar
	upper = xMin_xBar * yMin_yBar
	for i in range(len(upper)):
		upperSum+=upper[i]
	put_text("Σ(x - x̅) * (Y- ȳ ) = {}".format(upperSum))
	
	
	# ## Lets Find sum of lower array[ Σ(x - x̅)^2 ]

	lowerSum = 0
	for i in range(len(lower)):
	    lowerSum+=lower[i]
	put_text("Σ(x - x̅)^2  = {}".format(lowerSum))

	# ## Lets Find β1(Coefficient)

	B1 = upperSum / lowerSum
	put_text("β1 = {}".format(B1))

	# ## Lets find β0(intercept)

	B0 = yBar - B1 * xBar
	put_text("β0 = {}".format(B0))

	# ## Let's plot our line of best fit
	
	
	# ## and Finnaly we got our forcasted value with mean
	
	# In[48]:
	
	
	yPred = B0 + B1 * xBar
	
	
	# In[49]:
	
	
	put_text("y hat is : {} ".format(yPred))
	
	
	# ## let's find R'2
	# ### it defines how well our line is fitted towards data points
	
	# ## let's find sigma X
	
	# In[40]:
	
	
	sigX = lowerSum / len(X)
	
	
	# In[41]:
	
	
	put_text("sigmaX is {}".format(sigX))
	
	
	# ## let's find sigma Y
	
	# In[42]:
	
	
	yMin_yBar = np.array(yMin_yBar)
	
	
	# In[43]:
	
	
	yMin_yBar_Sqr = yMin_yBar * yMin_yBar 
	
	
	# In[44]:
	
	
	yMin_yBar_Sqr_sum = 0
	for i in range(len(yMin_yBar_Sqr)):
	    yMin_yBar_Sqr_sum+=yMin_yBar_Sqr[i]
	yMin_yBar_Sqr_sum
	
	
	# In[45]:
	
	
	sigY = yMin_yBar_Sqr_sum * 1 / len(Y)
	
	
	# In[46]:
	
	
	put_text("sigmaY is {}".format(sigY))
	#sum1 = 0
	#for i in range(len(df['X'])):
	#	sum1 += X[i]
	#put_text("ΣX = {}".format(sum1))
	R_Square = np.square(upperSum*(1/len(X)))/(sigX * sigY)
	put_text("R^2 is {}".format(R_Square))
app = Flask(__name__)


app.add_url_rule('/tool', 'webio_view', webio_view(lr),methods=['GET', 'POST', 'OPTIONS'])
if __name__ == '__main__':
    app.run(debug=True)


