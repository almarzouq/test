import wpf

from System.Windows import Application, Window

def calculate_final_grade(mygrade, myabcenses):
    #this functions takes 2 values, grade and abcense
    #and returns the final grade after deducting
    #points from absence
    #1 points should be deducted from each 3 absence
    #if number of absences is greater than 9,
    #then function should return -1 indicating FA
    #replace this statement
    
    GRD = self.finalGradeLabel.Content
    abs = self.absBox.text.Text
        
    if abs <= 3:
        abs=0
    elif abs > 3 and abs <= 6:
        abs = 1
    elif abs > 6 and abs <= 9:
        abs = 2
    else:
        abs = -1
    
    fnl = int(GRD)- abs
    if abs ==-1:
        fnl = -1
    else:
        self.finalGradeLabel.Content = fnl 
    

def get_letter_grade(mygrade):
    #takes grade as a number and returns the letter grade
    #A: 90 to 100
    #B: 80 to less than 90
    #C: 70 to less than 80
    #D: 60 to less than 70
    #FA: if grade is -1
    #F: otherwise
    #replace this statement
    
    self.letterGradeLabel.Content =LT_GRD
    self.finalGradeLabel.Content = FNL_GRD 
   
    if FNL_GRD >= 90 and < 100:
       LT_GRD = 'A'
    elif FNL_GRD >= 80 and < 90:
       LT_GRD = 'B'
    elif FNL_GRD >= 70 and < 80:
       LT_GRD = 'C'
    elif FNL_GRD >= 60 and < 70:
       LT_GRD = 'D'
    elif FNL_GRD == -1 :
       LT_GRD = 'FA'
    else:
        LT_GRD = 'F'
        
       

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'pyfinal2.xaml')
       
    def Window_Loaded(self, sender, e):
        #for all the following collections
        #use student name as the key
        self.ids = {} #store student ids here
        self.grades = {} #store student grades here
        self.absences = {} #store student absences here
        

    def studentList_SelectionChanged(self, sender, e):
        #this function is called when an item
        #from studentList is selected
        #see exam paper for details
        
        id = self.studentList.SelectedItem
        self.idBox.text.Text = id
        n = self.nameBox.text.Text
    
        
    
    def Button1_Click(self, sender, e):
        #this function is called when
        #update button is clicked
        #see exam paper for details
        name = self.nameBox.Text
        grd = self.gradeBox.Text
        Abss = self.absBox
        self.ids.Add(ids , name)
        self.grades.Add(ids , grd )
        self.absences.Add(ids , Abss)
        self.yearLabel.Content = YEAR
        INROL = YEAR[1:3]
        inroyear = int(INROL) + 2000 
        self.yearLabel.Content = inroyear
 

if __name__ == '__main__':
	Application().Run(MyWindow())
