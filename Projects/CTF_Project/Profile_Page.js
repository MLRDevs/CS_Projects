/*
    Alex Miller
    Jordan Latimer

    Client code for Profile Page for Users
*/

// populate both user tables
async function PopulateUserTables(PCData) {
    const TB = document.querySelector('#Past_Contests tbody');
    TB.innerHTML = "";

    // get all of the flags
    const res = await fetch('/getAllFlags');
    const PCData2 = await res.json();
    let flagamount = 0;

    // insert the amount of flags per contests
    PCData.forEach(contest => {
        const row = document.createElement('tr');
        const name = document.createElement('td');
        name.textContent = contest.Name;
        const flags = document.createElement('td');
        PCData2.forEach(flag => {
            if (flag.ContestID === contest.ContestID) flagamount++;
        });
        flags.textContent = flagamount;


        // add to the table
        row.appendChild(name);
        row.appendChild(flags);

        TB.appendChild(row);
    });

    // get the user information
    const data = { email: getEmail() };
    const res2 = await fetch('/getUser', {
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json'
        },
        body: JSON.stringify(data)
    });
    if (res2.ok) {
        const Rdata = await res2.json();

        const TB2 = document.querySelector('#Record tbody');
        TB2.innerHTML = '';

        // create the table for the users record, flags completed, and total flags
        const row = document.createElement('tr');
        const Total = document.createElement('td');
        const Completed = document.createElement('td');
        const record = document.createElement('td');
        Total.textContent = flagamount;
        Completed.textContent = Rdata.Flags;
        record.textContent = Completed.innerHTML + ' / ' + Total.innerHTML;

        row.appendChild(Completed);
        row.appendChild(Total);
        row.appendChild(record);

        TB2.appendChild(row);
    }
    else {
        console.error('Error getting data for Flag Users');
    }
}