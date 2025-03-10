/*
    Jordan Latimer
    Alex Miller

    Modifying Contests for Admin
*/

// on load
window.addEventListener('load', function(event) {
    
    // if not on an add flag/add contest or one of those screens
    if (!(window.opener && window.opener !== window)) {
        loadContests();
	    loadFlagsForContest();
    }

    // for popup windows
    else {
        // to make sure we are in addflag or all images
        getImages();
    }
	
});

// get all of the images and put them into the dropdown list
async function getImages() {
    const data = { email: getEmail() };
    const res = await fetch('/getImages', {
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json'
        },
        body: JSON.stringify(data)
    });
    if (res.ok) {
        const list = document.getElementById('Images');
        const ret = await res.json();

        // loop through all of the images adding them to the options list
        for (var i=0; i < ret.length; i++) {
            let op = document.createElement('option');
            op.innerHTML = ret[i].Name;
            list.appendChild(op);
        }
    }
}

let selectedContest = {name: null ,id: null};
let selectedFlag = {name: null, id: null};

// popup window to add Flag
function PopupForFlag(site) {
    if(selectedContest.id === null || selectedContest.id === undefined){
        alert("Select a contest");
        return;
    }

    // setting up the sizing and openeing the window with the contest ID in the URL
	const width = screen.width;
	const height = screen.height;
    const contestId = selectedContest.id;
    const x = (screen.width - width) / 2;
    const y = (screen.height - height) / 2;
    const url = `${site}?contestId=${contestId}&email=${getEmail()}`;
    const features = `width=${width},height=${height},left=${x},top=${y}, scrollbars = yes`;
	window.open(url, 'popup',features);
}

// select a contest
function selectContest(contestName, contestId, listItem) {

    // Deselect the previously selected contest
    const previouslySelected = document.querySelector('.selected');
    if (previouslySelected) {
        previouslySelected.classList.remove('selected');
    }

    // Select the new contest and clear last flag selected
    listItem.classList.add('selected');
    selectedContest = {name: contestName, id: contestId};  // Store the selected contest name
    selectedFlag = {name: null, id: null};
    loadFlagsForContest();

    console.log("Selected contest:", contestName);
}

// select a flag
function selectFlag(flag, flagName, flagId, listItem) {

    // Optionally, highlight the selected flag visually
    const previouslySelectedFlag = document.querySelector('.selected-flag');
    if (previouslySelectedFlag) {
        previouslySelectedFlag.classList.remove('selected-flag');
    }
    listItem.classList.add('selected-flag');
    selectedFlag = {name: flagName, id: flagId};
}

// add the image to the right side for the specfic flag
function AddImage(flag) {
    const image = flag.Image;
    const imageList = document.getElementById('imageList');
    const listitem = document.createElement('li');
    listitem.textContent = image + ' (' + flag.Name + ')';
    listitem.onclick = function() {
        listitem.classList.toggle('selected-image');
    }
    imageList.appendChild(listitem);
}

// delete an image from the database
async function DeleteImage() {
    const image = document.querySelector('.selected-image');
    if (image === undefined || image === null) {
        alert('must select an immage to delete it');
        return;
    }

    const data = { flag: selectedFlag.id, image: image };
    const res = await fetch('/DeleteImageReplaceFlag', {
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json'
        },
        data: JSON.stringify(data)
    });
    if (res.ok) {
        window.reload();
    }
}

// add a contest to the database
async function AddContest() { 
	const name = document.getElementById("Name").value;
    console.log("Name entered: ", name);
    const isActive = 0;
	const data = {Name: name, IsActive: isActive, email: getEmail()};
	const res = await fetch('/AddContest', {
		method: 'POST',
		headers: {
			'Content-Type' : 'application/json'
		},
		body: JSON.stringify(data)
	});
	if (res.ok) {
		console.log("Success: adding contest");
		window.opener.location.reload();
		window.close();
	}
	else {
		console.log("ERROR: adding contest");
	}
}

// delete a specific contest
async function deleteContest() {
    if (!selectedContest.id) {
        console.log("No contest selected");
        alert("Please select a contest to delete.");
        return;
    }

    // Send a POST request to delete the contest by its name
    const contestId = selectedContest.id;
    let data = {contest: contestId};  // You could pass contest's `id` instead if needed
    let res = await fetch('/DeleteContest', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });

    if (res.ok) {
        console.log("Success: deleting contest");

        // Reload the contests list after deleting
        loadContests();
    } else {
        console.log("ERROR: deleting contest");
        alert("Failed to delete contest.");
    }

    // delete all the flags from the now deleted contest
    data = { contest: selectedContest.id };
    res = await fetch('/DeleteFlagsFromContest', {
		method: 'POST',
		headers: {
			'Content-Type' : 'application/json'
		},
		body: JSON.stringify(data)
	})
	if (res.ok) {
		console.log('deleted flags');
		location.reload();
	}
	else {
		console.error('error deleting flags');
	}
}

// load all the contests for specific Admin
async function loadContests() {
    try {
        const data = { email: getEmail() };
        const res = await fetch('/getContests', {
            method: 'POST',
            headers: {
                'Content-Type' : 'application/json'
            },
            body: JSON.stringify(data)
        });
        if (res.ok) {
            const contests = await res.json();

            // Get the contest list element
            const contestList = document.getElementById('contestList');

            // Clear the existing list
            contestList.innerHTML = '';

            // Loop through the contests and create list items
            contests.forEach(contest => {
                const li = document.createElement('li');
                if (contest.IsActive === 1) li.style.backgroundColor = 'lawngreen';
                li.textContent = contest.Name;
                li.onclick = () => selectContest(contest.Name, contest.ContestID, li);  // This line is important
                contestList.appendChild(li);  // Add the list item to the list
            });
        }
    } catch (error) {
        console.error('Error loading contests:', error);
    }
}

// add a flag to a contest
async function AddFlag(){
	// get contestId from URL
	contestId = getContestIdFromURL();

    // get all the values in the form
    const flagName = document.getElementById("Name").value;
    const description = document.getElementById("Description").value;
    let Hint1 = document.getElementById("Hint1").value;
    let Hint2 = document.getElementById("Hint2").value;
    let Hint3 = document.getElementById("Hint3").value;
    const image = document.getElementById('Images').value;
    const path = document.getElementById('Path').value;

    // required fields
    if(!flagName){
        alert("Enter a flag name.");
        return;
    }
    if(contestId === null || contestId === undefined){
        alert("Please select a contest first.");
        return;
    }

    // add the flag
    const data = {name: flagName, desc: description, contest: contestId, image: image, path: path, hint1: Hint1 || '', hint2: Hint2 || '', hint3: Hint3 || ''};
    try{
        const response = await fetch('/AddFlag', {
            method: 'POST',
            headers: {'Content-Type': 'application/json',},
            body: JSON.stringify(data)
        });
        if(response.ok){
            console.log("Flag added");
            window.close();
            // reload the parent window when this window closes
            window.onunload = function() {
				window.opener.location.reload();
			};
        }
        else{
            alert("Failed to add flag.");
        }
    } catch(error){
        console.error("Error adding flag:", error);
        alert("An error occurred while adding flag.");
    }
}

// get the contestID from URL
function getContestIdFromURL(){
    const params = new URLSearchParams(window.location.search);
    return params.get('contestId');
}

// load the flags for the specific contest
async function loadFlagsForContest() {
    if (!selectedContest.id) {
		console.log('no selected Contest');
        return;
    }
    try {
		const data = { contest: selectedContest.id };
        const res = await fetch('/getAllFlagsFromContest', {
			method: 'POST',
			headers: {
				'Content-Type' : 'application/json'
			},
			body: JSON.stringify(data),
		});
		if (res.ok) {
        	const flags = await res.json();

            // get flags list and images list and clear them
        	const flagList = document.getElementById('flagList');
        	flagList.innerHTML = '';

            const imageList = document.getElementById('imageList');
            imageList.innerHTML = '';

        	if (flags === undefined || flags.length === 0) {
        	    flagList.innerHTML = '<li>No flags found for this contest.</li>';
        	}

            // create a list item for each flag
        	flags.forEach(flag => {
        	    const li = document.createElement('li');
        	    li.textContent = flag.Name;
                li.onclick = () => selectFlag(flag, flag.Name, flag.FlagID, li); //*
        	    flagList.appendChild(li);  // Add each flag to the list
                AddImage(flag); // add the image to the list
        	});
		}
		else {
			console.error('error getting flags');
		}
    } catch (error) {
        console.error('Error loading flags:', error);
    }
}

// set a contest to active state
async function setContestActive() {
    if (!selectedContest.id) {
        console.log("No contest selected");
        alert("Please select a contest to set active.");
        return;
    }

    const contestId = selectedContest.id;
    let data = { contest: contestId, email: getEmail() };
    let res = await fetch('/setContestActive', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });

    if (res.ok) {
        console.log("Set as active");

        // Reload the contests list after deleting
        loadContests();
    } else {
        const err = await res.json();
        alert(err.error);
    }
}

// end a current active contest
async function EndContest() {
    if (!selectedContest.id) {
        console.log("No contest selected");
        alert("Please select a contest to set active.");
        return;
    }

    const contestId = selectedContest.id;
    let data = { contest: contestId, email: getEmail() };
    let res = await fetch('/EndContest', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });

    if (res.ok) {
        console.log("End Contest");
        // Reload the contests list after ending one
        loadContests();
    } else {
        const err = await res.json();
        alert(err.error);
    }
}

// delete a flag 
async function DeleteFlag() {
    if(!selectedContest.id){
        console.log("no contest selected");
        alert("Please select a flag to delete");
        return;
    }

    if (!selectedFlag) {
        console.log("No flag selected");
        alert("Please select a flag to delete.");
        return;
    }

    const flagId = selectedFlag.id;
    let data = { flag: flagId };

    let res = await fetch('/DeleteFlag', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });

    if (res.ok) {
        console.log("Flag deleted successfully");

        // Reload the flags list after deleting
        loadFlagsForContest(selectedContest.id);
    } else {
        const err = await res.json();
        alert(err.error);
    }
}