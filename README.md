# Local Chat Messanger

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

クライアントとサーバの間でメッセージを双方向に送信できるアプリケーション

## Usage Examples and Demos

Comming Soon...

## Desciption

このアプリケーションは、クライアントサーバ間で情報のやりとりができるシンプルなアプリケーションです。

このアプリケーションでは、メッセージの送信と受信を体験できます。

Client(ユーザ)がメッセージを送信すると、Server はそのメッセージを受け取り、何らかのメッセージを返してくれます。

サーバから返されるメッセージは、フェイクデータなので送信したメッセージの正確な返答ではありません。

例. 送信:Hello! / 受信: Google is one of the big tech!

基本的な機能として、メッセージの送信と受信ができます。

## Getting Started (Installation)

### Requierements

Python3, pip がインストールされている必要があります。  
実行例のように何らかのパスが帰って来れば OK です。

```zsh
% which python3
/opt/homebrew/opt/python@3.10/libexec/bin/python3

% which pip3
/opt/homebrew/opt/python@3.10/libexec/bin/pip3
```

次に仮想環境の準備と Faker パッケージを仮想環境内にインストールします。
Python のパッケージマネージャである pip はモジュールやライブラリ同士の依存関係を簡単に壊します。
そのため、使い捨ての仮想環境を作成し、その中でプログラムを動作させるのが作法です。  
以下のコマンドを実行してください。

```zsh
% python3 -m venv venv # venvという名前の仮想環境をvenvパッケージを使って作成

% source venv/bin/activate
(venv) % # 左のように表示されていれば仮想環境の中に入れている

% pip3 install Faker
```

これらがインストールされていることを確認できたら、以下のコマンドを実行してください。

## Why I made this ?

TCP や UDP などのトランスポート層プロトコルを用いた通信技術を Recursion で学びました。
学んだ知識を定着させるためにアウトプットとして簡単なアプリケーション Local Chat Messanger を作成しました。
アウトプットの一環として行ったため、ドメイン等を取得するつもりはありません。
