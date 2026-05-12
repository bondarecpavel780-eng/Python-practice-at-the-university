from django.http import HttpResponse


def list_singers():
    singers = [
        {'id': 1, 'name': 'Океан Ельзи', 'genre': 'Рок', 'lead_singer': 'Святослав Вакарчук', 'slug': 'okean-elzy'},
        {'id': 2, 'name': 'Бумбокс', 'genre': 'Рок, Хіп-хоп', 'lead_singer': 'Андрій Хливнюк', 'slug': 'bumboks'},
        {'id': 3, 'name': 'Gazan', 'genre': 'kids song', 'lead_singer': 'Gazan', 'slug': 'gazan'}
    ]
    return singers


def popular_singers(request):
    html_content = """
        <h1>Популярні співаки України</h1>
        <ul>
    """

    for singer in list_singers():
        html_content += f"<li><strong>{singer['name']}</strong> - {singer['genre']} (Вокаліст: {singer['lead_singer']})</li>"

    html_content += """
        </ul>
    """

    return HttpResponse(html_content, content_type='text/html; charset=utf-8')


def singer_card(request):

    singer_id = request.GET.get('id')

    singer_id = int(singer_id)

    singers = list_singers()

    singer = next((s for s in singers if s['id'] == singer_id), None)

    # Створюємо HTML для відображення інформації про співака
    html_content = f"""
    <html>
    <body>
        <h1>{singer['name']}</h1>
        <p>Жанр: {singer['genre']}</p>
        <p>Вокаліст: {singer['lead_singer']}</p>
    </body>
    </html>
    """

    return HttpResponse(html_content, content_type='text/html; charset=utf-8')


def popular_singers(request):
    html_content = """
    <html>
    <body>
        <h1>Популярні співаки України</h1>
        <ul>
    """

    for singer in list_singers():
        singer_url = f"/singer/?id={singer['id']}"
        html_content += f"<li><a href='{singer_url}'><strong>{singer['name']}</strong></a>" \
                        f" - {singer['genre']} (Вокаліст: {singer['lead_singer']})</li>"

    html_content += """
        </ul>
    </body>
    </html>
    """

    return HttpResponse(html_content, content_type='text/html; charset=utf-8')