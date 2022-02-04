import webbrowser #работа с браузером
def search_for_term_on_google(*args: tuple):
    """
    Поиск в Google с автоматическим открытием ссылок только для пк версии
    """
    search_term = "Кто будет участвовать на олимпиаде"
    search_results = []

    # открытие ссылки на поисковик в браузере
    url = "https://google.com/search?q=" + search_term
    webbrowser.get().open(url)