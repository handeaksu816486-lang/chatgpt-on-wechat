# -*- coding: utf-8 -*-
import os
import json
import signal
import sys
from channel import channel_factory
from common.log import logger
from config import conf, load_config

def sigterm_handler_wrap(signum, frame):
    sys.exit(0)

dify_config = {
    "channel_type": "wechatmp",
    "model": "dify",
    "dify_api_base": "https://api.dify.ai/v1",
    "dify_api_key": "app-4ULbJ79PaosvXZ2NDmP8Tyci",
    "dify_app_type": "chatbot",
    "wechatmp_app_id": "wx1d8ac1ac53a08a52",
    "wechatmp_app_secret": "351eb54bad3b9e9f59f9da094a8ee9ea",
    "wechatmp_aes_key": "krxI6Ud119fuEplvMMKiFD4fE06WuC3jIx4aMgn6Xt6",
    "wechatmp_token": "yj0523",
    "wechatmp_port": 8080
}

try:
    with open("config.json", "w") as f:
        json.dump(dify_config, f)
except Exception as e:
    pass

os.environ["MODEL"] = "dify"
os.environ["OPENAI_API_KEY"] = "sk-placeholder-for-dify"

def run():
    try:
        load_config()
        conf().set("model", "dify")
        channel_type = "wechatmp"
        channel = channel_factory.create_channel(channel_type)
        signal.signal(signal.SIGTERM, sigterm_handler_wrap)
        channel.startup()
    except Exception as e:
        sys.exit(1)

if __name__ == '__main__':
    run()
