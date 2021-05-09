import bar
import cosine
import line
import log
import PieChart
import sine
import scatter



def options():
    print('Choose the type of graph which you want to plot \n')
    print('1. Line Graph\n')
    print('2. Bar Graph\n')
    print('3. Pie Chart\n')
    print('4. Scatter Graph\n')
    print('5. Sine Wave\n')
    print('6. Cosine Wave\n')
    print('7. Natural Log Graph\n')
    print('8. Exit\n')
    a = input()
    return a

print('Hello this is a program build to plot different graphs.\n')

while True:
    a=options()
    if (a == "Line Graph" or a == "1"):
        line.LineGraph()
    elif (a == "Bar Graph" or a == "2"):
        bar.BarGraph()
    elif (a == "Pie Chart" or a == "3"):
        PieChart.Pie()
    elif (a == "Scatter Graph" or a == "4"):
        scatter.scatter()
    elif (a == "Sine Wave" or a == "5"):
        sine.sin()
    elif (a == "Cosine Wave" or a == "6"):
        cosine.cos()
    elif (a == "Natural Log Graph" or a == "7"):
        log.log1()
    elif (a == "Exit" or a == "8"):
        exit()
    else:
        print("Choose a valid Option!!")
        continue
            

