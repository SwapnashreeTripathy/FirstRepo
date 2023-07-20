import pandas

# Create DataFrame
import pandas as pd

def getitems():
    data_frame= pd.read_csv('user.csv') #reas_csv will read from my CSV file
    # print(type(file))   # <class 'pandas.core.frame.DataFrame'>
    
    # df=pd.DataFrame(file) 

    # # dict=df.to_dict(file)

    # print (df)

    data_dict=data_frame.to_dict()
    

    
   

   
    # return my_dict
print(getitems())


