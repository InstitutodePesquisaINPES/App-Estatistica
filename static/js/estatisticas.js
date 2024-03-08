/* Login activate */
document.addEventListener('DOMContentLoaded', function() {
    const userIcon = document.getElementById('userIcon');
    const userBox = document.getElementById('userBox');
    const closeBox = document.getElementById('closeBox');

    userIcon.addEventListener('click', function() {
        userBox.style.display = 'block';
    });

    closeBox.addEventListener('click', function() {
        userBox.style.display = 'none';
    });
});


/* Estatística */


// Seu código Chart.js
const data = {
    labels: ['Label 1', 'Label 2', 'Label 3', 'Label 4'],
    datasets: [{
        label: 'Dataset Label',
        data: [12, 19, 3, 5],
        fill: false,
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1
    }]
};

const config = {
    type: 'line',
    data: data,
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'Chart.js Line Chart'
            }
        }
    },
};

// Criar o gráfico
const myChart = new Chart(document.getElementById('myChart'), config);


// Gráfico 2 

const data2 = {
    labels: ['Label 1', 'Label 2', 'Label 3', 'Label 4'],
    datasets: [{
        label: 'Dataset Label',
        data: [
            { x: 'Label 1', y: 12 },
            { x: 'Label 2', y: 19 },
            { x: 'Label 3', y: 3 },
            { x: 'Label 4', y: 5 }
        ],
        backgroundColor: 'rgba(75, 192, 192, 0.5)', // Cor de preenchimento dos círculos
        borderColor: 'rgb(75, 192, 192)',
    }]
};

const config2 = {
    type: 'scatter', // Tipo de gráfico de dispersão (círculos)
    data: data2,
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'Chart.js Scatter Chart'
            }
        },
        scales: {
            x: {
                type: 'category',
                labels: ['Label 1', 'Label 2', 'Label 3', 'Label 4']
            },
            y: {
                beginAtZero: true
            }
        }
    },
};

// Criar o gráfico
const myChart2 = new Chart(document.getElementById('myChart2'), config2);


