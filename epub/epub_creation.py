from pathlib import Path

from ebooklib import epub

from epub.text_formatting import format_aya_text, format_trans_text
from epub.utils import merge_multi_ayah_translations

BASE_DIR = Path(__file__).resolve().parent.parent


def generate_chapter_html(sura_no, surah_data):
    # Add surah name and basmalah
    sura_name = surah_data[0]["sura_name_ar"]
    html_content = f'<h1 class="surah_name" lang="ar">سُورَةُ {sura_name}</h1>\n'
    if int(sura_no) != 9 and int(sura_no) != 1:
        html_content += '<p class="basmalah" lang="ar">بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ</p>\n'

    aya_list = []
    trans_texts = []

    for row in surah_data:
        aya_list.append(format_aya_text(row["aya_text"][:-2], row['aya_no']))
        translation = format_trans_text(row.get("translation", ""))
        trans_texts.append(translation)

    merged_translations = merge_multi_ayah_translations(aya_list, trans_texts, " ")
    for aya_text, trans_text in merged_translations:
        html_content += f'<p class="ayah_text" lang="ar">{aya_text}</p><p class="translation" lang="dv">{trans_text}</p>\n'
    return html_content


def create_epub_book(surahs):
    book = epub.EpubBook()
    book.set_title("ކީރިތި ޤުރްއާނުގެ ދިވެހި ތަރުޖަމާ")
    book.set_language("dv")

    book.add_author("ރައީސުލްޖުމްހޫރިިއްޔާގެ އޮފީސް")
    book.set_direction("rtl")

    default_css = """@font-face {
  font-family: "hafs";
  src: url(../font/uthmanic_hafs_v20.ttf) format("truetype");
}
@font-face {
  font-family: "tharujamaanu";
  src: url(../font/merged-400.woff2) format("woff2");
}
body {
  direction: rtl;
  font-size: 18pt;
}
.surah_name {
  font-family: "hafs";
  text-align: center;
  margin-bottom: 15px;
  font-weight: 400;
}
.basmalah {
  font-family: "hafs" !important;
  text-align: center;
  margin-bottom: 20px;
}
p.ayah_text {
  font-family: "hafs" !important;
  line-height: 2;
  margin-bottom: 10px;
}
p.translation {
  font-family: "tharujamaanu" !important;
  line-height: 1.8;
  margin-bottom: 20px;
}
.ayah_num_ar {
  color: red;
}
.waqf {
  color: green;
}
.symbol {
  color: blue;
}
"""
    stylesheet = epub.EpubItem(
        uid="style_nav",
        file_name="style/styles.css",
        media_type="text/css",
        content=default_css,
    )

    font_hafs_ttf = open(BASE_DIR / 'epub/fonts/uthmanic_hafs_v20.ttf', 'rb').read()
    font_thaana_ttf = open(BASE_DIR / 'epub/fonts/merged-400.woff2', 'rb').read()

    font_hafs_ttf_item = epub.EpubItem(
        uid="font_hafs_ttf",
        file_name="font/uthmanic_hafs_v20.ttf",
        media_type="application/font-sfnt",
        content=font_hafs_ttf
    )
    font_thaana_ttf_item = epub.EpubItem(
        uid="font_thaana",
        file_name="fonts/merged-400.woff2",
        media_type="font/woff2",
        content=font_thaana_ttf
    )
    book.add_item(stylesheet)
    book.add_item(font_hafs_ttf_item)
    book.add_item(font_thaana_ttf_item)

    # TODO: add title page with metadata like repo link and generation date
    # TODO: add intro chapter

    for sura_no, surah_data in surahs.items():
        chapter = epub.EpubHtml(title=f'{surah_data[0]["sura_name_ar"]}', file_name=f"surah_{sura_no}.xhtml", lang="dv")
        chapter.content = generate_chapter_html(sura_no, surah_data)
        chapter.add_item(stylesheet)
        book.add_item(chapter)

        book.toc.append(epub.Link(f"surah_{sura_no}.xhtml", f'{surah_data[0]["sura_name_ar"]}', f"surah_{sura_no}"))
        book.spine.append(chapter)

    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    epub.write_epub("test.epub", book, {})
