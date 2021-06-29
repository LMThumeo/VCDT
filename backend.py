from flask import *
from random import *
from algor import *

backend = Flask(__name__)

def randomInitial(permannentPoint):
    pointList = [] 
    #pointList.append(permannentPoint[0]) #add B to list   
    for i in range(100):
        duplicate = True
        while (duplicate):
            if(i < 21):
                xRandom = i
            else:
                xRandom = randint(0,20)
            yRandom = randint(0,20)
            point = [xRandom, yRandom]
            #print (point, point not in permannentPoint, point not in pointList)
            if ((point not in permannentPoint) and (point not in pointList)):
                pointList = [*pointList, point]
                duplicate = False
    return pointList
            
def randomToChangePoint(permannentPoint, pointList):    
    pointIndex = sample(range(len(pointList)), k=10)
    newPoint = []
    oldPoint = []

    # reserve to detele from tail of pointList inorder to not change index for points before it
    pointIndex.sort(reverse=True) 
    
    for i in pointIndex:
        oldPoint.append(pointList[i])
        pointList.remove(pointList[i])
    
    for index, item in enumerate(pointIndex):
        if item in range(21):
            x = oldPoint[index][0]
        else :
            x = randint(0,20)
        duplicate = True
        while (duplicate):
            y = randint(0,20)
            point = [x, y]
            if( (point not in pointList) and (point not in permannentPoint) and (point != oldPoint[index])):
                duplicate = False
                pointList = [*pointList, point]
                newPoint = [*newPoint, point]
    return oldPoint, newPoint, pointList
   
permannentPoint = []
pointList = []
    
@backend.route('/', methods=['GET', 'POST'])
def grid():
    if request.method == 'POST':
        print('Incoming..')
        global permannentPoint
        permannentPoint = request.json
        global pointList
        pointList = randomInitial(permannentPoint)
        return 'OK'
    else:
        return render_template('input.html') 

@backend.route('/grid', methods=['GET', 'POST'])
def draw():
    global permannentPoint, pointList
    if request.method == 'GET':
        response = json.dumps({
        'red': pointList,
        'blue': permannentPoint
        })
        return render_template('step.html', response = response)
    else:
        permannentPoint, pointList = findNext(permannentPoint, pointList)
        oldPoint, newPoint, pointList = randomToChangePoint(permannentPoint, pointList)
        
        response = json.dumps({
            'permannentPoint': permannentPoint,
            'oldPoint': oldPoint,
            'newPoint': newPoint
        })        
        return response
        