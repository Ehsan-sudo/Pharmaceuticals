submitButton = document.getElementById('submit');
parent = document.getElementById('parent-div-for-rows');
addRow = document.getElementById('addRow');
removeRow = document.getElementById('removeRow');

names = {
    'Person1': 'Ahmad',
    'Person2': 'Mahmood'
}
response_from_server = {}


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

// ----------------------------------------------

submitButton.onclick = function(){
    console.log('submit button clicked');
    $.ajax({
        url: url_to,
        type: 'POST',
        headers: {'X-CSRFToken': csrftoken},
        contentType: 'application/json; charset=UTF-8',
        async: false, 
        data: JSON.stringify({'names': names}),
        dataType: 'json',
        success: ()=>{
            console.log('response sent!');
        },
        'error': (response)=>{
            console.log('error response!');
            console.log(response);
            response_from_server = response;
        }
    });
};


// ----- CREATING ROW ----------
count = 1;
addRow.onclick = (e) => {
    // the row div
    let row = document.createElement('div');
    row.classList.add('row');

    // the drug name input div
    let drugNameField = document.createElement('div');
    drugNameField.classList.add('col-md-5');

    let drugNameFieldSub = document.createElement('div');
    drugNameFieldSub.classList.add('mb-3', 'position-relative', 'pashto');

    let drugNameFieldSubLable = document.createElement('label');
    drugNameFieldSubLable.textContent = 'د درمل ډول'+count;

    let drugNameFieldSubSelect = document.createElement('select');
    drugNameFieldSubSelect.classList.add('form-control');
    drugNameFieldSubSelect.name = 'medicine_type';
    drugNameFieldSubSelect.dir = 'rtl';
    for (const med of medicine) { drugNameFieldSubSelect.appendChild(med); }

    drugNameFieldSub.append(drugNameFieldSubLable);
    drugNameFieldSub.append(drugNameFieldSubSelect);

    drugNameField.append(drugNameFieldSub);


    // the price input div
    priceField = document.createElement('div');
    priceField.classList.add('col-md-2');

    // the quantity input div
    quantityField = document.createElement('div');
    quantityField.classList.add('col-md-2');


    // appending the tree
    row.append(drugNameField);
    parent.append(row);
    count++;
}