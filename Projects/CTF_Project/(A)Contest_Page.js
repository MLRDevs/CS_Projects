/*
	Alex Miller
	Jordan Latimer

	Client side code for Contest Page on Admin side
*/

// on load, load the active contest
window.addEventListener('load', async function() {

	// basics for use in multiple methods
	flagname = document.getElementById('Flag_Name');
	description = document.getElementById('Desc');
	hintDesc = document.getElementById('Hint_Desc');
	HintButts = document.getElementById('Hint_Butts');
	LoadContest();
});

// load the current active contest
async function LoadContest() {
	const data = { email: getEmail() };
	const res = await fetch('/getActiveContest', {
		method: 'POST',
		headers: {
			'Content-Type' : 'application/json'
		},
		body: JSON.stringify(data)
	});
	if (res.ok) {
		const contest = await res.json();

		if (!contest) {
			alert('No Contest is Active');
		}
		else {
			console.log('Contest:', contest);
			LoadElements(contest);
		}
	}
	
};

// load all the dynamic elements
async function LoadElements(contest) {
	const data = { contest: contest.ContestID };
	const res = await fetch('/getAllFlagsFromContest', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(data)
	});
	if(!res.ok){
		console.error('Error fetching flags for contest');
		return;
	}
	const flagdata = await res.json();
	console.log("Fetched Flags:", flagdata);
	const UL = document.querySelector('#FlagList');
	UL.innerHTML = '';

	if(flagdata.length === 0){
		console.warn("no flags found for contest");
		return;
	}
	// add the contest name to the list
	contestName = document.getElementById('Contest_Name');
	contestName.innerHTML = contest.Name;

	// add the hints
	hintDesc.innerHTML = 'click buttons to see hints';

	// add each flag to the list
	document.getElementById('Flag_Name').textContent = '';
	document.getElementById('Desc').textContent = '';
	HintButts.innerHTML = '';
	const submitFlagButton = document.getElementById('Submit_Flag_Stuff');
	if(submitFlagButton) submitFlagButton.classList.add('hidden');
	
	//if(!document.location.href.includes("(A)Contest_Page.html")) {document.getElementById('Submit_Flag').classList.add('hidden'); }
	document.getElementById('Hint_Stuff').classList.add('hidden');
	document.getElementById('DefaultMessage').style.display = 'block';

	flagdata.forEach(flag => {
		
			console.log(flag);
			const li = document.createElement('li');
			const a = document.createElement('a');
			a.textContent = flag.Name;
			li.onclick = () => setNewFlag(flag);

			// add to list
			li.appendChild(a);
			UL.appendChild(li);
	});
	getActiveFlag(getEmail(), contest.ContestID);
}

// get the active flag of a user
async function getActiveFlag(email, contest) {
	const data = { email: email };
	const res = await fetch('/getActiveFlag', {
		method: 'POST',
		headers: {
			'Content-Type' : 'application/json'
		},
		body: JSON.stringify(data)
	});
	if (res.ok) { // get the active flag onto html
		const ret = await res.json();

		// go through all the flags gotten and make sure it's the right one for this contest
		for (let i=0; i < ret.length; i++) {
			if (contest === ret[i].ContestID) setUpFlag(ret[i]);
		}
	}
}

// get the new flag the user clicked on
async function setNewFlag(flag) {

	document.getElementById('Flag_Name').textContent = flag.Name;
	document.getElementById('Desc').textContent = flag.Description;
	const submitFlagButton = document.getElementById('Submit_Flag_Stuff');
	if(submitFlagButton)
		submitFlagButton.classList.remove('hidden');
	//if(!document.location.href.includes("(A)Contest_Page.html")) document.getElementById('Submit_Flag').classList.remove('hidden');
	document.getElementById('Hint_Stuff').classList.remove('hidden');
	document.getElementById('DefaultMessage').style.display = 'none';

	const email = getEmail();
	const data = { FlagImage: flag.Image, email: email };
	const res = await fetch('/setNewActiveFlag', {
		method: 'POST',
		headers: {
			'Content-Type' : 'application/json'
		},
		body: JSON.stringify(data)
	});
	if (res.ok) { // get the flag details onto html
		const ret = await res.json();
		clearTerminal();
		setUpFlag(flag);
		await updateContainer(email);
		console.log('Setting new Flag');
		await reattachTerminal();
		//window.location.reload();
	}
	else
		console.error('Failed to set new flag.');
}

// set the HTML to the correct flag
function setUpFlag(flag) {

	// set up the basics
	flagname.innerHTML = flag.Name;
	description.innerHTML = flag.Description;
	HintButts.innerHTML = '';
	hintDesc.innerHTML = '';

	// set up the hints buttons
	if (flag.Hint1) {
		const hint1 = document.createElement('button');
		hint1.textContent = 'Hint 1';
		hint1.addEventListener('click', function() {
			hintDesc.innerHTML = flag.Hint1;
		});
		HintButts.appendChild(hint1);
	}
	if (flag.Hint2) {
		const hint2 = document.createElement('button');
		hint2.textContent = 'Hint 2';
		hint2.addEventListener('click', function() {
			hintDesc.innerHTML = flag.Hint2;
		});
		HintButts.appendChild(hint2);
	}
	if (flag.Hint3) {
		const hint3 = document.createElement('button');
		hint3.textContent = 'Hint 3';
		hint3.addEventListener('click', function() {
			hintDesc.innerHTML = flag.Hint3;
		});
		HintButts.appendChild(hint3);
	}
}

async function updateContainer(email){
	const res = await fetch(`/updateContainer/${email}`, { method: 'POST'});

	if(res.ok){
		console.log('Container updated successfully');
	}
		
	else
		console.log('Failed to update container');
}

async function stopContainer(){
	if(container){
		await container.kill();
		await container.remove({force:true});
	}
}

async function reattachTerminal(){
	console.log('reattaching termnial');

	if(term) term.dispose();
	term = new Terminal();
	term.open(document.getElementById('Linux_Shell'));
	const socket = new WebSocket('ws://localhost:3000');
	socket.onopen = () => {
		socket.send(JSON.stringify(getEmail()));
		console.log('Websocket opened');
	}
	const attachAddon = new AttachAddon.AttachAddon(socket);
	term.loadAddon(attachAddon);
	term.focus();
	socket.onclose = () => {
		console.log("socket closed");
	}
}

function clearTerminal(){
	term.write("\x1b[2J");
	term.write("\x1b[H");
	term.write('Loading Environment...');
}

function AconfirmSelection(){
	const confirmSelection_ = confirm("You will lose your current flag progress, are you sure?");
	if(confirmSelection_){
		const email = getEmail();
		window.location.href = `(A)Profile_Page.html?email=${email}`;
	}
	else
		console.log("Profile navigation canceled");
}

function confirmSelection(){
	const confirmSelection_ = confirm("You will lose your current flag progress, are you sure?");
	if(confirmSelection_){
		const email = getEmail();
		window.location.href = `Profile_Page.html?email=${email}`;
	}
	else
		console.log("Profile navigation canceled");
}
