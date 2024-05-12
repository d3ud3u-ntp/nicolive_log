// content.js
const images = document.querySelectorAll('img');

for (const image of images) {
  const canvas = document.createElement('canvas');
  const context = canvas.getContext('2d');

  canvas.width = image.width;
  canvas.height = image.height;
  context.drawImage(image, 0, 0);

  const imageData = context.getImageData(0, 0, canvas.width, canvas.height);
  const data = imageData.data;

  const blockSize = 8; // モザイクブロックのサイズ
  for (let y = 0; y < canvas.height; y += blockSize) {
    for (let x = 0; x < canvas.width; x += blockSize) {
      const baseIndex = (y * canvas.width + x) * 4;
      const avgColor = getAverageColor(data, baseIndex, blockSize, canvas.width);
      setBlockColor(data, baseIndex, blockSize, canvas.width, avgColor);
    }
  }

  context.putImageData(imageData, 0, 0);
  image.src = canvas.toDataURL();
}

function getAverageColor(data, baseIndex, blockSize, width) {
  let r = 0, g = 0, b = 0;
  const count = blockSize * blockSize;
  for (let i = 0; i < count; i++) {
    const offset = baseIndex + (i % blockSize) * 4 + Math.floor(i / blockSize) * width * 4;
    r += data[offset];
    g += data[offset + 1];
    b += data[offset + 2];
  }
  r = Math.round(r / count);
  g = Math.round(g / count);
  b = Math.round(b / count);
  return { r, g, b };
}

function setBlockColor(data, baseIndex, blockSize, width, { r, g, b }) {
  for (let i = 0; i < blockSize * blockSize; i++) {
    const offset = baseIndex + (i % blockSize) * 4 + Math.floor(i / blockSize) * width * 4;
    data[offset] = r;
    data[offset + 1] = g;
    data[offset + 2] = b;
  }
}