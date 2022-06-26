submitButton = document.getElementById('submit');
parent = document.getElementById('parent-div-for-rows');
addRow = document.getElementById('addRow');
removeRow = document.getElementById('removeRow');
grandTotal = document.getElementById('grand-total');
customer = document.getElementById('customer_purchase_customers');


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
submitButton.onclick = function(){
    let selections = preparePurchaseData();

    // ajax call
    $.ajax({
        url: url_to,
        type: 'POST',
        headers: {'X-CSRFToken': csrftoken},
        contentType: 'application/json; charset=UTF-8',
        async: false, 
        data: JSON.stringify(selections),
        dataType: 'json',
        success: (response)=>{
            console.log('success response!');
            console.log(response);
        },
        'error': (response)=>{
            console.log('error response!');
            console.log(response);
        }
    });
};

const preparePurchaseData = () => {
    let selections = {'selections':[], 'customer':-1};
    for(let i=0;i<parent.childNodes.length;i++){
        let selectedDrugID = parent.childNodes[i].childNodes[0].childNodes[0].childNodes[0].value;
        let price = parent.childNodes[i].childNodes[1].childNodes[0].childNodes[0].value;
        let quantity = parent.childNodes[i].childNodes[2].childNodes[0].childNodes[0].value;
        selections['selections'].push({'id':selectedDrugID, 'price':price, 'quantity':quantity})
        selections['customer'] = customer.value;
    }
    return selections;
}

// ----------------------------------------------

// -----  Price & Quantity ONCHANG -----------
countRows = 0;
const priceOnChange = (e) => {
    let quantity = parseInt(e.path[3].childNodes[2].childNodes[0].childNodes[0].value);
    if (isNaN(quantity)){
        quantity = 1;
    }
    let price = e.target.value;
    e.path[3].childNodes[3].childNodes[0].childNodes[0].innerHTML = quantity*price;
    updateGrandTotalAdd();
}
const quantityOnChange = (e) => {
    let price = parseInt(e.path[3].childNodes[1].childNodes[0].childNodes[0].value);
    if (isNaN(price)){
        price = 1;
    }
    let quantity = e.target.value;
    e.path[3].childNodes[3].childNodes[0].childNodes[0].innerHTML = quantity*price;
    updateGrandTotalAdd();
}
const updateGrandTotalAdd = () => {
    let gt = 0;
    for(let i=0;i<parent.childNodes.length;i++){
        gt += parseInt(parent.childNodes[i].childNodes[3].childNodes[0].childNodes[0].innerHTML);
    }
    grandTotal.innerHTML = gt;
}
const updateGrandTotalRemove = () => {
    let amount = parseInt(parent.lastChild.childNodes[3].childNodes[0].childNodes[0].innerHTML);
    grandTotal.innerHTML = parseInt(grandTotal.innerHTML)-amount;
}

// ----- AddRow ONCLICK ----------
addRow.onclick = (e) => {
    parent.append(rowCreate());
}
const rowCreate = () => {
    // creat base div
    let row = document.createElement('div');
    row.classList.add('row');

    // the drug name input div
    let drugNameField = document.createElement('div');
    drugNameField.classList.add('col-md-5');

    let drugNameFieldSub = document.createElement('div');
    drugNameFieldSub.classList.add('mb-3', 'position-relative', 'pashto');

    let drugNameFieldSubSelect = document.createElement('select');
    drugNameFieldSubSelect.classList.add('form-control');
    drugNameFieldSubSelect.dir = 'rtl';
    for (const med in medicine) {
        option = document.createElement('option');
        option.value = med;
        option.innerHTML = medicine[med].name;
        drugNameFieldSubSelect.append(option);
    }
    drugNameFieldSubSelect.onclick = drugNameSelect;

    drugNameFieldSub.append(drugNameFieldSubSelect);

    drugNameField.append(drugNameFieldSub);

     // the price input div
    priceField = document.createElement('div');
    priceField.classList.add('col-md-2');

    priceFieldSub = document.createElement('div');
    priceFieldSub.classList.add('mb-3', 'position-relative', 'pashto');

    let priceFieldSubInput = document.createElement('input');
    priceFieldSubInput.classList.add('form-control');
    priceFieldSubInput.onchange = priceOnChange;
    priceFieldSubInput.type = "number";
    priceFieldSubInput.placeholder = "بیه";

    priceFieldSub.append(priceFieldSubInput);

    priceField.append(priceFieldSub);


    // the quantity input div
    quantityField = document.createElement('div');
    quantityField.classList.add('col-md-2');

    quantityFieldSub = document.createElement('div');
    quantityFieldSub.classList.add('mb-3', 'position-relative', 'pashto');

    let quantityFieldSubInput = document.createElement('input');
    quantityFieldSubInput.classList.add('form-control');
    quantityFieldSubInput.type = "number";
    quantityFieldSubInput.placeholder = "تعداد";
    quantityFieldSubInput.onchange = quantityOnChange;

    quantityFieldSub.append(quantityFieldSubInput);

    quantityField.append(quantityFieldSub);

    // the total input div
    totalField = document.createElement('div');
    totalField.classList.add('col-md-2');

    totalFieldSub = document.createElement('div');
    totalFieldSub.classList.add('mb-3', 'position-relative', 'pashto');

    let totalFieldSubValue = document.createElement('label');
    totalFieldSubValue.textContent = '0';
    totalFieldSubValue.classList.add('mb-0', 'mt-2');

    totalFieldSub.append(totalFieldSubValue);
    totalField.append(totalFieldSub);

    hr = document.createElement('hr');
    hr.style = "height:2px;text-align:left;margin-left:0;margin-left:0;";
    // appedning all the dives to parent div
    row.append(drugNameField);
    row.append(priceField);
    row.append(quantityField);
    row.append(totalField);
    row.append(hr);

    countRows++;
    return row;
}

// ----- RemoveRow ONCLICK --------
removeRow.onclick = () =>{
    if(parent.hasChildNodes()){
        updateGrandTotalRemove();
        parent.removeChild(parent.lastChild);
    }
}

// ------ Drug name select onchange --------
const drugNameSelect = (e) => {
    e.path[3].childNodes[1].childNodes[0].childNodes[0].value = null;
    e.path[3].childNodes[1].childNodes[0].childNodes[0].placeholder = medicine[e.target.value].price;
}