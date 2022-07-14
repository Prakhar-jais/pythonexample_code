import matplotlib.pyplot as plt
from matplotlib import style

#how to draw a line graph representation
# i am giving input by a list
days=[1,2,3,4,5,6,7,8,9,10,11,12]
I_temperature=[13.5,24.2,25.6,30.0,32.1,15.5,12.2,10.2,35.0,29.8,23.5,38.6]
B_temperature=[12.5,26.2,20.6,30.0,39.1,11.5,10.2,10.2,38.0,21.8,23.5,30.6]
plt.plot(days,I_temperature,color="b",marker="s",linestyle="--",label="INDORE_TEMPERATUR")
plt.plot(days,B_temperature,color="k",marker="s",linestyle=":",label="BHOPAL TMPERATURE")
plt.legend(loc=4)
plt.title("INDORE TEMPERATURE")
plt.xlabel("DAYS")
plt.ylabel("TEMPERATURE")
#to make a background grid
plt.grid(color="y",linestyle="-",linewidth="1")
#to make axis start with (0,0)and setting its amx point also
plt.axis([0,12,0,40])
#now to get the output graph use .show() function
plt.show()
help(plt.plot)
