
const COLORS = ['rgb(140, 214, 16)', 'rgb(239, 198, 0)', 'rgb(231, 24, 49)'];

function index(perc) {
  if (perc <= 50) return 0;
  if (perc <= 80) return 1;
  return 2;
}

const baseConfig = {
  type: 'doughnut',
  options: {
    aspectRatio: 2,
    circumference: 180,
    rotation: -90
  }
};

function createGaugeChart(canvasId) {
  const canvas = document.getElementById(canvasId);
  const value = Number(canvas.dataset.value);

  const data = {
    datasets: [{
      data: [value, 100 - value],
      backgroundColor(ctx) {
        if (ctx.type !== 'data') return;
        if (ctx.index === 1) return 'rgb(234, 234, 234)';
        return COLORS[index(ctx.raw)];
      }
    }]
  };

  const config = structuredClone(baseConfig);
  config.data = data;

  return new Chart(canvas, config);
}

createGaugeChart('cpu_chart');
createGaugeChart('memory_chart');

/* ----------------------------------------------------------------------- */

const fileCanvas = document.getElementById('file_chart');
const txtCount = Number(fileCanvas.dataset.txt);
const pyCount = Number(fileCanvas.dataset.py);
const pdfCount = Number(fileCanvas.dataset.pdf);
const jpgCount = Number(fileCanvas.dataset.jpg);
const totalFiles = Number(fileCanvas.dataset.total);

const labels = ['txt', 'py', 'pdf', 'jpg'];
const data = {
  labels: labels,
  datasets: [{
    label: 'Nombre de fichiers',
    data: [txtCount, pyCount, pdfCount, jpgCount],
    backgroundColor: [
      'rgba(255, 99, 132, 0.2)',
      'rgba(255, 159, 64, 0.2)',
      'rgba(255, 205, 86, 0.2)',
      'rgba(75, 192, 192, 0.2)'
    ],
    borderColor: [
      'rgb(255, 99, 132)',
      'rgb(255, 159, 64)',
      'rgb(255, 205, 86)',
      'rgb(75, 192, 192)'
    ],
    borderWidth: 1
  }]
};

const configFileChart = {
  type: 'bar',
  data: data,
  options: {
    scales: {
      y: {
        beginAtZero: true,
        max: totalFiles
      }
    }
  },
};

new Chart(fileCanvas, configFileChart);