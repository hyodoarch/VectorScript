# ha_ｉｊ方向移動・複製

## 対応環境

- Windows 64bit上のVectorworks 2026用。SDK追加関数は2026 SDKのRelease/x64ビルドです。
- 開発時の確認環境はVectorworks Architect 2026です。
- macOS、Windows ARMネイティブ、他のVectorworks年度・製品構成では動作未確認です。
- 作者による配布版のインストール・動作確認済みです。他のPC環境での動作は未確認です。

## インストール

1. Releasesから `ha_ij_direction-v0.1.0-vw2026-windows-x64.zip` をダウンロードして解凍します。
2. Vectorworksを終了します。
3. 解凍した `ha_ij_direction` フォルダーを、そのままユーザーのPlug-insフォルダーへコピーします。

標準のコピー先（エクスプローラーのアドレス欄に入力できます）:

```text
%APPDATA%\Nemetschek\Vectorworks\2026\Plug-ins
```

配置結果:

```text
Plug-ins/
  ha_ij_direction/
    ha_ｉｊ方向移動.vsm
    ha_ｉｊ方向移動.vss
    ha_MeasureDistance.px
    ha_PickReferenceAngle.px
    ha_ij_direction.vwr
    ha_VSFunctions.vlb
    ha_VSFunctions.vwr
    LICENSE ...
```

ユーザーフォルダーを変更している場合は、Vectorworksの環境設定で実際のユーザーフォルダーを確認してください。
個人名を含むパスを書き換える必要はありません。各INCLUDEは同じフォルダーのファイル名を参照します。
ファイルの一部だけを取り出したり、ファイル名を変更したりしないでください。

4. Vectorworksを起動します。未確認の開発元に関する確認画面が出た場合は、配布元とファイルを確認して扱いを選びます。
5. 「ツール → 作業画面 → 作業画面の編集」で、メニューコマンド `ha_ｉｊ方向移動` を任意のメニューへ追加します。
   カテゴリー名は `ha_斜め作図支援PRO` です。必要ならショートカットを割り当てます。

古い同名プラグインやSDK追加関数が別フォルダーにあると、古い方が読み込まれる場合があります。
既存版はバックアップしてPlug-ins検索対象の外へ移し、重複を避けてください。
配布版の利用だけならSDK・Visual Studio・Pythonのインストールは不要です。
実行時はVectorworks付属のVWMM.dllとWindows/MSVCのランタイムを使用します。
VCランタイム不足が表示された場合はMicrosoft公式のVisual C++ x64再頒布可能パッケージを使用してください。

## 使い方

1. 対象図形を選択し、`ha_ｉｊ方向移動` を実行します。
2. 距離、複製数、基準線の傾きを設定します。i方向は基準線に沿う方向、j方向はその直交方向です。
3. 矢印キーまたは矢印ボタンで移動、Ctrlを押しながらの操作で複製します。

- 「線の傾きの取得」: 図面の直線をクリックし、角度を入力します。
- 「距離計測ツール」: 2点を指定し、△L・△X・△Yを選択すると約1秒後に距離欄へ戻します。
  △Lは2点間距離、△Xと△Yは図面のX/Y座標差の絶対値です。i/j方向への投影距離ではありません。
- 計測や角度取得の際、複製数と入力内容を保持します。
- 履歴は図面内の `ha_ij_direction_history` ワークシートに保存します。距離は縮尺ごと、角度は図面共通です。
- 角度はθ/tanθを切り替えられます。垂直線はθ方式で扱います。
- 点取得中のEscはVectorworks側でコマンド全体を終了する場合があります。

## 確認していただきたい項目

- 他の場所にある開発版へ依存せず、上記フォルダーのみでコマンドが読み込まれること。
- 矢印画像が表示され、通常操作で移動、Ctrl操作で指定数の複製ができること。
- X差300、Y差400の点で△L=500、△X=300、△Y=400を取得できること。
- 線の傾き取得、履歴の保存、再起動後の読み込みができること。

## 更新・アンインストール

Vectorworksを終了し、配布フォルダーをバックアップしたうえで新しいフォルダーへ置き換えます。
アンインストール時は作業画面からコマンドを外し、Vectorworks終了後に配布フォルダーを取り除きます。
図面内に保存した履歴ワークシートはそのまま残ります。

## 配布条件・問い合わせ

`LICENSE` に対象別の条件を記載しています。SDK追加関数を含むZIP全体の転載は許諾していません。
配布先: https://github.com/hyodoarch/VectorScript/releases
不具合報告: https://github.com/hyodoarch/VectorScript/issues

公式資料: [スクリプトプラグインの配置とINCLUDE検索](https://app-help.vectorworks.net/2026/eng/VW2026_Guide/Scripts/Concept_Scripted_plug-ins.htm)
