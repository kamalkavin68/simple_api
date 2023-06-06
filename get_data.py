import requests



def get_live_price(symbol: str):
    url = f"https://groww.in/v1/api/stocks_data/v1/accord_points/exchange/NSE/segment/CASH/latest_prices_ohlc/{symbol}"

    payload = {}
    headers = {
    'authority': 'groww.in',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en-GB;q=0.9,en;q=0.8,ta;q=0.7',
    # 'authorization': 'Bearer eyJraWQiOiJXTTZDLVEiLCJhbGciOiJFUzI1NiJ9.eyJleHAiOjE2ODQwNjIwMjcsImlhdCI6MTY4MTQ2MDIwMywibmJmIjoxNjgxNDYwMTUzLCJzdWIiOiJ7XCJlbWFpbElkXCI6XCJrYW1hbGthdmluNjhAZ21haWwuY29tXCIsXCJwbGF0Zm9ybVwiOlwid2ViXCIsXCJwbGF0Zm9ybVZlcnNpb25cIjpudWxsLFwib3NcIjpudWxsLFwib3NWZXJzaW9uXCI6bnVsbCxcImlwQWRkcmVzc1wiOlwiMjQwMTo0OTAwOjYzMjQ6NmVhYTo2OWU0OjlkY2U6MjlhYTpmZjUyLFwiLFwibWFjQWRkcmVzc1wiOm51bGwsXCJ1c2VyQWdlbnRcIjpcIk1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMTIuMC4wLjAgU2FmYXJpLzUzNy4zNlwiLFwiZ3Jvd3dVc2VyQWdlbnRcIjpudWxsLFwiZGV2aWNlSWRcIjpcIjU1MGMzMTBhLTgwMTEtNWU1Yy04NmRlLWRjNGE3MGNiMjZhMVwiLFwic2Vzc2lvbklkXCI6XCI5YTVmYjM2My1lMjMwLTQwZjMtYmY2ZS0zYTRiNmI3YjIzMDJcIixcInN1cGVyQWNjb3VudElkXCI6XCJBQ0M3NDM0OTI0NDc1NzE5XCIsXCJ1c2VyQWNjb3VudElkXCI6XCJBQ0M3NDM0OTI0NDc1NzE5XCJ9IiwiaXNzIjoiZ3Jvd3diaWxsaW9ubWlsbGVubmlhbCJ9.kU7Z7CuQXqtMUDqeO9sULT3KnziXsQ4IFUV__DDo245oCUktO63JeobLd7QCTXdp4UUSCgT1ACJcsEm84xrigA',
    'cookie': 'G_ENABLED_IDPS=google; _gcl_au=1.1.1655331589.1681449787; bfdskfds=light; we_luid=bcb1e0254530a6a5330820af86e9ccfb075c685b; g_state={"i_l":0}; lhtndhgfd=U2FsdGVkX19UpJY3QNGZ/uqIGS1nfmmNGZGbcqQkAGNLW6gEEccjHk/zdG5gm65LifLjaDaMW8Qv6GZfIp/0p2q1tssp+ZP6xWctsXQ3p3Y0cETNa5wHmvntERPQ7h7foyAkT09/spKfc4ETRlDOLL6cBlPOe0KhdQSO2Xg2/fZ73yayNvdY3MlZIwi4oKdVXwx/u3YO+0/0BUWihi+j4M+i4J55pW3j1QlT+z745rd5sEOXXTMnuhIc+ytPYcoaJehY5dkyUU3IdsJanEyZ4DykE/HfZnggjBHpc91UbgY/gHX0C1ka54oMXg1SdblQkebg/kIULW9j5KvyRbS1AsrK1OxZef2aq5VFCt3BQryx6IENnBz+qmoWIKUXxcXdNiO6knivre83Z9Lz7XYGWjgCR5H4a+tgJX84tOjjzRe3YxSVEefgXc/wuhu0e+mNmIZdaaQ4rFXDueJKaEKa5o8XwKzShcp0nBY4GWdhbyJGww2QgXFmNPMOjXu2a9CxxUZqV9tvMgsfI2FSvurnir+SVkixqCLXqW9WVk6ds0qr+asMJos5FT8ElbhEGlCIz/Ftudf2+Jz8q9ItW6JMZGydXKB+81nMUXHrsop1AiLcNrzVbMjYq9pLTCu0uTrOibeySLpC8F0dQtFG9GfZHBEc8uqQockxrtLc3iBgMvPQNM1uVkfRHJzdle4RRzk6KSXeuUvd1C7mokk7SQwed79qYCuo0FFK0U816Ttwa3jhWuv+IBAVEFcqH+jsM8TR1jNhJYtNss81qtMQzGxx0OcKhwhFVtQh6Pj3K3P5+CqjtO7/72nnKLsILEJZaGe9RW7xqLzeY+WJ7tnZhuDd6mrMXsJ77YrODINYGEotjvWIX+nbvTKS8zXuXFJSRKI/hOKtDZCh8pYO8QQBttZlBLdH1UUfuA6EknIs73AK1MngMBqB97DvWB4QmpvJ4VsezfBv5T9TgXbYMijFJBvUY2sNuz55kKZbv8hNYxjwBqaZZGvhRlBReG+6itPe4GNq9aiISn2uLgzkWwunz39fGBgQhfwZ/zQMecfN9BzsW6peUA0ZFXbpAGnGy6Vv1vXco/zQNbzod5tsy6EhOI4Yf5HbYKXsjJVjqg/Us47JfcquvhWELuRqRnH9QFQ3ghDLzF0yMLCKwBNIGnNMWwNaT0CX5xsV7IQGZAifgmjoG2Yd7YIs+KTQXNZrnJ/fws7keCwibXNPyQa8Q0EXJplOIGQgrDv/O/wUQUEibuoBdhZ/xOdWLHsSaoyj+5N8BKH0V+3FrMDK4JS19K+8/qYM5BERyYM4Rh3iZQgdL8GYysGM3o2n/v2VyUuyukBWwHqP; sc1sd3fd6gdf=true; _gid=GA1.2.2101972326.1681745025; arkeyt473rfh7834cd=U2FsdGVkX1/PeLpdRoz2QGNGg+txgj0mjf54Hqg/ODIXMxx59b3iy/XkIotHLY+PCzE4zWKhGZhrRXwBUAEOXWAJnzpjc/5uoyAmTfAHBL2UC00iRdVhldMU1mtRPzNRSnqrR0oWH163eB8gkAFYMIfpW9DuxOw2JNpLpDwh+zWmrl8HcM2lZqDq9tgplYQ+zFJMW7KRR81UP6XpfHYa1JVaFZjH5EaTsoVrssYJGNk1SRZ+2xLt7vD9PZ83PAaWpi6WacE15NkJ8/f7D/Z5QEJZ+qlq6Gx6+SLbg0Ujf+CCq+N4FTRjQ+EAis/rJVlFDV7DOOH3DHI4d55oWAXEe5/CKy1n+FYSv54wv+ow1bdFeDTzThXG3+KV0QMrUNp8G7dicSBG51Vo1Bb8NWJONh4G70qq6wcGTXY5GLCVC+XYc3a5RtT+/f6jxSuU4PvR3K3bLg8HPPMs0Fl402E9KjUWdV3CNrWxxOeI70LOrrYMoK1GTbSjM5NtW6KYpZLwVBfKz47af458GbMUr/hjesYbJbKFXVN84b/IfRYjS20BLb7coCSZhD/2oEvnqZxoyDjsiz5lbEECNx5zUo9nvwipP7LkTRFkuSvxnaB7yDLvx7NOUCSOtIqskdiR4+CMupfyPP6VQuzfVfE2emmv1fEFuSOBNzAoUDL5jds7vDaxwHny8S/ut9t+9k2JDF38KgVh7XdsJIh89r5nONF80slAZKWZtf6+8Ax08mKDQ+WN+2ADqDuGyE4YfOQG9a2XyQHQFxN0NuRCe/ARz8y/ddNi/sxRgEylvXRN0Dfs7YAtLeW0NXNvLuNMOxrV9sWvLSHnmv649XfwicDDN1HuH6arNWP10NJQzlMogIr5DCj3R9pYH8ptjrUkMazOdxDa; AUTH_SESSION_ID=U2FsdGVkX19R+CMTbKNNaA5R2k//lLNXBCFJIx7J+XnRpIlm7lWll2yz5N/AMgmvtigRdIUnbwMf2Yjbsj1OGg==; __cf_bm=75KLX5s_Jcs3RvoZ65dTCVMS0RgmidtGDwrjB2kXO9E-1681747407-0-AdO4FVARvL5odRSc9HcncwjgXMxFBtHno6KwGVLf7NGQOw3VTo0jQx0mrDZRnSZoSOylQ4PTysQUCJg5bcCHXyU=; __cfruid=af4cfa32212cfbbfbf5a13319119fd3653e48e1f-1681747407; _cfuvid=cnzIcd3tHaWGKM67p_YP5x6PUHAQq_ZkdivM1HJSFbk-1681747407692-0-604800000; _gat_UA-76725130-1=1; _ga=GA1.2.940432028.1650253765; _ga_BNCSRMD1F4=GS1.1.1681745023.11.1.1681747507.0.0.0',
    'referer': 'https://groww.in/stocks/infosys-ltd',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'x-app-id': 'growwWeb',
    'x-device-id': '550c310a-8011-5e5c-86de-dc4a70cb26a1',
    'x-device-type': 'desktop',
    'x-platform': 'web',
    'x-request-checksum': 'dWR0NWYjIyMwWXJKWExmcUI1RlpMWTc1cXlLa3BldDFhbERiV3RtNmZEcWlTL2NVMjhTUE9Ec01DSk5oUk1XdEVkUVVGMndIM0VOY0I3TDh2bnRJU3o2NWJWV3hkRTl0TFlCSUh0MTZ0N2Y5NStQcmFpUT0=',
    'x-request-id': 'b336c65e-ed23-4655-a306-f0b113c9b9c2',
    'x-user-campaign': 'Bearer eyJraWQiOiJJQjYxMkEiLCJhbGciOiJFUzI1NiJ9.eyJleHAiOjE2ODE4MjM5MTEsImlhdCI6MTY4MTc0NjIzNCwibmJmIjoxNjgxNzQ2MTg0LCJzdWIiOiJ7XCJjcmVhdGVkQXRcIjpcIjIwMjMtMDQtMTdUMTU6NDM6NTQuMzU5KzAwOjAwXCIsXCJ1c2VyQWNjb3VudElkXCI6XCJBQ0M3NDM0OTI0NDc1NzE5XCIsXCJpc1N1Y2Nlc3NcIjp0cnVlLFwic2Vzc2lvbklkXCI6XCI3ZDlmNDg2Ny1lMTQ0LTQzZWMtOGQwZS00YzI3NzI2ZTUyN2JcIixcImlwQWRkcmVzc1wiOlwiNDUuMjUxLjMzLjE5NSxcIixcImRldmljZUlkXCI6bnVsbCxcInN1cGVyQWNjb3VudElkXCI6XCJBQ0M3NDM0OTI0NDc1NzE5XCIsXCJzdG9ja3NBY2NvdW50U3RhdHVzXCI6XCJOT1RfQ09NUExFVEVEXCJ9IiwiaXNzIjoiZ3Jvd3diaWxsaW9ubWlsbGVubmlhbCJ9.ndTjBAD0NIBJvwv12hx0EiPfri86D4DIhRCQPSl3uDqBeDB23AuodwGxeAGGgW2pXdXn1rMe4xvVTXgAq57VGQ'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()