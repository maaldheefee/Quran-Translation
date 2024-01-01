# Ebook Generation

This generates an ebook (epub format) of the Quran with Divehi translations. 

## Features

- Retrieves Quran text and metadata from [qurancomplex.gov.sa](https://qurancomplex.gov.sa/techquran/dev/)
- Add Divehi translations from this repo
- Translations for multiple ayahs are displayed woithouy repetition, with the grouop of ayahs combined.
- CSS classes added to ayah markers, sajdah and hizm barkers, and waqf symbols for styling
- Generate EPUB3 ebook with fonts embedded

## Usage

To generate the ebook:

```
python main.py
```

This will output `test.epub` containing the full Quran.

## Customization

The translation text file can be replaced to create ebooks with other translations. Modify `TRANS_FILE` in `main.py`.

Formatting and styling can be customized by editing files in the `epub` module.

## Credits

- Quran text and metadata from [Tanzil Project](https://tanzil.net) 
- Divehi translation from [President's Office of Maldives](https://www.presidencymaldives.gov.mv)
- Ebook generation powered by [EbookLib](https://github.com/aerkalov/ebooklib)