let bluePoint = []
let redPoint = []

function handleSubmit() {
    let xA = parseInt(document.getElementById('xA').value)
    let yA = parseInt(document.getElementById('yA').value)
    let xB = parseInt(document.getElementById('xB').value)
    let yB = parseInt(document.getElementById('yB').value)
    var permannentPoint= []    
    permannentPoint.push([xB, yB])
    permannentPoint.push([xA, yA])
    
    var asJson = JSON.stringify(permannentPoint)
    fetch('/', {
        headers: {
            'Content-Type': 'application/json'
        },
        method: 'POST',
        body: asJson
    }).then ( response => location.href('/grid'))
}
     


