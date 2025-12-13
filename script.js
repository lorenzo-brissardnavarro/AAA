
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
const htmlCount = Number(fileCanvas.dataset.html);
const cssCount = Number(fileCanvas.dataset.css);
const jsCount = Number(fileCanvas.dataset.js);
const pngCount = Number(fileCanvas.dataset.png);
const totalFiles = Number(fileCanvas.dataset.total);

const labels = ['txt', 'py', 'pdf', 'jpg', 'html', 'css', 'js', 'png'];
const data = {
  labels: labels,
  datasets: [{
    label: 'Nombre de fichiers',
    data: [txtCount, pyCount, pdfCount, jpgCount, htmlCount, cssCount, jsCount, pngCount],
    backgroundColor: [
  'rgba(255, 99, 132, 0.2)',
  'rgba(255, 159, 64, 0.2)',
  'rgba(255, 205, 86, 0.2)',
  'rgba(75, 192, 192, 0.2)',
  'rgba(54, 162, 235, 0.2)',
  'rgba(153, 102, 255, 0.2)',
  'rgba(201, 203, 207, 0.2)',
  'rgba(0, 128, 128, 0.2)'
],
borderColor: [
  'rgb(255, 99, 132)', 
  'rgb(255, 159, 64)', 
  'rgb(255, 205, 86)', 
  'rgb(75, 192, 192)', 
  'rgb(54, 162, 235)',  
  'rgb(153, 102, 255)', 
  'rgb(201, 203, 207)',
  'rgb(0, 128, 128)'
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