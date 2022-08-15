# AWS Clean Up Tool

This tool lets you find services in AWS that have NOT been used / executed for a very long time and terminate those
services on demand

## List Of Services Supported

- Lambda

## System Requirements

Software packages you might require before running this app

- Python >= 3.9
- Git
- Conda / Venv ( I personally prefer to use conda environment)
- Vs Code / PyCharm

## Run Locally

Clone the project

```bash
  git clone https://github.com/AWSPersonal/clean-up.git
```

Go to the project directory

```bash
  cd clean-up
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the app

```bash
  python app.py
```


## Arguments Reference

|    Args     | Default                      | Description                                                                |
|:-----------:|:-----------------------------|:---------------------------------------------------------------------------|
| `--export`  | `false`                      | Lets you only the export all the list of services to a CSV file            |
| `--display` | `false`                      | Lets you only display the list of services as JSON on the terminal or bash |
| `--account` | `default value from .config` | Set which account to get the services from                                 |

To get more details for the arguments passed for the app, use the below command

```bash
  python app.py -h
```

## Authors

- [@devpoilath](https://www.linkedin.com/in/manjunath-pv-336232127/)

