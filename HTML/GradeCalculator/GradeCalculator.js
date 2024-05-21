// Alex Miller
// JS for Grade Calculator

function AddItem() {
    var assignmentnumber = GetAssignmentNumber();
    if (assignmentnumber == 99) {
        alert('maximum amount of assignments');
    }
    else {
        //get assignments and add the new grade
        var assignments = document.getElementById("assignments");
        var grades = document.getElementById("GradePercentage");
        var assignmentgrade = assignments.lastElementChild.value;
        var values = assignmentgrade.split('/');
        var percentage = Math.round((values[0] / values[1]) * 100);
        grades.lastElementChild.innerHTML = percentage;
        Style(percentage, grades.lastElementChild);

        // add the new input line for assignments
        var br = document.createElement('br');
        var input = document.createElement('input');
        input.setAttribute('placeholder', '50/60');
        input.setAttribute('id', 'assignment');
        assignments.appendChild(br);
        br = document.createElement('br');
        assignments.appendChild(br);
        assignments.appendChild(input);

        // add the new input line for weights
        var weights = document.getElementById('weights');
        input = document.createElement('input');
        input.setAttribute('placeholder', '10');
        input.setAttribute('type', 'number');
        br = document.createElement('br');
        weights.appendChild(br);
        br = document.createElement('br');
        weights.appendChild(br);
        weights.appendChild(input);

        // add the new div for percentage
        br = document.createElement('br');
        grades.appendChild(br);
        div = document.createElement('div');
        div.setAttribute('id', 'GPercent');
        div.innerHTML = "0";
        grades.appendChild(div);

        // change the amount of assignments
        var assignmentnumber = GetAssignmentNumber();
        assignmentnumber = parseInt(assignmentnumber);
        document.getElementById('numofassignments').innerHTML = 'Amount of assignments (' + (assignmentnumber+1) + ')';
    }
}
function Style(text, prop) {
    if (text >= 80) {
        prop.style = "color: greenyellow";
    }
    else if (text < 80 && text >= 69) {
        prop.style = "color: orange";
    }
    else {
        prop.style = "color: red";
    }
}
function GetAssignmentNumber() {
    var assignmentstring = document.getElementById('numofassignments').innerHTML;
    if (assignmentstring.length == 25) {
        var number = assignmentstring.substring(23,24);
        return number;
    }
    else {
        var number = assignmentstring.substring(23,25);
        return number;
    }
}
function DeleteItem() {
    var assignmentnumber = GetAssignmentNumber();
    if (assignmentnumber == 1) {
        alert('minimum amount of assignments');
    }
    else {
        // Delete last assignment input and breaks
        var assignments = document.getElementById('assignments');
        assignments.removeChild(assignments.lastElementChild);
        assignments.removeChild(assignments.lastElementChild);
        assignments.removeChild(assignments.lastElementChild);

        // Delete last weight input and breaks
        var weights = document.getElementById('weights');
        weights.removeChild(weights.lastElementChild);
        weights.removeChild(weights.lastElementChild);
        weights.removeChild(weights.lastElementChild);

        // Delete last percentage
        var grades = document.getElementById('GradePercentage');
        grades.removeChild(grades.lastElementChild);
        grades.removeChild(grades.lastElementChild);

        // drop assignments number by 1
        var assignmentnumber = GetAssignmentNumber();
        assignmentnumber = parseInt(assignmentnumber);
        assignmentnumber--;
        document.getElementById('numofassignments').innerHTML = 'Amount of assignments (' + assignmentnumber + ')';
    }
}
function RefreshPercents() {
    // get assignments and grades
    var assignments = document.getElementById('assignments').children;
    var grades = document.getElementById('GradePercentage').children;

    // loop through each one and calculate the new grade
    var spot = 3;
    for (var i=3; i < assignments.length; i+=3) {
        var text = assignments[i].value;
        var values = text.split('/');
        var percentage = Math.round((values[0] / values[1]) * 100);
        grades[spot].innerHTML = percentage;

        // get the color right for the new percentage
        Style(percentage, grades[spot])
        spot += 2;
    }
}
function FinalGrade() {
    // check all assignment inputs are valid
    var assignments = document.getElementById('assignments').children;
    for (var i=3; i < assignments.length; i+=3) {
        if (assignments[i].value == "" || assignments[i].value == null) {
            alert('must fill all assignment input fields');
            return null;
        }
    }

    // check all weight inputs are valid
    var weights = document.getElementById('weights').children
    for (var i=2; i < weights.length; i+=3) {
        if (weights[i].value == "" || weights[i].value == null) {
            alert('must fill all weight input fields');
            return null;
        }
    }

    // update all the grades
    RefreshPercents();
    
    // get the final grade
    var topfrac = 0;
    var bottomfrac = 0;
    var spot = 3;
    var grades = document.getElementById('GradePercentage').children;
    for (var i=2; i < weights.length; i+=3) {
        var gradepercent = parseInt(grades[spot].innerHTML);
        topfrac += Math.round(weights[i].value * gradepercent);
        bottomfrac += parseInt(weights[i].value);
        spot += 2;
    }
    var Final = Math.round(topfrac / bottomfrac);
    
    // change the final grade in the html
    var finalgrade = document.getElementById('FinalGrade');
    finalgrade.innerHTML = 'Estimated Final Grade: ' + Final + ' %';
    Style(Final, finalgrade);
}