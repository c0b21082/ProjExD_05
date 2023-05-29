# main

## 実行環境の必要条件
* python >= 3.10
* pygame >= 2.1

## ゲームの概要
ランダムに敵や障害物が生成される世界を、プレイヤーが箱や爆弾をなげたりジャンプしながら進んでいくゲーム

## ゲームの実装
### 共通基本機能
* class Player(pg.sprite.Sprite):
プレイヤーの初期化、移動の設定を行う

* class Block(pg.sprite.Sprite):
プレイヤーの投げる箱の設定

### 担当追加機能
* class Score(self):
時間経過で加算されるスコアの設定と表示

### ToDo
- [ ] def render_final(self)の完成

### memo
* 調べながら作ってはいるが、render_finalは期限までに完成しない可能性高