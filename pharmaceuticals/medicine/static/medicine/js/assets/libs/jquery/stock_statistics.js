// stock statistics
let $stockChart = $("#stock-chart");
let ctx = $stockChart[0].getContext("2d");

new Chart(ctx, {
    type: 'bar',
    data: {
        labels: data.labels,
        datasets: [{
            label: 'پاته درمل',
            backgroundColor: 'green',
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
