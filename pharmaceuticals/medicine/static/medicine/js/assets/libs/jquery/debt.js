// debt statistics
let $debtChart = $("#debt-chart");
let ctx = $debtChart[0].getContext("2d");

new Chart(ctx, {
    type: 'bar',
    data: {
        labels: data.labels,
        datasets: [{
            label: 'پاته پور',
            backgroundColor: 'rgb(46, 184, 138)',
            data: data.data
            }]    
    },
    options: {
        responsive: true,
        legend: {
            position: 'top',
        }
    }
});
