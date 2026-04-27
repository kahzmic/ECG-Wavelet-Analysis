from src.rr_extraction import extract_rr_with_labels, plot_nn_intervals

RECORD = '104'

def main():
    rr_intervals, rr_labels = extract_rr_with_labels(RECORD)
    plot_nn_intervals(rr_intervals, rr_labels, RECORD)


if __name__ == "__main__":
    main()
