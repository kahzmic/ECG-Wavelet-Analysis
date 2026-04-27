import wfdb
import numpy as np
import matplotlib.pyplot as plt


def extract_rr_with_labels(record_name: str, pn_dir: str = 'mitdb'):
    record = wfdb.rdrecord(record_name, pn_dir=pn_dir)
    annotation = wfdb.rdann(record_name, 'atr', pn_dir=pn_dir)

    fs = record.fs
    sample_indices = annotation.sample
    symbols = annotation.symbol

    beat_symbols = set('NLRBAaJSVrFejnE/fQ')
    mask = [s in beat_symbols for s in symbols]
    beat_samples = sample_indices[mask]
    beat_labels = [s for s, m in zip(symbols, mask) if m]

    rr_intervals = np.diff(beat_samples) / fs * 1000  # ms
    rr_labels = beat_labels[1:]

    return rr_intervals, rr_labels


def plot_nn_intervals(rr_intervals, rr_labels, record_name: str):
    """ Normal RR intervals (label 'N') are plotted to visualize heart rate variability. """

    nn = np.array([rr for rr, lbl in zip(rr_intervals, rr_labels) if lbl == 'N'])
    idx = np.arange(len(nn))
    fig, ax = plt.subplots(figsize=(14, 4))
    ax.scatter(idx, nn, s=50)
    ax.set_xlabel('RR beat index')
    ax.set_ylabel('RR interval (ms)')
    ax.set_title(f'RR intervals - MIT-BIH Record {record_name}')
    plt.tight_layout()
    plt.show()