# This tool analyzes and visualizes network data.

## To run it locally:

### Requirements:

- Python v3.11+ (i used v3.13.5 locally and v3.11 for the docker image)
- pip

1. Install Dependencies:

```bash
pip install pandas openpyxl matplotlib

```
2. Run subnet_analyzer.py (this step generates subnet_report.csv)

```bash
python subnet_analyzer.py

```
3. Visualize the subnets (this step generates network_plot.png)

```bash
python visualize.py

```

## To run with docker:

1. Build the docker image:

```bash
docker build -t subnet-analyzer .

```

2. Run subnet-analyzer

```bash
docker run --rm -v "$PWD:/app" subnet-analyzer

```

3. Run visualize.py

```bash 
docker run --rm -v "$PWD:/app" subnet-analyzer python visualize.py

```
