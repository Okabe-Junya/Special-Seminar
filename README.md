# 情報特別演習

<p align="left">
    <a href="#">
        <img src="https://img.shields.io/badge/-archive-red">
    </a>
    <a href="https://github.com/Okabe-Junya/Special-Seminar/blob/main/README_en.md">
        <img src="https://img.shields.io/badge/link-English-blue">
    </a>
</p>

## 概要

学部2年生で履修した[情報特別演習](https://kdb.tsukuba.ac.jp/syllabi/2021/GB13312/jpn/)に関するアーカイブ．
演習テーマとして『航空ネットワークのハブ配置最適化』を採用し，演習を行った．アドバイザ教員を[長谷部 浩二 先生](http://www.cs.tsukuba.ac.jp/~hasebe/)に務めていただいた．

### 情報特別演習に関する補足

学部1年生から3年生を対象とした授業（通年，2単位）で，履修した学生が自主的に設定したテーマで約半年間の演習（≒研究活動）を行う．ただし，卒業研究などの研究活動とは異なり，**新規性**は求められない（もちろん演習した内容をまとめ，報告書として提出する必要はある）．

## 演習内容

航空ネットワークにいくつかのハブ空港を配置することで，ネットワーク全体の総費用を最小化する **ハブ配置問題** をテーマに演習を行った．まず，ハブ配置問題に関する論文のサーベイを行った．並列して数理最適化に関する学習を行った．その後，既存のモデルを拡張し，新規モデルの提案及びその厳密解の導出を行った．厳密解の導出には，数理最適化ソルバー [Gurobi Optimizer](https://www.gurobi.com/products/gurobi-optimizer/) を用いた．

## スケジュール

演習は6月に開始し，翌年1月（2月）に終了する．基本的には2週間に1回（集団）ミーティングを実施し，進捗の報告を行う．その後アドバイスや質問を受ける．必要に応じて，随時アドバイザ教員との個別ミーティングを行う．

### 4~5月

アドバイザを務めてもらう先生への連絡．配属先の決定．

### 6月

演習の開始．演習テーマの決定，及び関連する分野の簡単な調査．

### 7~9月

中間発表（演習テーマや現時点での進捗報告）．数理最適化の学習の開始．該当分野に関する論文のサーベイ．

### 10~11月

新規モデルの作成，及びプログラムの実装．

### 12~1月

最終発表のためのプレゼンテーションや報告書の作成．ソースコードの軽微なバグの修正など．

### 2月

[最終報告書](https://github.com/Okabe-Junya/Special-Seminar/blob/main/Publications/Final_Report.pdf)の提出．演習の終了．

## ディレクトリ構成

本Repositoryは，以下のディレクトリ構成を持つ．

```text
.
├── Publications
│   ├── Final_Presentation.pdf
│   └── Final_Report.pdf
├── README.md
├── README_en.md
└── src
    ├── README
    ├── draw.py
    ├── my_def.py
    └── res
```

`Publications` フォルダ内に最終発表のプレゼンスライド，最終報告書がある．`src` フォルダ内に，提案したモデルに基づき実装したコードがある．
