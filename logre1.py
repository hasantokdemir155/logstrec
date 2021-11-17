from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

class logres():
    def __init__(self):
        self.veri3=pd.read_csv('rrrr.csv',sep=',')
#print(veri3)
        self.vr3=pd.DataFrame(self.veri3)
        print('tttttt')


    def algtanm(self):
        
        self.lgr= LogisticRegression()
    def verdnsm(self):
        
        self.x1=self.vr3.drop('Purchased',axis=1)
        
        self.lb= LabelEncoder()
        self.vf= self.vr3
        self.vf.Purchased=self.lb.fit_transform(self.vf.Purchased)
        self.y1=self.vf.Purchased

    def logsttahmn(self):
        
        self.x_train,self.x_test,self.y_train,self.y_test=train_test_split(self.x1,self.y1,test_size=0.2,shuffle=True,random_state=123)
        self.lgr.fit(self.x_train,self.y_train)


        self.m=self.lgr.predict(self.x_test)
        

        print(self.m)
        


veri3=pd.read_csv('rrrr.csv',sep=',')

vr3=pd.DataFrame(veri3)
lgr= LogisticRegression()

lb= LabelEncoder()
vf= vr3
vf.Gender=lb.fit_transform(vf.Gender)
      
y1=vf.Purchased




x1=vf.drop('Purchased',axis=1)

       


x_train,x_test,y_train,y_test=train_test_split(x1,y1,test_size=0.2,shuffle=True,random_state=123)
lgr.fit(x_train,y_train)

m=lgr.predict(x_test)
print(m)













