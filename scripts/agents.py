from datetime import datetime
import numpy as np
from card import Card, Category, CardGroup, action_space
from utils import to_char, to_value, get_mask_alter, give_cards_without_minor, \
    get_mask, action_space_single, action_space_pair, get_category_idx, normalize
import sys
import os
from datetime import datetime
from env import Env as CEnv


trans_dict = {'T': '10', 'B': '$', 'L': '*'}

def trans_cards(delta_cards):
    """将 deltadou 中的格式转化为当前程序中的格式
    """
    res = []

    for c in delta_cards:
        if c in trans_dict:
            res.append(trans_dict[c])
        else:
            res.append(c)

    return res

trans_dict_rev = {'10': 'T', '$': 'B', '*': 'L'}

def trans_cards_reverse(delta_cards):
    """将 deltadou 中的格式转化为当前程序中的格式
    """
    res = []

    for c in delta_cards:
        if c in trans_dict_rev:
            res.append(trans_dict_rev[c])
        else:
            res.append(c)

    return "".join(res)

from flask import Flask, jsonify, request
app = Flask(__name__)

# // 2 ：地主， 1： 地主上家，3：地主下家


@app.route('/AI/play/', methods=['POST'])
def ai_play():
    data = request.json
    print(data)
    pos = int(data['current_player'])

    player_cards = data['player_cards']
    my_cards = trans_cards( player_cards.split("|")[pos] )
    last_move = trans_cards(data['last_move'])
    if int(data['last_player']) == int(data['current_player']):
        last_move = []
    else:
        last_move = trans_cards(data['last_move'])


    intention = to_char(CEnv.step_auto_static(Card.char2color(my_cards), to_value(last_move)))

    res =  trans_cards_reverse(intention)
    if res == "":
        res = 'P'
    print("result is {}".format(res))
    return jsonify({'move': res})

if __name__ == '__main__':
    print('Running Flask Server')
    app.run(host='0.0.0.0', port=8098, debug=False)

