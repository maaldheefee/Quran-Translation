from pathlib import Path

from epub.data_processing import get_surah_data
from epub.epub_creation import create_epub_book

BASE_DIR = Path(__file__).resolve().parent.parent
QURAN_DATA_FILE = BASE_DIR / "epub/data/hafsData_v2-0.csv"
TRANS_FILE = BASE_DIR / "alt_dv.divehi.txt"

surahs = get_surah_data(QURAN_DATA_FILE, TRANS_FILE)

if __name__ == "__main__":
    create_epub_book(surahs)
