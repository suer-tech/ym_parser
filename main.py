import requests

from db_conf import conn
from product import Product


def get_data(products_page):
    cookies = {
        'yandexuid': '7876350741706419974',
        'yuidss': '7876350741706419974',
        'ymex': '2021779975.yrts.1706419975',
        'yashr': '7727414501706420460',
        'amcuid': '6761591241706420483',
        'cmp-merge': 'true',
        'reviews-merge': 'true',
        'skid': '796626191706597083',
        'oq_shown_onboardings': '%5B%5D',
        'oq_last_shown_date': '1706597083295',
        'muid': '1152921510211329024%3A4NeHeaNYTl8xgkzoNN6CyvjCK6BB%2BeN5',
        'nec': '0',
        '_ym_uid': '1706597088552854179',
        '_ym_d': '1706597106',
        'yandex_gid': '172',
        'yp': '1710589676.ygu.1',
        'i': 'U4mjVzk50DyO48z3N040rSCuY7F1mFUMmw8wYycki5ZOxuquWz5/uDHksyx5p8pxvc+Ov5T3T/0y7gPfyGAAp+/HUVE=',
        'receive-cookie-deprecation': '1',
        '_ym_isad': '2',
        'spvuid_market:list_e7a346_expired:1710398993886': '1710312593824%2Fbbbe97556b90a75c561c9c2e85130600',
        'spvuid_market:product_2a1fe8_expired:1710400433876': '1710314033827%2F839cf4dab4a9f0fa05cd708485130600',
        'spvuid_market:product_59f101_expired:1710400938320': '1710314538277%2Feaaf29f5cc1d2d77b21982a285130600',
        'spvuid_market:product_528dfb_expired:1710404591462': '1710318191358%2Fec721501449bf80788b23f7c86130600',
        'yabs-vdrf': 'A0',
        'spvuid_market:index_3751af_expired:1710405012205': '1710310375269%2F2e39ac0d1333587b63a55faa84130600',
        'spvuid_market:list_a01169_expired:1710407649633': '1710321249542%2F8827b16c5ee17a85d3df873287130600',
        'global_delivery_point_skeleton': '{%22regionName%22:%22%D0%A3%D1%84%D0%B0%22%2C%22addressLineWidth%22:25}',
        'is_gdpr': '0',
        'is_gdpr_b': 'CL/XRBCk8AEoAg==',
        'bh': 'Ej8iQ2hyb21pdW0iO3Y9IjEyMiIsIk5vdChBOkJyYW5kIjt2PSIyNCIsIkdvb2dsZSBDaHJvbWUiO3Y9IjEyMiIaBSJ4ODYiIhAiMTIyLjAuNjI2MS4xMTIiKgI/MDoJIldpbmRvd3MiQggiMTUuMC4wIkoEIjY0IlJcIkNocm9taXVtIjt2PSIxMjIuMC42MjYxLjExMiIsIk5vdChBOkJyYW5kIjt2PSIyNC4wLjAuMCIsIkdvb2dsZSBDaHJvbWUiO3Y9IjEyMi4wLjYyNjEuMTEyIiI=',
        'gdpr': '0',
        'visits': '1706597083-1710310375-1710378582',
        'js': '1',
        'rcrr': 'true',
        'ugcp': '1',
        '_yasc': 'NhJqGB3HhGr/1O628EbibhWoKICcCYIvKWNT80RHk5yjdyvIVYL45g+EIeRXTwTCDhpFuyaWvE4KBdM=',
        'parent_reqid_seq': '1710378582533%2F9c2a8d3716d232aeb9e3d78b94130600%2C1710378616324%2Fa8700ba06c605256c582db8d94130600%2C1710379002840%2F93cdb87402a6b736b145e5a494130600',
    }

    headers = {
        'authority': 'market.yandex.ru',
        'accept': '*/*',
        'accept-language': 'ru,ru-RU;q=0.9',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://market.yandex.ru',
        'referer': 'https://market.yandex.ru/catalog/mobilnye-telefony-61808?rs=eJxtUD1IQnEcfP8Ser3pjWYF_zYhCjRQTANxioaKxhCeL9OSJMWPqeWREDU4BG0tuoZFBEGUkQ0RCC6FQzRkDdEkNETR1LsjmlqO4-6434e33DsvboQSS04BZ4M2ytcQ-PMF-N2kjZ0ylMo73NghdQtcuYaubAMbg3UbrTm44TfqJ-CNc_DOKNzOHpRYm3wGKBcw1xphfwmucgsePgVaxQCUbzYcA-UX5nY2rtDchGt5mI8yc8DmaXRWPtmpgssSpwThxgR4Y4yb7PCKLd77wYZ73lKDW9mn3sYHZI1tD8w8cocX7iOZGbqEEgn99ct-8ir_4OKGT_yPxf4wN-lyylqwKVSP3-vx-QL-yKbQBjRVFbpwOqRD73H1LSeSZjFdkIpb0cZpqU4hha67nEtmPhU34mYuU8wn0kY2babWjUImK4_qK-7WblSb-M1rUrPzw__m8wkzF181vPKsa7hb1UVd_ABurbGX&hid=91491&local-offers-first=0&glfilter=21194330%3A34066443',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sk': 's8ac4b8f19baf11b871baad379a50aacc',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'x-market-app-version': '2024.1.161.t2214332401',
        'x-market-core-service': '<UNKNOWN>',
        'x-market-page-id': 'market:list',
        'x-requested-with': 'XMLHttpRequest',
        'x-retpath-y': 'https://market.yandex.ru/catalog/mobilnye-telefony-61808?rs=eJxtUD1IQnEcfP8Ser3pjWYF_zYhCjRQTANxioaKxhCeL9OSJMWPqeWREDU4BG0tuoZFBEGUkQ0RCC6FQzRkDdEkNETR1LsjmlqO4-6434e33DsvboQSS04BZ4M2ytcQ-PMF-N2kjZ0ylMo73NghdQtcuYaubAMbg3UbrTm44TfqJ-CNc_DOKNzOHpRYm3wGKBcw1xphfwmucgsePgVaxQCUbzYcA-UX5nY2rtDchGt5mI8yc8DmaXRWPtmpgssSpwThxgR4Y4yb7PCKLd77wYZ73lKDW9mn3sYHZI1tD8w8cocX7iOZGbqEEgn99ct-8ir_4OKGT_yPxf4wN-lyylqwKVSP3-vx-QL-yKbQBjRVFbpwOqRD73H1LSeSZjFdkIpb0cZpqU4hha67nEtmPhU34mYuU8wn0kY2babWjUImK4_qK-7WblSb-M1rUrPzw__m8wkzF181vPKsa7hb1UVd_ABurbGX&hid=91491&local-offers-first=0&glfilter=21194330%3A34066443',
    }

    json_data = {
        'params': [
            {
                'hid': 91491,
                'nid': 61808,
                'how': 'dpop',
                'searchPlace': '__standalone__',
                'filters': {
                    'glfilter': '21194330:34066443',
                },
                'page': products_page,
                'withResults': True,
                'rs': 'eJxtUD1IQnEcfP8Ser3pjWYF_zYhCjRQTANxioaKxhCeL9OSJMWPqeWREDU4BG0tuoZFBEGUkQ0RCC6FQzRkDdEkNETR1LsjmlqO4-6434e33DsvboQSS04BZ4M2ytcQ-PMF-N2kjZ0ylMo73NghdQtcuYaubAMbg3UbrTm44TfqJ-CNc_DOKNzOHpRYm3wGKBcw1xphfwmucgsePgVaxQCUbzYcA-UX5nY2rtDchGt5mI8yc8DmaXRWPtmpgssSpwThxgR4Y4yb7PCKLd77wYZ73lKDW9mn3sYHZI1tD8w8cocX7iOZGbqEEgn99ct-8ir_4OKGT_yPxf4wN-lyylqwKVSP3-vx-QL-yKbQBjRVFbpwOqRD73H1LSeSZjFdkIpb0cZpqU4hha67nEtmPhU34mYuU8wn0kY2babWjUImK4_qK-7WblSb-M1rUrPzw__m8wkzF181vPKsa7hb1UVd_ABurbGX',
                'isLocalOffersFirst': False,
                'prevTotal': 2594,
                'isDefaultRelevance': False,
                'isDeliveryFilterChange': False,
            },
        ],
        'path': '/catalog/mobilnye-telefony-61808?hid=91491&rs=eJxtUD1IQnEcfP8Ser3pjWYF_zYhCjRQTANxioaKxhCeL9OSJMWPqeWREDU4BG0tuoZFBEGUkQ0RCC6FQzRkDdEkNETR1LsjmlqO4-6434e33DsvboQSS04BZ4M2ytcQ-PMF-N2kjZ0ylMo73NghdQtcuYaubAMbg3UbrTm44TfqJ-CNc_DOKNzOHpRYm3wGKBcw1xphfwmucgsePgVaxQCUbzYcA-UX5nY2rtDchGt5mI8yc8DmaXRWPtmpgssSpwThxgR4Y4yb7PCKLd77wYZ73lKDW9mn3sYHZI1tD8w8cocX7iOZGbqEEgn99ct-8ir_4OKGT_yPxf4wN-lyylqwKVSP3-vx-QL-yKbQBjRVFbpwOqRD73H1LSeSZjFdkIpb0cZpqU4hha67nEtmPhU34mYuU8wn0kY2babWjUImK4_qK-7WblSb-M1rUrPzw__m8wkzF181vPKsa7hb1UVd_ABurbGX&local-offers-first=0&glfilter=21194330%3A34066443',
    }

    response = requests.post(
        'https://market.yandex.ru/api/resolve/?r=src/resolvers/search/resolvePoorRemoteSearch:resolvePoorRemoteSearch',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    if response.status_code == 200:
        json_response = response.json()
        return json_response


def main():
    products_page = 1
    response = get_data(products_page)
    data = response['results'][0]['data']['search']['collections']['offer']

    for offer in data:
        data_offer = data[offer]
        product = Product(data_offer)
        product.save_to_database(conn)


if __name__ == '__main__':
    main()