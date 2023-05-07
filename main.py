import datetime
import requests

def check_billing(api_key):
    now = datetime.datetime.now()
    start_date = (now - datetime.timedelta(days=90)).strftime("%Y-%m-%d")
    end_date = (now + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    sub_date = datetime.datetime(now.year, now.month, 1).strftime("%Y-%m-%d")

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    try:
        response = requests.get(f"https://api.openai.com/v1/dashboard/billing/subscription", headers=headers)
        response.raise_for_status()
        total_amount = response.json()["hard_limit_usd"]

        if total_amount > 20:
            start_date, url_usage = sub_date, f"https://api.openai.com/v1/dashboard/billing/usage?start_date={sub_date}&end_date={end_date}"
            response = requests.get(url_usage, headers=headers)
            response.raise_for_status()
            total_usage = response.json()["total_usage"] / 100
        else:
            total_usage = 0

        remaining = total_amount - total_usage

        url_models = "https://api.openai.com/v1/models"
        response = requests.get(url_models, headers=headers)
        response.raise_for_status()
        models = response.json()["data"]
        can_access = any(model["id"] == "gpt-4" for model in models)

        print(f"总额度: {total_amount:.2f}美元\n已用额度: {total_usage:.2f}美元\n剩余额度: {remaining:.2f}美元\nAPI Key: {api_key} {'可以' if can_access else '不能'}访问 GPT-4""\n")

        return [total_amount, total_usage, remaining, can_access]
    except Exception as e:
        print(f"查询失败: {e}")
        return [None, None, None, False]

if __name__ == '__main__':
    with open('apikey.txt', 'r') as f:
        api_keys = f.read().splitlines()
    for api_key in api_keys:
        check_billing(api_key)
