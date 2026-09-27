# VectorScript

兵藤善紀建築設計事務所のVectorworks用プラグインです。
**ha_ｉｊ方向移動・複製** と **ha_ｉｊ方向頂点移動ツール** を、1つのフォルダーにまとめて配布します。

- [v0.2.0 ダウンロード](https://github.com/hyodoarch/VectorScript/releases/tag/v0.2.0)
- [対応環境・インストール・操作方法](plugins/ha_ij_direction/README.md)
- [ライセンスの適用範囲](LICENSE)
- [配布内容と検証記録](VALIDATION.md)

Windows x64 / Vectorworks 2026向けです。作者による統合配置での動作確認済みです。確認範囲は検証記録を参照してください。
通常の導入にはRelease添付の `ha_ij_direction-v0.2.0-vw2026-windows-x64.zip` を使用してください。GitHub自動生成のSource code (zip)とは配置構成が異なります。

## 収録機能

- 移動・複製：基準線に沿うi方向と直交するj方向へ、図形を移動・Ctrl操作で複製。
- 頂点移動：矩形で囲んだ選択図形の頂点をi/j方向へ移動。Ctrl操作でも複製しません。
- 共通機能：距離計測、直線の傾き取得、距離・角度履歴、θ／tanθ切替。

SDK追加関数 `ha_VSFunctions` は起動時の開発元確認で有効化し、Vectorworksを再起動してください。
旧単独候補版・重複ファイルの整理方法は同梱READMEを参照してください。

## フォルダー構成

- `plugins/ha_ij_direction/`：2機能と必要な共通ファイル一式
- `resources/ha_ij_direction/Images/`：矢印画像原本
- `resources/ha_ij_vertex_move/Images/`：頂点移動ツールのアイコン原本
- `tools/build_zip.py`：ZIP・SHA-256作成と静的検証

SDK本体、SDKヘッダー・サンプルソース、開発リポジトリの履歴は含みません。
スクリプト等はMIT、SDK追加関数は別規約です。リポジトリ全体がMITではありません。

## 配布ZIPの再作成（作者用）

```text
python tools/build_zip.py
python tools/build_zip.py --verify-only
```

`dist/` にZIPとSHA-256を出力します。SDK追加関数の再配布権を第三者へ与えるものではありません。
梱包対象の変更時は `package-sha256.json` を更新し、新しいバージョンを使用してください。
