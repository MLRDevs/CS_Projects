/*
	Alex Miller
	Jordan Latimer

	Client side js for the menu for the User just before entering a contest
*/

// insert all the contests into the two tables 
async function InsertIntoTable(list) {
	// Past Contest Table
	const PCT = document.querySelector('#Past_Contests tbody');
	PCT.innerHTML = '';

	// Active Contest Table
	const ACT = document.querySelector('#Record tbody');
	ACT.innerHTML = '';

	// list of flags
	const res2 = await fetch('/getAllFlags');
	const flaglist = await res2.json();

	const email = getEmail();

	list.forEach(contest => {
		const row = document.createElement('tr');
		const name = document.createElement('td');
		const flags = document.createElement('td');

		name.textContent = contest.Name;
		let i = 0;
		flaglist.forEach(flag => {
			if (flag.ContestID === contest.ContestID) i++;
		});
		flags.textContent = i;

		row.appendChild(name);
		row.appendChild(flags);

		if (contest.IsActive === 1) {
			const button = document.createElement('td');
			const JoinButton = document.createElement('button');
			JoinButton.textContent = 'Join';
			JoinButton.addEventListener('click', function() {
				window.location.href = '/Contest_Page.html?email=' + email;
			});

			button.appendChild(JoinButton);
			row.appendChild(button);
			ACT.appendChild(row);
		}
		else {
			PCT.appendChild(row);
		}
	});
}