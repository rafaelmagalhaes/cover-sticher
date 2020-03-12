const submit = document.getElementById('submit'),
    submitBtn = document.getElementById('submit-btn'),
    resultsEl = document.getElementById('results'),
    search = document.getElementById('search'),
    name = document.getElementById('name'),
    csrf = document.getElementsByName('csrfmiddlewaretoken')[0];


function removeSpace(str) {
    return str.replace(/\s+/g, ',');
}

async function searchMeal(e) {
    e.preventDefault();
    const isbns = search.value,
        list_name = name.value;
    submitBtn.disabled = true;
    try {
        const response = await fetch(`process_images?q=${isbns}&name=${list_name}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrf.value
            },
            body: JSON.stringify({
                name: list_name,
                isbns: isbns
            })
        });
        if (!response.ok) {
            throw new Error(response.status);
        }
        submitBtn.disabled = false;
       $('#results').load('#results')
    } catch (error) {
        submitBtn.disabled = false;
        console.log(error)
    }

}

// Event listeners
submit.addEventListener('submit', searchMeal);
