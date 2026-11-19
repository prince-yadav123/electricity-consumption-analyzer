import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data():
    try:
        df = pd.read_csv("usage.csv")
    except FileNotFoundError:
        print("Error: usage.csv not found!")
        return None
    valid = []
    for i, row in df.iterrows():
        try:
            u = float(row["Units"])
        except:
            print(f"Row {i+2} skipped: invalid Units '{row['Units']}'.")
            continue
        if u < 0:
            print(f"Row {i+2} skipped: Units cannot be negative.")
            continue
        valid.append({"Month": str(row["Month"]), "Units": u})
    if not valid:
        print("No valid data found!")
        return None
    print(f"Valid rows: {len(valid)} | Total: {len(df)}")
    return pd.DataFrame(valid)

def summary(df):
    u = df["Units"].to_numpy()
    total = np.sum(u)
    avg = np.mean(u)
    sd = np.std(u)
    mx = np.max(u)
    mn = np.min(u)
    h = df[df["Units"] == mx]["Month"].values[0]
    l = df[df["Units"] == mn]["Month"].values[0]
    print("\n--- Summary ---")
    print(f"Total: {int(total)} units | Average: {avg:.2f}")
    print(f"Highest: {h} ({int(mx)}) | Lowest: {l} ({int(mn)})")
    print(f"Std Dev: {sd:.2f}")

def above_and_chart(df):
    avg = np.mean(df["Units"].to_numpy())
    above = df[df["Units"] > avg]
    print(f"\nMonths above average ({avg:.2f}): ", end="")
    if len(above) == 0:
        print("None")
    else:
        for _, r in above.iterrows():
            print(f"{r['Month']} ({int(r['Units'])})", end="  ")
        print()
    plt.figure()
    plt.bar(df["Month"], df["Units"])
    plt.title("Monthly Consumption")
    plt.xlabel("Month")
    plt.ylabel("Units")
    plt.show()
    plt.figure()
    plt.plot(df["Month"], df["Units"], marker="o")
    plt.title("Electricity Consumption Trend")
    plt.xlabel("Month")
    plt.ylabel("Units")
    plt.show()

def main():
    df = load_data()
    if df is None:
        return
    while True:
        print("\n--- Electricity Consumption Analyzer ---")
        print("1. Summary")
        print("2. Above-average months and chart")
        print("3. Show Charts Only")
        print("4. Exit")
        ch = input("Enter choice: ")
        if ch == "1":
            summary(df)
        elif ch == "2" or ch == "3":
            above_and_chart(df)
        elif ch == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()