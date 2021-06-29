let grid_canvas = document.getElementById("grid");
let context = grid_canvas.getContext("2d");

function createGrid() {
    for (let x = 0.5; x < 601; x += 30) {
        context.moveTo(x, 0);
        context.lineTo(x, 601);
    }
    for (let y = 0.5; y < 601; y += 30) {
        context.moveTo(0, y);
         context.lineTo(601, y);
    }
    context.strokeStyle = "#000000";
    context.stroke();
}

function drawPoint(point, color) {
    context.fillStyle = color;
    context.beginPath();
    context.arc(point[0] *30, point[1] *30, 5, 0, 2 * Math.PI);
    context.fill();
    context.closePath();    
}

function drawPointList(pointList, color) {
    for(let p of pointList) {
        drawPoint(p, color)
    }    
}

function overDraw(oldPoint, newPoint, color) {
    //eraser
    for( let p of oldPoint) {
        drawPoint(p, "#FFFFFF")
    }
    //overdraw
    for (let p of newPoint) {
        drawPoint(p, "#FF0000")
    }
}

function drawLineSegment(pointA, pointB) {
    
    context.beginPath();
    context.moveTo(pointA[0]*30, pointA[1]*30);
    context.lineTo(pointB[0]*30, pointB[1]*30);
    context.strokeStyle = "#FFFF00";
    context.stroke();
}

let point = JSON.parse(document.getElementById('p').getAttribute('data-point'))
let des = point["blue"][0]

createGrid()

drawPointList(point["blue"], "#32CD32")
drawPointList(point["red"], "#FF0000")

function handleNext() {
    fetch('/grid', {
        headers: {
            'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify("post")
    }).then (function (response) {
        return response.text()
    }).then (function (text) {
        point = JSON.parse(text)               
        let per = point['permannentPoint']
        let preStep = per[ per.length-2]
        let nextStep = per[ per.length-1]
        
        if ((nextStep[0] != des[0] ) || (nextStep[1] != des[1])) {
            drawLineSegment(preStep, nextStep)        
            overDraw(point['oldPoint'], point['newPoint'])
            drawPoint(nextStep, "#32CD32")
        }      
        drawLineSegment(preStep, nextStep)  
    })
}