from pathlib import Path

EXPECTED_STATUS = {
    'A': ('Active', 'Accepted'),
    'D': ('Deferred',),
    'F': ('Final',),
    'P': ('Provisional',),
    'R': ('Rejected',),
    'S': ('Superseded',),
    'W': ('Withdrawn',),
    '': ('Draft', 'Active'),
}

DOWNLOAD_LOG_INFO = 'Архив был загружен и сохранён: {archive_path}'
START_LOG_INFO = 'Парсер запущен!'
FINISH_LOG_INFO = 'Работа парсера завершена'
URLS_NOT_FOUND_LOG_ERROR = ('Не найдены ссылки на документацию '
                            'на странице {url}')
GENERALISED_LOG_ERROR = 'Ошибка в работе парсера: {error}'
FILE_OUTPUT_LOG_INFO = 'Файл с результатами был сохранён: {file_path}'

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
DT_FORMAT = '%d.%m.%Y %H:%M:%S'

LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'

OUTPUT_FORMAT_DEFAULT = None
OUTPUT_FORMAT_FILE = 'file'
OUTPUT_FORMAT_PRETTY = 'pretty'


BASE_DIR = Path(__file__).parent
DOWNLOADS_DIR = BASE_DIR / 'downloads'
LOG_DIR = BASE_DIR / 'logs'
LOG_FILE = LOG_DIR / 'parser.log'
RESULTS_DIR = BASE_DIR / 'results'
DOWNLOADS = 'downloads'
RESULTS = 'results'


MAIN_DOC_URL = 'https://docs.python.org/3/'
MAIN_PEP_URL = 'https://peps.python.org/'
