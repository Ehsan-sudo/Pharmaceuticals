let reportPdfBtn = document.getElementById('save-pdf-btn');
let reportDataBtn = document.getElementById('save-data-btn');
// let tableData = document.getElementById('table-data');

let today = new Date();
let date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
let time = today.getHours() + ":" + today.getMinutes();
let dateTime = date+' '+time;

reportPdfBtn.onclick = (e) => {
    reportPdfBtn.innerHTML = 'صبر...';
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
            doc.save(reportName+'-'+dateTime+'.pdf'); //Download the rendered PDF.

            reportPdfBtn.innerHTML = 'PDF <i class="mdi mdi-archive-arrow-down me-1"></i>';
            // documcanvasetime').innerHTML = '';
        }
    );
    
}


reportDataBtn.onclick = () => {
    $("#table-data").table2excel({
        // exclude CSS class
        exclude:".noExl",
        name:"Worksheet Name",
        filename:reportName+'-'+dateTime,//do not include extension
        fileext:".xls" // file extension
    });
}