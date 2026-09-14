# VectorScript

兵藤善紀建築設計事務所のVectorworks用プラグイン公開リポジトリです。
現在の公開対象は **ha_ｉｊ方向移動・複製** のみです。

斜め方向の移動・複製、図面からの距離・傾き取得、距離・角度履歴をひとつのダイアログで利用できます。

- [ダウンロード（Releases）](https://github.com/hyodoarch/VectorScript/releases)
- [対応環境・インストール・使い方](plugins/ha_ij_direction/README.md)
- [ライセンスの適用範囲](LICENSE)
- [配布内容と検証記録](VALIDATION.md)

Windows 64bit / Vectorworks 2026向けのプレビュー版です。配布形式での実機確認はまだ完了していません。
通常の導入にはReleasesの配布ZIPを使用してください。GitHubの「Source code (zip)」はリポジトリ全体で、配置構造が異なります。

## フォルダー構成

- `plugins/ha_ij_direction/`: 配置用プラグインと必須ファイル一式
- `resources/ha_ij_direction/Images/`: 矢印画像の編集用原本（配置用VWRにも収録済み）
- `tools/build_zip.py`: 標準Pythonのみで配布ZIP・SHA-256一覧を作成するスクリプト

SDK本体、SDKのヘッダー・サンプルソース、他の自作プラグイン、開発リポジトリの履歴は含めていません。
スクリプト等はMIT、SDK追加関数は別規約です。リポジトリ全体がMITライセンスではありません。

## 配布ZIPの再作成（作者用）

```text
python tools/build_zip.py
```

`dist/` にZIPとSHA-256を作成します。SDK追加関数の再配布権を第三者へ与えるコマンドではありません。
