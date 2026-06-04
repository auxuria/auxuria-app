app.background='darkSlateGray'
# near you
app.nearYouScreen=Label("Near you:",200,120,size=16)
app.nearYouScreen.visible=False
# created phone UI
Rect(100,20,200,360, fill='white', borderWidth=4, border='black')
Circle(168,30,7)
Circle(230,30,7)
Rect(170,25,60,12,fill='black')
Circle(230,30,3,fill='grey')
Line(104,23,296,23,fill='lightGrey',lineWidth=3)
# created home page UI
auxuriaLabel = Label('AUXRUIA',200,200,size=28,bold=True,opacity=0)
sloganLabel = Label('Sustainability for Fashion',200,220,size=10,italic=True,opacity=0)
startBorder = Rect(150,250,100,30,opacity=0)
startButton = Label('Begin',200,265,size=15,fill='white',bold=True,font='montserrat',opacity=0)
# groups elements in loading screen 
loadingScreen=[auxuriaLabel,sloganLabel,startBorder,startButton]
# back button
app.backBorder=Rect(110,45,40,20,fill='lightGrey',border='black',borderWidth=1)
app.backLabel=Label('<--',130,55,size=10)
app.backGroup=Group(app.backBorder,app.backLabel)
app.backGroup.visible = False 
# added onstep function animation for homescreen
app.onHomeScreen=True
def onStep(): 
    if app.onHomeScreen:
        if auxuriaLabel.opacity<100:
            auxuriaLabel.opacity+=2
        if sloganLabel.opacity<100:
            sloganLabel.opacity+=2
        if startBorder.opacity<100:
            startBorder.opacity+=2
        if startButton.opacity<100:
            startButton.opacity+=2
def onMousePress(x,y):
    if app.backGroup.visible and app.backGroup.hits(x,y):
       # hides stuff
        app.shoesScreen.visible=False
        app.pantsScreen.visible=False
        app.shirtsScreen.visible=False
        app.jacketsScreen.visible=False
        app.nearYouScreen.visible=False
        app.backGroup.visible=False
        # brings back stuff 
        app.question.visible=True
        app.welcome.visible=True
        app.shoes.visible=True
        app.shoesLabel.visible=True
        app.pants.visible=True
        app.pantsLabel.visible=True
        app.shirts.visible=True
        app.shirtsLabel.visible=True
        app.jackets.visible=True
        app.jacketsLabel.visible=True
        return
    # button functions 
    if startButton.hits(x,y) or startBorder.hits(x,y):
        if app.onHomeScreen == True:
            goToNextScreen()
            return
    # created a checking function using hasattr() 
    if hasattr(app,'shoes') and app.shoes.hits(x,y) or app.shoesLabel.hits(x,y) and app.shoes.visible:
        hideChoicesScreen()
        app.shoesScreen.visible=True
        app.backGroup.visible=True
        
    if hasattr(app, 'pants') and app.pants.hits(x,y) or app.pantsLabel.hits(x,y) and app.pants.visible:
        hideChoicesScreen()
        app.pantsScreen.visible=True
        app.backGroup.visible=True
        
    if hasattr(app,'shirts') and app.shirts.hits(x,y) or app.shirtsLabel.hits(x,y) and app.shirts.visible:
        hideChoicesScreen()
        app.shirtsScreen.visible=True
        app.backGroup.visible=True

    if hasattr(app, 'jackets') and app.jackets.hits(x,y) or app.jacketsLabel.hits(x,y) and app.jackets.visible:
        hideChoicesScreen()
        app.jacketsScreen.visible=True
        app.backGroup.visible=True
        app.backGroup.visible=True
        
# next screen of app where you choose what you want to fix
def goToNextScreen():
    app.onHomeScreen=False
    for item in loadingScreen:
        item.opacity=0
    auxuriaLabel.opacity=0
    sloganLabel.opacity=0
    startBorder.opacity=0
    startButton.opacity=0
    app.question=Label("What piece are you up-cycling?", 200,140,size=10)
    app.welcome=Label("Welcome",200,100,size=30,bold=True)
  # creates buttons for what you're up cycling
    app.shoes=Rect(125,150,150,30,fill='lightGrey')
    app.shoesLabel=Label("Shoes",200,165)
    app.pants=Rect(125,190,150,30,fill='lightGrey')
    app.pantsLabel=Label("Pants",200,205)
    app.shirts=Rect(125,230,150,30,fill='lightGrey')
    app.shirtsLabel=Label("Shirts",200,245)
    app.jackets=Rect(125,270,150,30,fill='lightGrey')
    app.jacketsLabel=Label("Jackets",200,285)
    app.nearYouScreen.visible=False
# temporarily hides choices
def hideChoicesScreen():
    app.question.visible=False
    app.welcome.visible=False
    app.shoes.visible=False
    app.shoesLabel.visible=False
    app.pants.visible=False
    app.pantsLabel.visible=False
    app.shirts.visible=False
    app.shirtsLabel.visible=False
    app.jackets.visible=False
    app.jacketsLabel.visible=False
    app.nearYouScreen.visible=False

# shoes screen 
app.shoesTitle=Label("Near you:",200,120,size=18)
app.shoePerson1=Label("Jessica",160,160,size=20,bold=True)
app.jessicaDetails=Label("Book Now",160,180,size=10,fill='Grey')
app.shoePerson2=Label("Rimone",250,160,size=20,bold=True)
app.rimoneDetails=Label("Book Now",250,180,size=10,fill='Grey')
app.shoePerson3=Label("Lyndall",160,220,size=20,bold=True)
app.lyndallDetails=Label("Book Now",160,240,size=10,fill='Grey')
app.shoePerson4=Label("Emily",250,220,size=20,bold=True)
app.emilyDetails=Label("Book Now", 250,240, size=10, fill='Grey')
app.shoesScreen=Group(app.emilyDetails, app.lyndallDetails, app.rimoneDetails, app.jessicaDetails, app.shoesTitle,app.shoePerson1,app.shoePerson2,app.shoePerson3,app.shoePerson4)
app.shoesScreen.visible=False
# pants screen
app.pantsTitle=Label("Near you:",200,120,size=18)
app.pantsPerson1=Label("Heaven",160,160,size=20,bold=True)
app.heavenDetails=Label("Book Now",160,180,size=10,fill='Grey')
app.pantsPerson2=Label("Ethan",250,160,size=20,bold=True)
app.ethanDetails=Label("Book Now",250,180,size=10,fill='Grey')
app.pantsPerson3=Label("Olivia",160,220,size=20,bold=True)
app.oliviaDetails=Label("Book Now",160,240,size=10,fill='Grey')
app.pantsPerson4=Label("Brittany",250,220,size=20,bold=True)
app.brittanyDetails=Label("Book Now", 250,240, size=10, fill='Grey')
app.pantsScreen=Group(app.pantsTitle,app.pantsPerson1,app.pantsPerson2,app.pantsPerson3,app.pantsPerson4,app.heavenDetails,app.ethanDetails, app.oliviaDetails, app.brittanyDetails)
app.pantsScreen.visible=False
# shirts screen 
app.shirtsTitle=Label("Near you:",200,120,size=18)
app.shirtsPerson1=Label("Naomi",160,160,size=20,bold=True)
app.naomiDetails=Label("Book Now",160,180,size=10,fill='Grey')
app.shirtsPerson2=Label("Ronald",250,160,size=20,bold=True)
app.ronaldDetails=Label("Book Now",250,180,size=10,fill='Grey')
app.shirtsPerson3=Label("Bethany",160,220,size=20,bold=True)
app.bethanyDetails=Label("Book Now",160,240,size=10,fill='Grey')
app.shirtsPerson4=Label("Jannah",250,220,size=20,bold=True)
app.jannahDetails=Label("Book Now", 250,240, size=10, fill='Grey')
app.shirtsScreen=Group(app.shirtsTitle,app.shirtsPerson1,app.shirtsPerson2,app.shirtsPerson3,app.shirtsPerson4,app.naomiDetails,app.ronaldDetails,app.bethanyDetails,app.jannahDetails)
app.shirtsScreen.visible=False
# jackets screen
app.jacketsTitle=Label("Near you:",200,120,size=18)
app.jacketsPerson1=Label("King",150,160,size=20,bold=True)
app.kingDetails=Label("Book Now",150,180,size=10,fill='Grey')
app.jacketsPerson2=Label("Marley",250,160,size=20,bold=True)
app.marleyDetails=Label("Book Now",250,180,size=10,fill='Grey')
app.jacketsPerson3=Label("Trish",150,220,size=20, bold=True)
app.trishDetails=Label("Book Now",150,240,size=10,fill='Grey')
app.jacketsPerson4=Label("Rachel",250,220,size=20, bold=True)
app.rachelDetails=Label("Book Now", 250,240, size=10, fill='Grey')
app.jacketsScreen=Group(app.jacketsTitle,app.jacketsPerson1,app.jacketsPerson2,app.jacketsPerson3,app.jacketsPerson4, app.kingDetails,app.marleyDetails,app.trishDetails,app.rachelDetails)
app.jacketsScreen.visible=False
