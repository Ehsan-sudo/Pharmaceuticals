$(function () {
    let $stockChart = $("#stock-chart");
    $.ajax({
      url: $stockChart.data("url"),
        success: function (data) {

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

        }
    });

});