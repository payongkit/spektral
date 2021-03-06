from core import MODES, run_layer

from spektral import layers

config = {
    "layer": layers.ARMAConv,
    "modes": [MODES["SINGLE"], MODES["BATCH"], MODES["MIXED"]],
    "kwargs": {
        "channels": 8,
        "activation": "relu",
        "order": 2,
        "iterations": 2,
        "share_weights": True,
        "use_bias": True,
        "kernel_initializer": "zeros",
    },
    "dense": True,
    "sparse": True,
    "edges": False,
}


def test_layer():
    run_layer(config)
    config["kwargs"]["use_bias"] = False
    run_layer(config)
