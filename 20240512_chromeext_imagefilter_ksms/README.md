# Chrome Extensionで画像にくそみそフィルターをかける

- Chrome Extension のネタが降ってきたので、できるかわからんがつくる

ChromeExtensionで以下のプログラムを実現したいです。
・画像の色を点でランダムで取得して、その点を中心として、「A」という文字を画像に描画。この処理は100回行われる
・abea.ttfというオリジナルフォントの「A」という文字を描画する
・ページ内の画像にすべて加工を施す。

JavaScriptでloadを使わずにFontFaceを読み込む方法
ChromeExtensionでFontFaceを読み込む方法を3つ