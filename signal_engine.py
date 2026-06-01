from storage import load_signals, save_signals

def generate_signal():

    data = load_signals()

    data["signal"] = "WAIT"
    data["confidence"] = 0

    save_signals(data)

    return data
