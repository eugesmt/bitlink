import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
from pathlib import Path
import argparse


def shorten_link(bitlly_token, user_link):
    bitlink_creation_endpoint = 'https://api-ssl.bitly.com/v4/bitlinks'
    headers = {
        'Authorization': f'Bearer {bitlly_token}'
    }
    payload = {
        'long_url': user_link
    }
    response = requests.post(
        url=bitlink_creation_endpoint,
        headers=headers,
        json=payload
    )
    response.raise_for_status()
    bitlink = response.json()['link']
    return bitlink


def parse_link(user_link):
    parsed_link = urlparse(user_link)
    netloc_path = f'{parsed_link.netloc}{parsed_link.path}'
    return netloc_path


def count_clicks(parsed_user_link, bitlly_token):
    headers = {
        'Authorization': f'Bearer {bitlly_token}'
    }
    total_clicks_endpoint = ('https://api-ssl.bitly.com/v4'
                             '/bitlinks/{netloc_path}/clicks/summary')
    total_clicks_url = total_clicks_endpoint.format(
        netloc_path=parsed_user_link
    )
    response = requests.get(url=total_clicks_url, headers=headers)
    response.raise_for_status()
    total_clicks = response.json()['total_clicks']
    return total_clicks


def is_bitlink(parsed_user_link, bitlly_token):
    headers = {
        'Authorization': f'Bearer {bitlly_token}'
    }
    bitlink_info_endpoint = 'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    bitlink_info_url = bitlink_info_endpoint.format(bitlink=parsed_user_link)
    response = requests.get(url=bitlink_info_url, headers=headers)
    return response.ok


def main():
    description_program = ('Программа сокращает длинные адреса сайтов,'
                           ' а если для сайта уже есть короткий адрес'
                           ' выводит адрес, если вводится короткий адрес,'
                           ' то возвращается количество кликов по'
                           ' данной ссылке.')
    parser = argparse.ArgumentParser(description=description_program)
    parser.add_argument(
        'user_link',
        help='URL-адрес сайта, введенный пользователем'
    )
    args = parser.parse_args()
    load_dotenv()
    bitlly_token = os.getenv('BITLY_TOKEN')
    user_link = args.user_link
    parsed_user_link = parse_link(user_link)
    if is_bitlink(parsed_user_link, bitlly_token):
        try:
            total_clicks = count_clicks(parsed_user_link, bitlly_token)
            print(f'По вышей ссылке прошли: {total_clicks} раз(а)')
        except requests.exceptions.HTTPError:
            print("Ошибка")
    else:
        try:
            bitlink = shorten_link(bitlly_token, user_link)
            print('Битлинк:', bitlink)
        except requests.exceptions.HTTPError:
            print("Неверный формат ссылки для сокращения")


if __name__ == '__main__':
    main()
