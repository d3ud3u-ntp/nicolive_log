console.log("load");
// ページ内の全ての画像要素を取得
const images = document.querySelectorAll('img');

const canvas = document.createElement('canvas');
const ctx = canvas.getContext('2d');

// フォントをロードする
// const font = new FontFace('abea', 'url(chrome-extension://__MSG_@@extension_id__/abea.ttf)');
const font = new FontFace('abea', 'url(chrome-extension://__MSG_@@extension_id__/aboutaxmas.ttf)');
document.fonts.add(font);
// フォントが読み込まれたことを確認
// 各画像要素に対して処理を行う
for (const img of images) {
  // 画像が読み込まれた後に処理を実行
//   img.addEventListener('load', () => {
    canvas.width = img.width;
    canvas.height = img.height;
    ctx.drawImage(img, 0, 0);
    
    font.load().then(loadedFont => {
      document.fonts.add(loadedFont);
      ctx.font = '100px about a Xmas';

      // ランダムな点を100回選択し、その点の色を取得して「A」を描画
      for (let i = 0; i < 100; i++) {
        const x = Math.floor(Math.random() * canvas.width);
        const y = Math.floor(Math.random() * canvas.height);
        console.log("x="+x);
        console.log("y="+y);
        const pixelData = ctx.getImageData(x, y, 1, 1).data;
        console.log("pixel="+pixelData);
        const r = pixelData[0];
        const g = pixelData[1];
        const b = pixelData[2];
        const color = `rgb(${r}, ${g}, ${b})`;

        //   ctx.font = '20px Arial';
        ctx.fillStyle = color;
        ctx.fillText('A', x, y);
      }
    });
    

    // 処理後の画像をページに反映
    const processedImage = new Image();
    processedImage.src = canvas.toDataURL();
    img.parentNode.replaceChild(processedImage, img);
//   });
};
