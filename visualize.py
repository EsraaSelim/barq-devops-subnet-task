import pandas as pd
import matplotlib.pyplot as plt

def plot_subnet_hosts():
    subnet_summary = pd.read_csv("subnet_report.csv")
    plt.figure(figsize=(10, 6))
    plt.bar(subnet_summary["CIDR Notation"], subnet_summary["Usable Hosts"], color="blue")
    plt.xlabel("CIDR Notation")
    plt.ylabel("Usable Hosts")
    plt.title("Usable Hosts per Subnet")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("network_plot.png")
    plt.show()

if __name__ == "__main__":
    plot_subnet_hosts()

