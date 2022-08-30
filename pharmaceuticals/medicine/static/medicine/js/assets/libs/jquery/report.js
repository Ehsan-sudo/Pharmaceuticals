let reportSaveBtn = document.getElementById('save-image-btn');

let today = new Date();
let date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
let time = today.getHours() + ":" + today.getMinutes();
let dateTime = date+' '+time;

reportSaveBtn.onclick = (e) => {
    reportSaveBtn.innerHTML = 'یوه شېبه...';
    let div = document.getElementById('report-area');

    // Use the html2canvas
    // function to take a screenshot
    // and append it
    // to the output div
    document.getElementById('report-datetime').innerHTML = dateTime;
    html2canvas(div, {scale:2}).then(
        function (canvas) {
            let divHeight = $('#report-area').height();
            let divWidth = $('#report-area').width();
            let ratio = divHeight / divWidth;

            let doc = new jsPDF(); // using defaults: orientation=portrait, unit=mm, size=A4
            let width = doc.internal.pageSize.getWidth();    
            let height = doc.internal.pageSize.getHeight();
            height = ratio * width;
            doc.addImage(canvas, 'JPEG', 0, 0, width-20, height);
            doc.save('report'+dateTime+'.pdf'); //Download the rendered PDF.

            reportSaveBtn.innerHTML = 'ترسره سو!';
            // documcanvasetime').innerHTML = '';
        }
    );
    
}