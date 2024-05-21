// Alex Miller
// JavaScript for GPA calculator

function AddSemester() {
    var semesternumber = GetSemesterNumber();
    if (semesternumber == 99) {
        alert('Maximum number of semesters');
    }
    else {
        // get the semester div and add the new dropdown
        var semesters = document.getElementById('SemesterForm');
        for (var i=0; i < 3; i++) {
            var br = document.createElement('br');
            semesters.appendChild(br);
        }

        // get the semester number and add the lable
        var semesternumber = GetSemesterNumber();
        semesternumber = parseInt(semesternumber);
        var lable = document.createElement('lable');
        lable.innerHTML = "Semester #" + (semesternumber+1) + ' ';
        semesters.appendChild(lable);

        // change the semester number
        document.getElementById('numofsemesters').innerHTML = "Amount of semesters (" + (semesternumber+1) + ")";

        // add the buttons
        var button = document.createElement('button');
        button.setAttribute('onclick', 'AddClass(' + (semesternumber+1) + ')');
        button.setAttribute('type', 'button');
        button.innerHTML = 'Add Class';
        button.setAttribute('style', 'margin: 4px')
        semesters.appendChild(button);
        button = document.createElement('button');
        button.setAttribute('onclick', 'DeleteClass(' + (semesternumber+1) + ')');
        button.setAttribute('type', 'button');
        button.innerHTML = "Delete Class";
        semesters.appendChild(button);

        // add hr and br
        var hr = document.createElement('hr');
        var br = document.createElement('br');
        semesters.appendChild(hr);
        semesters.appendChild(br);

        // add the dropdown menu
        var select = document.createElement('select');
        select.setAttribute('id', 'Semester');
        select.setAttribute('style', 'margin-right: 4px');
        semesters.appendChild(select);
        AddDropDown(select);

        // add the credits input field
        var input = document.createElement('input');
        input.setAttribute('type', 'number');
        input.setAttribute('placeholder', '0');
        input.setAttribute('id', semesternumber+1);
        semesters.appendChild(input);

    }
}
function AddDropDown(select) {
    var option = document.createElement('option');
    option.innerHTML = 'A+';
    select.appendChild(option);
    option = document.createElement('option');
    option.innerHTML = 'A';
    select.appendChild(option);
    option = document.createElement('option');
    option.innerHTML = 'A-';
    select.appendChild(option);
    option = document.createElement('option');
    option.innerHTML = 'B+';
    select.appendChild(option);
    option = document.createElement('option');
    option.innerHTML = 'B';
    select.appendChild(option);
    option = document.createElement('option');
    option.innerHTML = 'B-';
    select.appendChild(option);
    option = document.createElement('option');
    option.innerHTML = 'C+';
    select.appendChild(option);
    option = document.createElement('option');
    option.innerHTML = 'C';
    select.appendChild(option);
    option = document.createElement('option');
    option.innerHTML = 'C-';
    select.appendChild(option);
    option = document.createElement('option');
    option.innerHTML = 'D+';
    select.appendChild(option);
    option = document.createElement('option');
    option.innerHTML = 'D';
    select.appendChild(option);
    option = document.createElement('option');
    option.innerHTML = 'D-';
    select.appendChild(option);
    option = document.createElement('option');
    option.innerHTML = 'F';
    select.appendChild(option);
}
function GetSemesterNumber() {
    var semesterstring = document.getElementById('numofsemesters').innerHTML;
    if (semesterstring.length == 23) {
        var number = semesterstring.substring(21,22);
        return number;
    }
    else {
        var number = semesterstring.substring(21,23);
        return number;
    }
}
function DeleteSemester() {
    var semesternumber = GetSemesterNumber();
    if (semesternumber == 1) {
        alert('Minimum number of semesters');
    }
    else {
        var semesters = document.getElementById('SemesterForm');
        for (var i=0; i < 10; i++) {
            semesters.removeChild(semesters.lastElementChild);
        }
        semesternumber = parseInt(semesternumber);
        document.getElementById('numofsemesters').innerHTML = "Amount of semesters (" + (semesternumber-1) + ")";
    }
}
function AddClass(pos) {
    var semesters = document.getElementById('SemesterForm');
    var spot = false;

    // get to the right spot in semesterform
    for (var i=0; i < semesters.length; i++) {
        var temp = semesters[i];
        if (semesters[i].getAttribute('id') == pos) {
            spot = true;
            break;
        }
    }

    // add the new class
    if (spot == true) {
        // add the br
        var br = document.createElement('br');
        br.setAttribute('id', 'break');
        var input = document.getElementById(pos);
        semesters.insertBefore(br, input.nextElementSibling);

        // add the dropdown
        var select = document.createElement('select');
        select.setAttribute('id', 'Semester');
        select.setAttribute('style', 'margin-right: 4px');
        semesters.insertBefore(select, br.nextElementSibling);
        AddDropDown(select);

        // add the input field
        var input2 = document.createElement('input');
        input2.setAttribute('type', 'number');
        input2.setAttribute('placeholder', '0');
        semesters.insertBefore(input2, select.nextElementSibling);
    }
}
function DeleteClass(pos) {
    var semesters = document.getElementById('SemesterForm');
    var spot = false;
    var newpos = 0;

    // go through semesterform till hit right semester
    for (var i=0; i < semesters.length; i++) {
        var temp = semesters[i];
        if (temp.getAttribute('id') == pos) {
            spot = true;
            newpos = i;
            break;
        }
    }
    var input = semesters[newpos];
    if (input.nextElementSibling == null || input.nextElementSibling.getAttribute('id') != 'break') {
        alert('Minumim number of classes');
        return null;
    }
    else {
        // get to the last input field and remove it
        if (spot == true) {
            for (var i=0; i < 3; i++) {
                var temp = semesters[newpos].nextElementSibling;
                semesters.removeChild(temp);
            }
        }
    }

}
function getPoints(letter) {
    if (letter == 'A+' || letter == 'A') {
        return 4.0;
    }
    else if (letter == 'A-') {
        return 3.7;
    }
    else if (letter == 'B+') {
        return 3.3;
    }
    else if (letter == 'B') {
        return 3.0;
    }
    else if (letter == 'B-') {
        return 2.7;
    }
    else if (letter == 'C+') {
        return 2.3;
    }
    else if (letter == 'C') {
        return 2.0;
    }
    else if (letter == 'C-') {
        return 1.7;
    }
    else if (letter == 'D+') {
        return 1.3;
    }
    else if (letter == 'D') {
        return 1.0;
    }
    else if (letter == 'D-') {
        return 0.7;
    }
    else {
        return 0.0;
    }
} 
function FinalGPA() {

    document.getElementById('FinalGPA').innerHTML = '';
    var semesternumber = GetSemesterNumber();
    semesternumber = parseInt(semesternumber);
    var input = document.getElementById('1');
    // check the credits are valid
    for (var i=0; i < semesternumber; i++) {
        while (input.nextElementSibling != null && input.nextElementSibling.getAttribute('id') == 'break') {
            if (input.value == null || input.value == '') {
                alert('Fill in all credits fields');
                return null;
            }
            input = input.nextElementSibling.nextElementSibling.nextElementSibling;
        }
        if (input.value == null || input.value == '') {
            alert('Fill in all credits fields');
            return null;
        }
    }
    // get all the grade points and credits
    input = document.getElementById('1');
    var topfrac = 0;
    var bottomfrac = 0;
    for (var i=0; i < semesternumber; i++) { // each semester
        while(input.nextElementSibling != null && input.nextElementSibling.getAttribute('id') == 'break') {
            var letter = input.previousElementSibling.value;
            var points = getPoints(letter);
            var credits = parseInt(input.value);
            topfrac += (points * credits);
            bottomfrac += credits;
            input = input.nextElementSibling.nextElementSibling.nextElementSibling;
        }
        var letter = input.previousElementSibling.value;
        var points = getPoints(letter);
        var credits = parseInt(input.value);
        topfrac += (points * credits);
        bottomfrac += credits;
    }
    var GPA = parseFloat(topfrac/bottomfrac).toFixed(2);
    document.getElementById('FinalGPA').innerHTML = "Estimated Final GPA: " + GPA;
    if (GPA >= 3.0) {
        document.getElementById('FinalGPA').style = "color: greenyellow";
    }
    else if (GPA < 3.0 && GPA >= 2.0) {
        document.getElementById('FinalGPA').style = "color: orange";
    }
    else {
        document.getElementById('FinalGPA').style = "color: red";
    }
}