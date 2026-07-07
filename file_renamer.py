import os, re, argparse

def rename_files(directory, pattern, start=1):
    files = sorted([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])
    for i, filename in enumerate(files, start=start):
        ext = os.path.splitext(filename)[1]
        new_name = pattern.format(n=i, name=os.path.splitext(filename)[0]) + ext
        src = os.path.join(directory, filename)
        dst = os.path.join(directory, new_name)
        if src != dst:
            os.rename(src, dst)
            print(f"  {filename} -> {new_name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bulk file renamer")
    parser.add_argument("--dir", required=True, help="Target directory")
    parser.add_argument("--pattern", default="{n:04d}", help="Name pattern e.g. file_{n:04d}")
    parser.add_argument("--start", type=int, default=1)
    args = parser.parse_args()
    rename_files(args.dir, args.pattern, args.start)
    print("Done.")
