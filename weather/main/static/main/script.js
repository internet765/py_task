const ctx = document.getElementById('myChart');
const form = document.getElementById('form');

let color = '#4cd3aa';
let cityWeather = {
	dates: ['04-03-2023', '05-03-2023', '06-03-2023'],
	t: [-11, 9, 12, 11, 11, 13],
};

form.addEventListener('input', (evt) => {
	console.log(evt.target.value);
	console.log(evt.currentTarget);
});

flatpickr('#data-input', {
	locale: 'ru',
	allowInput: true,
	altInput: true,
	altFormat: 'j F Y',
	dateFormat: 'd-m-Y',
	defaultDate: cityWeather.dates[0], // будем считать что это 'today'
	enable: cityWeather.dates,
	wrap: true,
});

new Chart(ctx, {
	type: 'line',
	data: {
		labels: ['04:00', '08:00', '12:00', '16:00', '20:00', '00:00'],
		datasets: [
			{
				data: cityWeather.t,
				borderColor: color,
				backgroundColor: color,
				borderWidth: 1,
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
