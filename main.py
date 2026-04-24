import wfdb

def main():
    # Download and read a WFDB record from PhysioNet
    record = wfdb.rdrecord('104', pn_dir='mitdb')

    # Plot the signal
    wfdb.plot_wfdb(record=record, title='Record 100 from MIT-BIH Arrhythmia Database')


if __name__ == "__main__":
    main()
