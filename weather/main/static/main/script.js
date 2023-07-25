const ctx = document.getElementById("myChart");

new Chart(ctx, {
    type: "line",
    data: {
        labels: [
			"04:00",
            "08:00",
            "12:00",
            "16:00",
            "20:00",
            "00:00",
        ],
        datasets: [
            {
                label: "Температура воздуха",
                data: [-11, 9, 12, 4, 11, 36, 7],
                borderColor: "#4cd3aa",
                backgroundColor: "#4cd3aa",
                borderWidth: 2,
            },
        ],
    },
    options: {
        plugins: {
            legend: {
                display: false,
            },
            tooltip: false,
        },
    },
});

flatpickr("#data-input", {
    locale: "ru",
    allowInput: true,
    altInput: true,
    altFormat: "F j, Y",
    dateFormat: "Y-m-d",
    wrap: true,
});