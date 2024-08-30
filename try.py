print("heello world")

x = 5
y = 10
print(x + y)


if(1):
    print("making changes to check if it commits in git")
    print("check")

if(0):

    down = {("Jan","grinder"): 1, ("Feb", "horiDrill"): 2, ("Mar", "borer"): 1,
            ("Apr", "vertDrill"): 1, ("May", "grinder"): 1, ("May", "vertDrill"): 1,
            ("Jun", "planer"): 1, ("Jun", "horiDrill"): 1}

    print(down.get(("Jan","grinder"),0))
    print(down.get(("Jan","horiDrill"),0))

    time_req = {
        "grinder": {    "Prod1": 0.5, "Prod2": 0.7, "Prod5": 0.3,
                        "Prod6": 0.2, "Prod7": 0.5 },
        "vertDrill": {  "Prod1": 0.1, "Prod2": 0.2, "Prod4": 0.3,
                        "Prod6": 0.6 },
        "horiDrill": {  "Prod1": 0.2, "Prod3": 0.8, "Prod7": 0.6 },
        "borer": {      "Prod1": 0.05,"Prod2": 0.03,"Prod4": 0.07,
                        "Prod5": 0.1, "Prod7": 0.08 },
        "planer": {     "Prod3": 0.01,"Prod5": 0.05,"Prod7": 0.05 }
    }

    print("time", time_req['grinder']['Prod1'])


### sample plot example
if(0):
    import matplotlib.pyplot as plt  
    
    # x axis values  
    x = [1,2,3]  
    # corresponding y axis values  
    y = [2,4,1]  
        
    # plotting the points   
    plt.plot(x, y)  
        
    # naming the x axis  
    plt.xlabel('x - axis')  
    # naming the y axis  
    plt.ylabel('y - axis')  
        
    # giving a title to my graph  
    plt.title('My first graph!')  
        
    # function to show the plot  
    plt.show()  

## sample optimization problem 
if(0):
    from gurobipy import *

    # resources and jobs sets
    R = ['Carlos', 'Joe', 'Monika']
    J = ['Tester', 'JavaDeveloper', 'Architect']

    combinations, ms = multidict({
        ('Carlos', 'Tester'): 53,
        ('Carlos', 'JavaDeveloper'): 27,
        ('Carlos', 'Architect'): 13,
        ('Joe', 'Tester'): 80,
        ('Joe', 'JavaDeveloper'): 47,
        ('Joe', 'Architect'): 67,
        ('Monika', 'Tester'): 53,
        ('Monika', 'JavaDeveloper'): 73,
        ('Monika', 'Architect'): 47
    })

    # Declare and initialize model
    m = Model('RAP')

    # Create decision variables for the RAP model
    x = m.addVars(combinations, name="assign")




    # create jobs  constraints
    job = m.addConstrs((x.sum('*',j) == 1 for j in J), 'job')
    job=m.addConstrs((x.sum('*',j)))

    # create resources constraints
    resource = m.addConstrs((x.sum(r,'*') <= 1 for r in R), 'resource')

    # The objective is to maximize total matching score of the assignments
    m.setObjective(x.prod(ms), GRB.MAXIMIZE)

    # save model for inspection
    m.write('RAP.lp')

    # run optimization engine
    m.optimize()

    def print_solution(model):
        for var in model.getVars():
            if abs(var.x) > 1e-6:
                print("{0}: {1}".format(var.varName, var.x))
        print('Total matching score: {0}'.format(model.objVal))
        return None

    # display optimal values of decision variables
    print_solution(m)  