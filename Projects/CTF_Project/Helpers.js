/*
    Jordan Latimer
    Alex Miller

    Helper functions used by a variety of javascript files
*/

// get the email of the client
function getEmail() {
	const url = window.location.search;
	const params = new URLSearchParams(url);
	return params.get('email');
}

// got to a specific page
function gotoPage(page) {
	window.location.href = page + getEmail();
}

// popup window for a specific page with the email
function Popup(site,email) {

    const width = 500;
    const height = 500;

    // get the right placement and size for any screen
    const x = screenX + (window.screen.width / 2) - (width / 2);
    const y = screenY + (window.screen.height / 2) - (height / 2);

    // add the features and the email inside the URL and open the window
    const features = `width=${width},height=${height},left=${x},top=${y}`;
    const params = new URLSearchParams(email).toString();
    const url = `${site}?`;
    if (email !== undefined) window.open(url + `email=${encodeURIComponent(email)}`,'popup',features);
    else window.open(url,'popup',features);
}

// get all the table contents and add them in the respective table
async function PopulateTable(page) {
	const data = { email: getEmail() };
	const res = await fetch('/getContests', {
		method: 'POST',
		headers: {
			'Content-Type' : 'application/json'
		},
		body: JSON.stringify(data)
	});
	if (res.ok) {
		const list = await res.json();
		if (page === 0) InsertIntoTable(list);
		else PopulateUserTables(list);
	}
}

const flagItems = document.querySelectorAll('#Flag_Sidebar li');
flagItems.forEach(item => {
	item.addEventListener('click', function() {
		flagItems.forEach(f => f.classList.remove('selected-flag'));
		item.classList.add('selected-flag');
	})
})